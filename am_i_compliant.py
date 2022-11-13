# ---------------------------------------------------------------------------
# -  Owner: Ananas                                                          -
# -  Purpose: This code checks for three parameters that govern compliance  -
# -     and returns whether a device is compliant or not                    -
# -  Date Updated: 10/11/22                                                 -
# ---------------------------------------------------------------------------

# Import required modules
import subprocess

# MAC commands used
jamf_update = "sudo jamf policy"
encryption_command = "sudo fdesetup status"
management_command = "sudo jamf manage"
device_information_command = "sw_vers"


# Main function that checks for parameters
def checks():
    # Checks if device is encrypted
    encryption_check = subprocess.getoutput(encryption_command)
    if "FileVault is On." in encryption_check:
        check_1 = True
    else:
        check_1 = False

    # Checks if device is managed by JAMF
    management_check = subprocess.getoutput(management_command)
    if "The JSS is available." in management_check:
        check_2 = True
    else:
        check_2 = False

    # Checks if device is at least Monterey 12.6
    os_check = subprocess.getoutput(device_information_command)
    if "ProductVersion:	12.6" in os_check:
        check_3 = True
    else:
        check_3 = False

    # Checks if all parameters for compliance is met. Returns the result true of false
    check_list = (check_1, check_2, check_3)
    if all(check is True for check in check_list):
        return True
    else:
        return False


# Displays whether a device compliant or not
if checks() is True:

    print("This device is compliant!")

else:
    print("This device is NOT compliant!")
