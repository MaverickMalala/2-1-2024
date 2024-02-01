def reverse_case_map_function(word):
  reversed_strings = list(map(str.swapcase, word))
  return reversed_strings

word = map(lambda a, b: a + b, ('blue', 'red', 'yellow'), ('green', 'orange', 'green'))
reversed_list = reverse_case_map_function(word)
for s in reversed_list:

    print(s)
