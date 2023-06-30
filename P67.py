#Dictionary on Python

phone_no={
   'Rayn':1234,
   'Kaiox':3534,
   'Ioxk':9443
}

print(phone_no)

# For print specific Key value

print(phone_no['Ioxk'])

# second method you can useag dict word

'''
phone_no2=dict{
   'Rayn':1234,
   'Kaiox':3534,
   'Ioxk':9443
'''

#for change specifc value

phone_no['Rayn']=9099
print(phone_no)

#for add new key and value

phone_no['Jios']={5352,3523}

print(phone_no)

#adding value in value

phone_no['Rayn']={"secon":5352,"keio":2646}

print(phone_no['Rayn'])

print(phone_no)

print(phone_no['Rayn']['secon']) #-> calling specifc value by key on also have key

#Another method for access

print(phone_no.get('Rayn')) #-> if some key is not match so its not giving error its just print error.

#for delete

#del phone_no['Rayn']

#print(phone_no.pop('Rayn')) #using pop

print(phone_no.popitem()) #-> its remove last added key value
print(phone_no)

#print(phone_no.clear()) #-> For delete all the value and key from dict

print(phone_no.keys()) #-> for acessing keys from dict

print(phone_no.values()) #-> for acessing values from dict


print(phone_no.items()) #-> its print key and value with tuple







