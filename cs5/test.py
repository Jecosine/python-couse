import random
def jumble(word):
    jb = ''
    while len(word) > 1:
        i = random.randrange(len(word))
        jb += word[i]
        word = word[:i] + word[i+1:] if (i + 1 > len(word)) else '' 