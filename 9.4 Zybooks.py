# define check_network_status()
def check_network_status(network_connection, firewall_status):
    if type(network_connection) != bool or type(firewall_status) != bool:
        return "Unexpected network status"

    elif network_connection and firewall_status:
        return "No issues detected"

    elif network_connection and not firewall_status:
        return "Proceed with caution"

    elif not network_connection:
        return "Network not detected"

    else:
        return "Unexpected network status"


# You may alter the code below to view your return value(s).
# Only the check_network_status function will be graded for this assessment.

# No issues detected
print(check_network_status(True, True))

# Unexpected network status
print(check_network_status(True, "Nope"))