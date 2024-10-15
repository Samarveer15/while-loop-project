word = input("enter your number")

count = 0
index = 0
while index < len(word):
    if word[index].isdigit():  
     count += 1
     index += 1
print( count)
    