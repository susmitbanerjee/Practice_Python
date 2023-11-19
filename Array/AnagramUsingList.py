s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("first string is: ", s1)
print("second string is: ", s2)

list1 = list(s1)
list2 = list(s2)

if list1.sort() == list2.sort():
    print("Anagram")
else:
    print("Not Anagram")
