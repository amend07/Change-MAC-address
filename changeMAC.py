#!/usr/bin/env python3
import subprocess
import optparse
import re
def getArg():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    parser.add_option("-h", "--help", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify a valid interface, type --help for help")
    elif not options.new_mac:
        parser.error("[-] Please enter valid mac address,  type --help for help")
    return options
def changeMac(interface,new_mac):
    print("[*]Changing MAC address for ",interface,"to",new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig", interface, "hw","ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read mac address")

options = getArg()

current_mac = get_current_mac(options.interface)
print("[+] Current MAC = ", str(current_mac))
changeMac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if options.interface == current_mac:
    print("[+] MAC address successfully changed to",current_mac)
else:
    print("[-] MAC address did not changed")