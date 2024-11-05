#add() and update() demonstration, 
#Usind the add()
even_numbers={2,4,6,8,10,12,14,16,18,20}

odd_numbers={1,3,5,7,9}

my_new_set= even_numbers.copy()  #Helps preserve the original set

my_new_set.add(22)



print(my_new_set)
 


#Using the update(), uncomment then run


my_set=even_numbers.update(odd_numbers)
print(even_numbers)