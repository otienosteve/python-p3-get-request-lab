from lib.employee import session, Employee


employees = []
data = [
    {
'id': 1,
'first_name': 'Pete',
'last_name': 'Jacke',
'email': 'pjacke0@ftc.gov',
'age': 44,
'gender': 'Male',
'phone_number': 4165929356,
'salary': 179681,
'designation': 'Supervisor'
},
{
'id': 2,
'first_name': 'Judah',
'last_name': 'Scolland',
'email': 'jscolland1@seattletimes.com',
'age': 53,
'gender': 'Male',
'phone_number': 6016570479,
'salary': 93098,
'designation': 'Surveyor'
},
{
'id': 3,
'first_name': 'Lucille',
'last_name': 'Oulett',
'email': 'loulett2@jigsy.com',
'age': 54,
'gender': 'Female',
'phone_number': 6469701273,
'salary': 121396,
'designation': 'Surveyor'
},
{
'id': 4,
'first_name': 'Kathy',
'last_name': 'Truswell',
'email': 'ktruswell3@storify.com',
'age': 42,
'gender': 'Female',
'phone_number': 4971711123,
'salary': 221547,
'designation': 'Construction Manager'
},
{
'id': 5,
'first_name': 'Ernesta',
'last_name': 'Getcliff',
'email': 'egetcliff4@ed.gov',
'age': 25,
'gender': 'Female',
'phone_number': 6925639593,
'salary': 226831,
'designation': 'Subcontractor'
},
{
'id': 6,
'first_name': 'Otha',
'last_name': 'Stollsteimer',
'email': 'ostollsteimer5@ed.gov',
'age': 25,
'gender': 'Female',
'phone_number': 8537571074,
'salary': 40226,
'designation': 'Supervisor'
},
{
'id': 7,
'first_name': 'Arvie',
'last_name': 'Escalante',
'email': 'aescalante6@squidoo.com',
'age': 39,
'gender': 'Male',
'phone_number': 1711391327,
'salary': 64493,
'designation': 'Subcontractor'
}
]

for item in data:
    emp = Employee(**item)
    employees.append(emp)

session.bulk_save_objects(employees)
session.commit()