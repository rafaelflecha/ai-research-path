text_block = """
The quick brown fox jumps over the lazy dog.
The dog, happy and quick, wags its tail.
Never underestimate the power of a quick fox.
"""

def find_most_frequent_word(text):
    normalized_text = text.lower().replace('.', '').replace(',', '')
    words = normalized_text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        
    if not word_counts:
        return None, 0
    
    most_frequent_word = max(word_counts, key=word_counts.get)
   
    # max_count = 0
    # most_frequent_word = ''
    # for word, count in word_counts.items():
    #     if count > max_count:
    #         max_count = count
    #         most_frequent_word = word
            
    return most_frequent_word, word_counts[most_frequent_word]

if __name__ == "__main__":
    word, count = find_most_frequent_word(text_block)
    
    print("Analysis Complete.")
    print(f"The most frequent word is '{word}' (appeared {count} times).)")
