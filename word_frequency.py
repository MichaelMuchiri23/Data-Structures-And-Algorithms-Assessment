def word_frequency(sentence):
    list = sentence.split()
    dictionary = {}

    for word in list:
        dictionary[f"{word}"] = list.count(word)
    return dictionary

print(word_frequency("Hello. I was wondering whether I can play."))        