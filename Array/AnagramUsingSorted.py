s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("first string is: ", s1)
print("second string is: ", s2)

choice = "default"
# reversing using the sorted method
rev1 = ''.join(sorted(s1))
rev2 = ''.join(sorted(s2))
while choice == "y" or choice == "Y":
    if rev1 == rev2:
        print("Anagram")
    else:
        print("Not Anagram")




