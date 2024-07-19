# Change-MAC-address
Python-based Media Access Control(MAC) address changer

MAC Address Changer is a Python-based tool designed for Linux systems to help users bypass MAC filtering by changing their MAC address. This program allows you to spoof your MAC address, enabling you to enhance your privacy or access restricted networks.

**Features**
- Change your MAC address to a specified value.
- Simple and user-friendly command-line interface.

**Prerequisites**
- Python 3.x
- optparse module (standard library)
- subprocess module (standard library)
- Root privileges (required to change the MAC address)

**Installation and Usage**
1. Clone the repository
` git clone https://github.com/amend07/change-mac-address.git `
2. Navigate to project directory
` cd change-mac-address `
3. Run the script
` sudo python changeMAC.py --interface eth0 --mac 00:11:22:33:44:55 `

**Disclaimer**

This tool is intended for educational purposes only. The author is not responsible for any misuse of this tool. Use it responsibly and only on networks where you have permission.
