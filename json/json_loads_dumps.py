''' JavaScript Object Notation'''
import json

json_string = '''
{
    "people": [
        {
            "name": "john smith",
            "phone": "615-555-7164",
            "email": ["john@bogus.com", "jsmith@place.com"],
            "has_license": false
        },
        {
            "name": "jane doe",
            "phone": "560-555-7164",
            "email": null,
            "has_license": true
        }
             ]
}
'''
data=json.loads(json_string)
# print(data)
# print(type(data))
# print(data['people'])
print(type(data['people'])) #Returns a type list
for person in data['people']:
    # print(person)
    # print(person['phone'])
    del person['phone'] # Delete phone key in json file

new_data=json.dumps(data,indent=2, sort_keys=True) # Use indent parameter to make output readable
print(new_data)
