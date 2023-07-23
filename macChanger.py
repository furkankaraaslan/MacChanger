import subprocess
import optparse
import re


def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()


def change_mac(interface, mac_address):

    print("Mac Changer Started!!")

    #subprocess.call(["ifconfig", interface, "down"])
    #subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    #subprocess.call(["ifconfig", interface, "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None


(user_input, argument) = get_user_input()
change_mac(user_input.interface, user_input.mac_address)
final_mac = control_new_mac(str(user_input.interface))

if final_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")
