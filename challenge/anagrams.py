# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. 
# Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should 
# return True while the call is_anagram("Alice", "Bob") should return False.
def is_anagram(word,word2):
    list1= sorted(word)
    list2= sorted(word2)
    if list1==list2:
        return True
    else:
        return False
print(is_anagram("Alice", "Bob"))

