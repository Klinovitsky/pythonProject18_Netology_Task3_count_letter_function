words_list = ["Xmas", "Xenomorph", "Reader", "Fool", "X-ray"]
print("Words in the list are: ", words_list)
letter: str = input("Input the letter to find: ")

def count_letter(words_list, letter):
  print("Function is started")
# Check the number of words
  for word in words_list:
    result = 0
# Check the letter in the word
    if letter in word:
        result = result + 1
    print(word, letter, result)
  # elif:
  #   print("??")

  return result

number = count_letter(words_list, letter)
print(f"The number of words with {letter} is: {number}")





