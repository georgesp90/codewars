def spin_words(sentence):
    def spin(word):
        if len(word) >= 5:
            return reduce(lambda x,y: x + y, reversed(word), "")
        else:
            return word
    return ' '.join(map(spin, sentence.split()))

 # mine

 def spin_words_b(sentence):
    for word in sentence.split():
      if len(str(word)) >= 5:
        word = [word[::-1] for word in sentence.split()]
        word = ''.join(word)
      else:
        word = sentence
    print(word)
    return (word)

# way better 
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])