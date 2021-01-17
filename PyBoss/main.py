import os
import csv

input_path = os.path.join('Resources', 'employee_data.csv')
output_path = os.path.join('Output', 'new_employee_data.csv')

# List variables
emp_id = []
names = []
first_names = []
last_names = []
dob_ymd = []
dob_mdy = []
ssn = []
ssn_hiden = []
states = []
states_abbrev = []

# Coping and pasting a dictionary of state name conversions found online...
# the original file where I get this is saved in the "Resources" folder
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# Read file
with open(input_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    header = next(reader)

    # Grab information in the original file and store them in lists
    for row in reader:
        emp_id.append(row[0])
        names.append(row[1])
        dob_ymd.append(row[2])
        ssn.append(row[3])
        states.append(row[4])

    # Split names
    for name in names:
        first_names.append(name.split(' ')[0])
        last_names.append(name.split(' ')[1])

    # Rearrange datetimes
    for i in dob_ymd:
        y = i.split('-')[0]
        m = i.split('-')[1]
        d = i.split('-')[2]
        dob_mdy.append(f'{m}/{d}/{y}')

    # Replace the first 5 digits of SSN with asterisks
    for i in ssn:
        last_four_digit = i[6:]
        ssn_hiden.append(f'***-**{last_four_digit}')

    # Convert state names to their abbreviations
    for state in states:
        if state in us_state_abbrev:
            states_abbrev.append(us_state_abbrev[state])

# Zip rearranged and new lists together to write rows later
new_data = zip(emp_id, first_names, last_names, dob_mdy, ssn_hiden, states_abbrev)

# In the output csv file, create a header and write the zipped object
with open(output_path, 'w', newline='') as output:
    writer = csv.writer(output)

    # Write the new header
    writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    writer.writerows(new_data)


    
