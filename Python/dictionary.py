import json
## 
# difflib - library that can be used to get similiar deltas.
from difflib import get_close_matches

with open('data.json') as data_file:    
    data = json.load(data_file)

def translate(word):
    word = word.lower()
    
    # paris
    if word in data:
        return data[word]
    # Paris
    elif word.title() in data:
        return data[word.title()]
    # PARIS
    elif word.upper() in data:
        return data[word.upper()]
    # parsi
    elif len(get_close_matches(word=word, possibilities=data.keys(), n=3, cutoff=.62)) > 0:
        suggestions = get_close_matches(word, data.keys())
        max_suggestions = int(len(suggestions))
        suggestion_limit = 0

        print("\nSuggestions %s." % suggestions, '\n')

        while True:
            try:    
                retry = input("\n\nDid you mean %s instead? Enter Y if yes, or N if no: " % suggestions[suggestion_limit])
                retry = retry.upper()

                suggestion_limit = suggestion_limit + 1

                if max_suggestions <= suggestion_limit:
                    print("\nThe word doesn't exist. Please double check it.")
                    break

                if retry == 'Y':
                    print("\nDefinition for '%s' is: %s" %(word, data[suggestions[suggestion_limit]]))
                    break

            except ValueError:
                print('\nPlease input "Y" or "N": ')
                continue
            except:
                print('\nUnknown input.')
    # prasi
    else:
        return "Please double check; word appears to not exist."



word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


