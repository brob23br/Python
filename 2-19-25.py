def set_convert(sample_values, *new_values):
    sample_values = set(sample_values)
    for new_value in new_values:
        sample_values.add(new_value)
    return sample_values

sample_values = ['user4', 'admin10', 'user5', 'user8', 'admin6', 'admin3', 'user9', 'guest9', 'guest5', 'admin3']

# You may alter the code below to view your return value(s).
# Only the set_convert function will be graded for this assessment.

print(set_convert(sample_values))
print(set_convert(sample_values, "newuser1", "newuser2", "newuser3"))