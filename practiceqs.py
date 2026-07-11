sentence = str(input('Enter your sentence: '))
letters = []
count = 0
for letterr in sentence:
  count = 0
  if letterr in letters:
    continue
  else:
    letters.append(letterr)
  for letter in sentence:
    if letter == letterr:
      count = count + 1
  print(count)