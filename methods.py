user_input = input("Enter employee name: ")
employ_list = user_input.split( )
print('List : ',employ_list)

emp_tuple = tuple(employ_list)
print("Tuple: ", emp_tuple)

emp_ids=[101,102,103,104,105]
emp_dict = dict(zip(emp_ids,employ_list))
print(emp_dict)