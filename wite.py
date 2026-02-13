#read the file and store all the lines in the list
#reverse the list
# write the list to txt file

with open('text.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

