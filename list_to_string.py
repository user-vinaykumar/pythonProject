courses = ['Math', 'Polity', 'Socials', 'Science', 'Biology']

# converting the above list to string

courses_str = ', '.join(courses)

print(courses_str)

courses2 = ['vinay', 'sharan', 'rajeshwari', 'shivalingaiah']
courses2_str = ' - '.join(courses2)
print(courses2_str)

n = courses2_str.split(' - ')
print(n)