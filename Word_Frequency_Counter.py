#Counts the number of times a word appears

def count_elements(elements):
    if elements[-1] == '.':
        elements = elements[0:len(elements) -1]

    if elements in dictionary :
        dictionary[elements] += 1

    else:
        dictionary.update({elements: 1})

Sentence = input("Enter statement ")

dictionary = {}

lst = Sentence.split()

for elements in list:
    count_elements(elements)

for allKeys in dictionary:
    print("Frequency : ", allKeys, end='')
    print(":", end=' ')
    print(dictionary[allKeys], end='')
    print()  
        

