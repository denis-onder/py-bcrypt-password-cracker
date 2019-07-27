import json
import bcrypt

with open('dictionary.json', 'r') as f:
  dictionary = json.load(f)

input_hash = input('Hash: ')

for i in range(0, len(dictionary)):
  if bcrypt.checkpw(dictionary[i].encode(), input_hash.encode()):
    print('Match found: {}'.format(dictionary[i]))
    break
  else:
    print('Not matching: {}'.format(dictionary[i]))
