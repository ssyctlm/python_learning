def break_words(stuff):
    '''This function will brak up words for us.'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# additional
def even_more_concise_trim(s):
    if s:
        if s == ' '* len(s):
            return ''
        while s[0] == ' ':
            s = s[1:]
        while s[-1] == ' ':
            s = s[:-1]
        return s
    else:
        return s

words1 = ['All','good','things','come','to','those','who','wait']
print(words1)
sentence = ''
for i in words1:
    if sentence == '':
        sentence = sentence + i
    else:
        sentence = sentence + ' ' + i

print('**********************')
sentenceb = ''
for i in words1:
    sentenceb = sentenceb  + ' ' + i


print(sentenceb)
cut = -1
for i in sentenceb:
    cut += 1
    if i != ' ':
        continue
    else:
        sentenceb = sentenceb[1:]
        break
print(break_words(sentenceb))

print('**********************')

even_more_concise_trim(sentence)

print(sentence)

words = break_words(sentence)

print(words)

sorted_words = sort_words(words)
print(sorted_words)

print_first_word(words)
print_last_word(words)

print(words)

print_first_word(sorted_words)
print_last_word(sorted_words)

print(sorted_words)

sorted_words = sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
