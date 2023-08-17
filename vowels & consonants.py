def count_characters(text):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    
    vowel_count = 0
    consonant_count = 0
    uppercase_count = 0
    lowercase_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        if char.isupper():
            uppercase_count += 1
        if char.islower():
            lowercase_count += 1
    
    return vowel_count, consonant_count, uppercase_count, lowercase_count

file_path = "textFile.txt"

with open(file_path, 'r') as file:
    content = file.read()
    vowel_count, consonant_count, uppercase_count, lowercase_count = count_characters(content)
    
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
    print("Number of uppercase characters:", uppercase_count)
    print("Number of lowercase characters:", lowercase_count)
