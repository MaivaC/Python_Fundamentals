#Returns number of vowels in a string

def count_vowels(word):
    vowels ="aeiouAEIOU"
    count= sum(1 for char in word if char in  vowels)
    return count
print(count_vowels("Amphibian"))
     

