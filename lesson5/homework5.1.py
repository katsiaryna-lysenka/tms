dict_1 = {
  "key1": 3,
  "key2": 6,
  "key3": 9,
  "key4": 12,
  "key5": 15
}
dict_2 = {v: k for k, v in dict_1.items()}
print(dict_2)