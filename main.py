words_list = ["Xmas", "Xenomorph", "Reader", "Fool", "Xor", "Xenon"]
print("Words in the list are: ", words_list)
#letter = "X"
letter: str = input("Input the letter to find: ")

def count_letter(words_list, letter):
  result = 0
  # Check the number of words
  for word in words_list:
    if letter in word:
      result += 1
      print("------------- LETTER cycle: ", word, letter, result)
  return result

number = count_letter(words_list, letter)
print(f"The number of words with {letter} is: {number}")

#print(count_letter(["Хmas", "Xenomorph", "Reader", "Fool", "X-ray"], "X"))
#test
