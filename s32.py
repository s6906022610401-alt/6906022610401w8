num_e = int(input( 'how many employee records do you want to create?'))
with open('employee.txt','w') as emp_file:
    for count in range(1,num_e +1):
        print('enter data for employee #',count,sep ='')
        name = input('name: ')
        id_n = input('ID number: ')
        dept = input('department: ')

        emp_file.write('Name :'+name + '\n')
        emp_file.write('ID :'+id_n + '\n')
        emp_file.write('Dept :'+dept + '\n')

        print()
print('employee records written to employee.txt. ')