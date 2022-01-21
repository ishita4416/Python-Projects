#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("Please specify an new mac address, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_curr_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface])
    mac_address_search_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res)

    if mac_address_search_res:
        return mac_address_search_res.group(0)
    else:
        print("Could not read the mac address")

options = get_arguments()
curr_mac = get_curr_mac(options.interface)
print("Current Mac is " + str(curr_mac))

change_mac(options.interface, options.new_mac)

curr_mac = get_curr_mac(options.interface)
if curr_mac == options.new_mac:
    print("Mac Address was successfully change to "+ curr_mac)
else:
    print("Mac Address did not get changed")


# interface = raw_input("Enter the Interface")
# new_mac = raw_input("Enter the New mac address")
# interface = options.interface
# new_mac = options.new_mac

# print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
# subprocess.call("ifconfig", shell=True)

# to make it more secure, we use the other version of subprocess call so that
# we aren't using a string that can be modified and hijacked by an external party

# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])
