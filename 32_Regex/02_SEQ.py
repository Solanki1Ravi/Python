import re

a = "Harry Potter"

# match = re.search(r"\AHar",a)
#match = re.search(r"\APot",a) #Output --> None


# match = re.search(r"\bHar",a) # checking if the given expression is starts from the specified string or not.If not then it returns "None"
 
# match = re.search(r"ter\b",a) # checking if the given expression is ends from the specified string or not.If not then it returns "None"

# match = re.search(r"\Bter",a)
# match = re.search(r"Har\B",a)

e = "e32rARass90"
match = re.findall(r"\d",e) # It returns all the digits from the specified string 
match1 = re.findall(r"\D",e) # It returns all the characters from the specified string 
# print(match1)


s = " Ravi ndra singh sol anki "
match = re.findall(r"\s",s)
match1 = re.findall(r"\S",s)
# print(match)
# print(match1)

s = " Ravi ndra singh @ sol # ^& @ anki "
match = re.findall(r"\w",e)
match1 = re.findall(r"\W",s)
# print(match)
# print(match1)


z = 'ravi@gmail.com'

match1 = re.search(r".com\Z",z)
print(match1)
