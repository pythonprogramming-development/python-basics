print ({} is {}) 

obj = {'r':'e'}
print(obj.get('r'))
print(obj['r'])

lookup = dict((('aa', 11), ('bb', 22), ('cc', 33), (23, 33)))
print(lookup)

if 'aa' in lookup:
    print ('contains key "aa"')

print(lookup['aa'])
print(lookup.get('aa'))

# A dictionary is an iterator object that produces its keys.

for key in lookup:
    print ('key: %s' % key)

for key in obj:
    print ('key: %s' % key)

print (lookup.keys())
print (obj.keys())

# to fetch object key values use items
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678} 
for name, phone in table.items(): 
    print(f'{name:10} ==> {phone:10d}')
    print(name, phone)


# Python program to demonstrate
# defaultdict
  
  
from collections import defaultdict
  
  
# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])



