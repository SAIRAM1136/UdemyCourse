str = "RahulShettyAcademy.com"
str1="course"
str2="RahulShetty"

print(str[1])
print(str[0:5]) #string slicing
print(str+" "+str1) #concatenation 2 strings
print(str2 in str) # substring check

a=str.split()
print(a)

#trim is used to remove the white spaces in the beggining and end
#method for trim is strip

str4 = "  SaiRam  "
print(str4.strip())
print(str4.lstrip())
