

# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 


mylis = [45,84,88,3,56,95,781,84,222222,2020212]


MyNewList = list(filter(lambda x:x%2==0,mylis))

print(MyNewList)