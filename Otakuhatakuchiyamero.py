from SpeechtoText import speechtotext
from CountWords import countwords

sentence, talking_time = speechtotext()
if not talking_time:
    print("no talking")
    exit()
words_count = countwords(sentence)
print(words_count)
wordspersecond = words_count / talking_time
print("Words Per Second: {}".format(wordspersecond))
    
