from SpeechtoText import speechtotext
from CountWords import countwords

sentence, talking_time = speechtotext()
if not talking_time:
    print("no talking")
    exit()
words_count = countwords(sentence)
print("Words: {}".format(words_count))
print("talking_time: {}".format(talking_time))
wordspersecond = words_count / talking_time
print("Words Per Second: {}".format(wordspersecond))
if wordspersecond > 5:
    print("オタク早口やめろ")
    
