import json, difflib
# How to get a ratio below --
# 	ratio = SequenceMatcher(None, str(keys), str(word)).ratio()
from difflib import SequenceMatcher # Need for similiarity ratio scores.
from difflib import get_close_matches # call help(get_close_matches) for ex.

# Load JSON data into data var.
data = json.load(open("data.json"))

closeMatches = []
word = input('Input word defintion search ("q" to exit): ')
word = word.lower()
#help(get_close_matches)

while(word != 'q'):
	if(word in data.keys()):
		print('\n\t\tDefinition of: ', str(word))
		index = 1
		for key in data[word]:
			print(str(index), '.', key)
			index+=1
		print('\n')
	else:
		# At most, return 6 match. Words must be at least a 75% match.
		#(word, words to check against, max return, match ratio)
		closeMatches = get_close_matches(word, data.keys(), n=6, cutoff=.75)
		print('\n\nClose matches')
		for keys in closeMatches:
			print(keys)
		print('\n')
		closeMatches[:] = []# Delete everything in list.


	word = input('Input word defintion search ("q" to exit): ')
	word = word.lower()