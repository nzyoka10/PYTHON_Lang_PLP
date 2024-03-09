# 
# ? function to print <Multiple items>
# 

def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items("David", "Eric", "Steve")

print('\n')

# ! Example 2
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(name1="David", name2="Eric", name3="Steve")


