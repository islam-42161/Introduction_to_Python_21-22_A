"""

Name: Islam, Md. Sazzadul
ID: 20-42161-1
code: Vowels frequency

"""
input_string = str(input("Chech frequency per vowel in string: "))
def getVowelFreq(input_string):
    frequencies = {}
    vowels = ['a','e','i','o','u']
    for char in input_string:
        if char.lower() in vowels:
           if char in frequencies: 
              frequencies[char] += 1
           else: 
              frequencies[char] = 1
    return str(frequencies)
print(f"Frequency per vowels in string '{input_string}': {getVowelFreq(input_string)}")
`
