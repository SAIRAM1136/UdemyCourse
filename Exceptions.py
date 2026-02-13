# ItemsInCart = 0
#
# if ItemsInCart !=2:
#     #raise Exception("ItemsInCart must be 2")
#     pass
#
# assert(ItemsInCart == 0)


#TRY, Except

person = ("Rahul", 25, 5.9)
print(person[1])

try:
    person[0] = "Sai"

except Exception as e:
    print(e)


