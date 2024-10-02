

myName = "Ravindra Singh";

# len():- returns the length of a string

print(len(myName))

# upper():- converts a string to upperCase()
print(myName.upper())

# lower():- converts a string to lowerCase()
print(myName.lower())

# strip():- remove any white spaces before and after the string 
myName = "     Ravindra Singh    ";
print(len(myName))
print(len(myName.strip()))


# rstrip():- removes any trailing characters. it only removes the trailing charachters that are present in the right side of the string

myName = "!!!!!!!Ravindra Singh!!!!";
print(myName.rstrip("!"))


# replace():= replaces all occurances of a string with another string

myName = "Ravindra Singh";
print(myName.replace("Singh","Solanki"))


# split():- split the given string at the specified instance and returns the separeted string as list items 

myName = "Ravindra Singh Solanki";
print(myName.split(" "))


# capitalize():- it turns the first character of the string to uppercase and the rest orher characters of the string are turned to lowercase. The String has no effect if the first character is already uppercase

myName = "ravindra siNgh Solanki";
print(myName.capitalize())

# center():- it aligns the string to the center as per the parameters given by the user
myName = "Ravindra Singh Solanki";
print(len(myName))
# print(myName.center(30))


# count():- returns the number of times the given value has occured while the given string

myName = "Ravindra Singh Solanki";
print(myName.count('i'))



# endswith():- check if the string ends with a given value. if yes then returns True else returns false

# we can check for a value in-between the string by providing start and end index positions



myName = "Ravindra Singh Solanki";
print(myName.endswith("Ravu"))
print(myName.endswith(" ",4,15))

# startwith():- check if the string Starts with a given value. if yes then returns True else returns false

myName = "Ravindra Singh Solanki";
print(myName.startswith("rav"))


# find():- searches for the first occurances of the given value and returns the index where it is present. if given value is absent from the string then returns -1
myName = "Ravindra Singh Solanki";
print(myName.find("rav"))
print(myName.find("ndra"))


# index():- searches for the first occurances of the given value and returns the index where it is present. if given value is absent from the string then raise an exception.


myName = "Ravindra Singh Solanki";
# print(myName.index("rav")) # return error
print(myName.index("ndra"))


# isalnum():- it returns True only if the entire string only consists of A-Z, a-z, 0-9 . If any other characters of punctuations are present, then it returns False


myName = "RavindraSingh@Solanki";
print(myName.isalnum())
myName = "RavindraSinghSolanki";
print(myName.isalnum())
myName = "Ravindra Singh Solanki 1";
print(myName.isalnum())
myName = "Ravindra Singh Solanki";
print(myName.isalnum())


# isalpha():- it returns True only if entire string only consists of A-z a-z . If any other characters or punctuations or numbers(0-9) are present it returns error

myName = "RavindraSinghSolanki";
print(myName.isalpha())


#  islower():- it returns True if all the characters in the string are lowercase , else it returns false

myName = "Ravindra Singh Solanki";
print(myName.islower())
myName = "ravindra singh solanki";
print(myName.islower())


# isspace():- it returns true only and only if the string contains white spaces , else returns false

myName = "       ";
print(myName.isspace())
myName = "      s ";
print(myName.isspace())


# istitle():- it returns True only if the first letter of each word of the string is capitalized, else it returns false

myName = "Ravindra Singh Solanki";
print(myName.istitle())
myName = "ravindra singh solanki";
print(myName.istitle())


# swapcase():- it changes casing of the string . upper case are converted to lower and lower case to upper case

myName = "ravindra singh solanki";
print(myName.swapcase())
myName = "RAVINDRA SINGH SOLANKI"
print(myName.swapcase())


# title():- capitalizes each letter of the word within the string
myName = "ravindra singh solanki";
print(myName.title())

