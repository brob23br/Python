

def is_valid_ipv4(ip_address):
    ipaddress_split = ip_address.split(".")
    if len(ipaddress_split) != 4:
        return False

    for octet in ipaddress_split:
        if not octet.isdigit():
            return False

        num = int(octet)
        if num < 0 or num > 255:
            return False

        if len(octet) > 1 and octet[0] == "0":
            return False

    return True


# You may alter the code below to view your return value(s).
# Only the is_valid_ipv4 function will be graded for this assessment.

# valid
print(is_valid_ipv4("192.168.1.1"))

# not valid
print(is_valid_ipv4("255.ABC.450"))

print(is_valid_ipv4("55.555.55.5"))