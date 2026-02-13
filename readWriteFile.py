file = open('text.txt')
print(file.read(3)) # which is used to read all the contents in the txt file
# #read 1 single line at a time
print(file.readline())
file.close()

#Interview question: print line by line using readline()
#readline: it is use to get the data from the txt and show as it is
#readlines: It is used to get data from the """LIST"""

line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()




