'''
1. A Regular Expression is a special sequence of characters that uses a search pattern to find a string or set of strings

2. It can detect the presence or absence of a text by matching it with a particular pattern, and also can split a pattern into one or more sub patterns 



'''

import re 


email = "rajne.sha422a31@gmaail.com"
b = "charlie chaplie  chach and the choacolate factory"

# match = re.search(r"\.",email)
# match = re.findall(r"\.",email)
# match = re.findall(r"[a]",email)
# match = re.search(r"[a]",email)

# match = re.search(r"^ra",email)
# match = re.search(r"^as",email) # output:- None

# match = re.search(r".com$",email)
# match = re.search(r"ucom$",email) # output:- None


# match = re.findall(r"c.a",b)
# match = re.findall(r"c..a",b)



# match = re.findall(r"cha|fac",b)
# match = re.findall(r"cha|ory",b)


# match = re.findall(r"ch?a",b)
# match = re.findall(r"ch*a",b)

d = 'XYZ,YZ,XXYYZZ,XZY,ZYZ,XXYYYYYZZZ'

# match = re.findall(r"XY+Z",d)

# match = re.findall(r"X{2,4}",d)
# match = re.findall(r"Y{2,4}",d)


match = re.findall(r"(X|Y)YZ",d)

print(match)




