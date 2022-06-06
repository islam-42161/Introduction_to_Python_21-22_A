"""

Name: Islam, Md. Sazzadul
ID: 20-42161-1
code: Character frequency

"""
input_string = str(input("Chech frequency per character in string: "))

def getCharFreq(input_string):
   frequencies = {} 
     
   for char in input_string: 
      if char in frequencies: 
         frequencies[char] += 1
      else: 
         frequencies[char] = 1
   return str(frequencies)

print(f"Frequency per char in string '{input_string}': {getCharFreq(input_string)}")
