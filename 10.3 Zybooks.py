'''Complete the function remove_admin() to remove admin usernames from a list through the first n usernames. Admin usernames begin with "admin" as the first 5 characters.
The function should accept a list of usernames and a numeric value representing a limit.
Remove any admin usernames from the list based on the limit value. For example, remove_admin(username_list, 5) would remove admin usernames from the first 5 entries in the username_list.

Return the username list with admin accounts now removed with "validated" added as the last entry. Additionally, return the number of admin accounts removed.'''

def remove_admin(usernames, limit):
    i = 0
    validated = []
    admin_count = 0

    for i in range(limit):
        if not usernames[i].startswith("admin"):
            validated.append(usernames[i])
        else:
            admin_count += 1

    validated += usernames[limit:]

    validated.append("validated")

    # remove "admin" usernames based on limit
    # return validated list with appended "validated" entry
    # return count of removed admin usernames

    return validated, admin_count


# You may alter the code below to view your return value(s).
# Only the generate_users function will be graded for this assessment.

usernames = ['FN84', 'adminPD66', 'OP83', 'IT32', 'OP27', 'OP13', 'IT95', 'adminHR73', 'OP12', 'HR31']
print(remove_admin(usernames, 10))

# Expected return
# (['FN84', 'OP83', 'IT32', 'OP27', 'OP13', 'IT95', 'OP12', 'HR31', 'validated'], 2)