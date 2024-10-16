

import re 

name = "Ravindar Singh Solanki"
# match = re.findall('[ngh]',name)
# print(match)

match = re.findall('[a-z]',name)
match1 = re.findall('[A-Z]',name)
# print(match)
# print(match1)

match  =re.findall('[^an]',name)
match1  =re.findall('[an]',name)
# print(match)
# print(match1)


num_str = "uier949834sjksj0984909fosdjf90834w9083jf"
match = re.findall('[345]',num_str)
# print(match)


match = re.findall('[0-9]',num_str)
# print(match)


match = re.findall('[0-7][0-9]',num_str)
# print(match)


match =re.findall('[a-zA-Z]',num_str)
print(match)
