# values = [1,2,"sai",6,7]
#List is a datatype that allows multiple values that can be different datatypes
# List is a mutable (can change)
# List will be declared with []

# print(type(values)) #<class 'list'>
# print(len(values)) #5
# print(values[0]) #1
# print(values[1]) #2
# print(values[2]) #sai
# print(values[3]) #6
# print(values[-1]) #7 (-1 will ive the last value in the list)
#
# values.insert(3,"Ram") #we can insert value in between the list
# print(values) #[1, 2, 'sai', 'Ram', 6, 7]
#
# values.append("End") #append is used to add the value to the list
# print(values) #[1, 2, 'sai', 'Ram', 6, 7, 'End']
#
# values[2] = "SAI" #it is used to update the list
# print(values)
#
# del values[6] #it is used to delete the value from the list
# print(values)


#Tuples

#Tuple is a type of data type that allows multiple values that can be different datatypes
#Tuple is a Immutable (cannot change)
#Tuple will be declared with ()
#Tuple is same as list
values = (1,2,"sai",4)
print(type(values))



#Dictionary it will be declared as a Key:value pair
dic={'a':2, 1:'Sai'}
print(type(dic))
print(dic)

dict={}
print(dict)
dict["firstname"]="Sai"
dict["lastname"]="Ram"
print(dict)
print(dict["lastname"])