#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

two_word_string_list = []




def begin_with_same_letter(two_word_string_list):
    word1 = [two_word_string_list[0]]
    word2 = [two_word_string_list[1]]
    
    if word1 == word2:
        print("They start with same letter!")
    else:
        print("They do not start with same letter ")

two_word_string = str(input("Enter two words : "))
two_word_string_list = two_word_string.split(" ")
print(two_word_string_list)        

if len(two_word_string_list) != 2:
    print("TWO words only!")
else:
    begin_with_same_letter(two_word_string_list)




        