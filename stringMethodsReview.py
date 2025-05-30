highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')

highlighted_poems_stripped = []

for word in highlighted_poems_list:
  word_stripped = word.strip(' ')
  highlighted_poems_stripped.append(word_stripped)

highlighted_poems_details = []

for word in highlighted_poems_stripped:
  split_colon = word.split(':')
  highlighted_poems_details.append(split_colon)

print(highlighted_poems_details)

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

for i in range(0, len(titles)):
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))



