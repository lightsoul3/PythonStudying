import pprint

people = {}
people['Arthur'] = {'Name': 'Arthur Dent', 
                    'Gender': 'Male', 
                    'Occupation': 'Sandwich-Maker'}
people['Trillian'] = {'Name': 'Tricia McMillian', 
                      'Gender': 'Female', 
                      'Occupation': 'Mathematician'}
people['Robot'] = {'Name': 'Marvin', 
                   'Gender': 'Paranoid Android', 
                   'Occupation': 'Unknown'}

pprint.pprint(people)

print(people['Arthur']['Occupation'])