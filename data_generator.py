import re
word_endings = []
middle_vowels = []
initial_consonants = []
final_words = []
root_words = []
prefixes = []
output_file = 'words.out'

# a few function definitions
def get_initial_consonant_sound(word):
    m = re.match('([^aeiouAEIOU]*)([aeiou].*)',word)
    initial_sound = m.group(1)
    remaining_word = m.group(2)
    return (initial_sound,remaining_word)

def epenthesize_initial_sound(cons):
    #if the initial cons should be epenthesized, return u+initial cons.
    epenthesized_set = {'sh','s','f'}
    if cons in epenthesized_set:
        return 'u'+cons
    else: return cons

#load data
with open('word_endings.txt','r') as fi:
    for line in fi:
        line = line.strip()
        word_endings.append(line)
with open('middle_vowels.txt','r') as fi:
    for line in fi:
        line = line.strip()
        middle_vowels.append(line)
with open('initial_consonants.txt','r') as fi:
    for line in fi:
        line = line.strip()
        initial_consonants.append(line)
with open('prefixes.txt','r') as fi:
    for line in fi:
        line = line.strip()
        prefixes.append(line)


# Build the roots
for we in word_endings:
    for mv in middle_vowels:
        for ic in initial_consonants:
            w = ic+mv+we
            root_words.append(w)

# build the prefix compounds
compound_word_list = []
for pref in prefixes:
    for w in root_words:
        (initial_sound, remaining_word) = get_initial_consonant_sound(w)
        initial_sound_epenth = epenthesize_initial_sound(initial_sound)
        root_epenth = initial_sound_epenth + remaining_word
        compound_word = pref+root_epenth
        compound_word_list.append(compound_word)
final_words = root_words + compound_word_list




with open(output_file,'w') as fo:
    for word in final_words:
        fo.write(word+"\n")

