# Question: Given an array of strings, return all groups of strings that are anagrams.

def anagrams(strs):
    # Create a dictionary to store the anagrams
    anagrams = {}
    # Iterate through the list of strings
    for word in strs:
        # Sort the string
        sorted_word = ''.join(sorted(word))
        # If the sorted string is in the dictionary, append the word to the list
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        # Otherwise, create a new key and value pair
        else:
            anagrams[sorted_word] = [word]
    return anagrams

print([i for i in anagrams(['cat', 'dog', 'god', 'tac']).values()])