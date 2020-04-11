from SpeechtoText import speechtotext
from CountWords import countwords
import PySimpleGUI as sg
import time
TIMEOUT = 60000  #ms

def measure_speed():
    sentence, talking_time = speechtotext()
    if talking_time:
        words_count = countwords(sentence)
        wordspersecond = words_count / talking_time
    else:
        words_count = 0
        wordspersecond = 0
        print("no talking")
    
    print("Words: {}".format(words_count))
    print("talking_time: {}".format(talking_time))
    print("Words Per Second: {}".format(wordspersecond))
    return wordspersecond

layout = [
    [sg.Text("スピードテスト",key="judge")],
]
window = sg.Window("Window Title", size=(600, 450)).Layout(layout)

while True:
    event, values = window.read(timeout=TIMEOUT, timeout_key="monitor")

    if event is None:
        break
    elif event=="monitor":
        wordpersecond=measure_speed()
        if wordpersecond>5:
            update_text = "{}文字/s\nオタク早口やめろ".format(wordpersecond)
        else:
            update_text = "{}文字/s\nいいじゃん".format(wordpersecond)
        window['judge'].update(update_text)

window.close()



    
