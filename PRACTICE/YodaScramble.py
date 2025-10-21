#MASTER YODA: Given a sentence, return a sentence with the words reversed


usersectence = str(input("Enter a sentence : "))


def masteryoda(userstring):
    words = userstring.split()
    reversed_words = words[:: -1]
    print(" ".join(reversed_words))
masteryoda(usersectence)
