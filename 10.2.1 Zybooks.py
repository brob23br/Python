'''Complete the function "generate_users()" to generate sequentially numbered usernames starting at 1 until an indicated end value.
The function should accept a string and a numeric value,generate usernames beginning with the string and ending with increasing numeric values
(e.g., "test_account1", "test_account2", "test_account3"), returning the usernames as a set to preserve uniqueness.
Only the set returned by generate_users() will be graded for this assignment.
The function should work for any string and positive integer passed to the function beyond the examples provided.'''

def generate_users(username_string, num_accounts):
    username_string_concat = [username_string + str(num_accounts) for num_accounts in range(0, 256)]

    for i in username_string_concat:
        print(i)




# You may alter the code below to view your return value(s).
# Only the generate_users function will be graded for this assessment.

print(generate_users("test_account", 4))