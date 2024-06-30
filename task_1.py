#list operations
my_list=[10,20,30,40,60]
my_list.append(50)
my_list.remove(40)
my_list[0]=80
print("Updated list:",my_list)

#Dictionary operations
my_dict={'name':'sai','age':19,'city':'hyd'}
my_dict['gender']='male'
del my_dict['city']
my_dict['name']='kumar'
print("updated dictionary:",my_dict)

#set operations
my_set={0,1,2,3,4}
my_set.add(5)
my_set.remove(2)
my_set.discard(2)
my_set.add(7)
print("updated set:",my_set)