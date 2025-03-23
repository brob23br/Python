def exponents(bases, powers):
    new_list = []
    for b in bases:
      for p in powers:
        raised = b ** p
        new_list.append(raised)
    return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))