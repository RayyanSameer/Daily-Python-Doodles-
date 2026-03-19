import sys

def count_words(filename):
    word_counts = {}
    
    with open(filename, "r") as f:
        text = f.read()              # read the whole file

    words = text.split()         # split into a list of words
    
    for word in words:
        word = word.lower()      # normalize to lowercase
        word = word.strip(".,!?;:\"'")  # strip punctuation (given to you)
        
        if word == "":         # skip empty strings after stripping
            continue
            
        if word in word_counts:
            word_counts[word] += 1                # increment count
        else:
            word_counts[word] = 1                # initialize count

    return word_counts

def get_top_n(word_counts, n=10):
  
    sorted_words =sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

if __name__ == "__main__":
    if len(sys.argv) < 2:                          # check if filename was passed
        print("Usage: python freq.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1] 
    counts = count_words(filename)
    top_words = get_top_n(counts, 10)
    
    print(f"\nTop 10 words in '{filename}':\n")
    for word, count in top_words:
        print(f"  {word:<20} {count}")
    
   # left-aligned, clean formatting