#Converting tuple to a list

my_tuple= ("bread", "chocolate", "butter", "eggs", "milk")

my_list= list(my_tuple)    #converts tuple to a list

my_list.insert(0, "airfryer")    #inserts the new air element at the first  position 

new_tuple=tuple(my_list)  #Converts the list back to  a tuple

print(my_tuple)
print(my_list)
print(new_tuple)
