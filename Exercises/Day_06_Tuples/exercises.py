



# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Lisa', 'Rochelle', 'Mitchell')
brothers = ('Keith', 'Ellis', 'Nick')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters.__add__(brothers)

# How many siblings do you have?
print('Total siblings:', siblings.__len__())

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.extend(['Father', 'Mother'])
family_members = tuple(family_members)
print(family_members)