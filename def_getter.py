from PyDictionary import PyDictionary
dictionary = PyDictionary()

words_list_path = r'lit_terms.txt'

start = 0
i = 0

words = []

f = open(words_list_path, 'r')
Lines = f.readlines()

Lines_l = len(Lines) - 1

f = open('defs.txt', 'w')
words_not_found = []


for i in range(1, len(Lines)+1):
    
    print("Getting defintion for word: {}".format(Lines[i-1]))
    
    definition = dictionary.meaning(Lines[i-1])

    try:
        print("Definition found for; writing definition for", Lines[i-1])
        writeDef = str(list(definition.values()))
        f.write("\nWord: {} & Def: {}\n".format(Lines[i-1], writeDef))
    except AttributeError:
        print("Could not find a definition for {}".format(Lines[i-1]))
        words_not_found.append(Lines[i-1])

print("Words not found: {}".format(words_not_found))

    

