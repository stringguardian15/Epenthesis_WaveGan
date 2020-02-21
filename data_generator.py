word_endings = []
middle_vowels = []
initial_consonants = []
final_words = []
root_words = []
prefixed_words = []
output_file = 'words.out'

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

def epenthesize_initial_cons(cons):
    #if the initial cons should be epenthesized, return u+initial cons.
    epenthesized_set = {'r','l','w'}
    if cons in epenthesized_set:
        return u+cons
    else: return cons

# Build the roots
for we in word_endings:
    for mv in middle_vowels:
        for ic in initial_consonants:
            w = ic+mv+we
            root_words.append(w)

with open(output_file,'w') as fo:
    for word in root_words:
        fo.write(word+"\n")
