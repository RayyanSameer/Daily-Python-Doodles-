#Log analysis is a daily DevOps task. NLP preprocessing starts with word frequency. Backend data processing pipelines do this at scale. This one script touches all three tracks.

#A program that reads any .txt file, counts how often each word appears, and prints the top 10 words with their counts.

#it's a modular program that works by taking a file , reading it and pushing all text into a variable text , then splitting text into words and normalizing them before counting them in the word_counts variable 

def count_words(filename):
    count_words = {} #dict store for key and value pair 

    with open(filename,"r") as f:
        #open file in readmode as f 
        text = f.read()
    words = text.split()

    for word in words:
        #normalize 
        word = word.lower()
        if word in count_words :
            count_words[word] += 1
        else:
            count_words[word] = 1
    return count_words                
if __name__ == "__main__":
    counts = count_words("sample.txt")
    print(counts)