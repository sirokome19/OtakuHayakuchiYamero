from SpeechtoText import speechtotext
from CountWords import countwords
import PySimpleGUI as sg
import time
from PIL import Image, ImageTk
import io
TIMEOUT = 60000  #ms
GO = "./images/go.jpg"
SLOW="./images/slow.png"
STOP = "./images/stop.jpg"

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

def get_img_data(f, maxsize=(600, 450), first=False):
    """Generate image data using PIL
    """
    print("open file:", f)
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:  # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

filename = GO
layout = [
    [sg.Text("計測します",key="result")],
    [sg.Image(data=get_img_data(filename, first=True),key="judge")],
]
window = sg.Window("Window Title", size=(600, 450)).Layout(layout)

while True:
    event, values = window.read(timeout=TIMEOUT, timeout_key="monitor")

    if event is None:
        break
    elif event == "monitor":
        window['judge'].update(data=get_img_data("./images/sokutei.jpg", first=True))
        window.Finalize()
        wordpersecond=measure_speed()
        if wordpersecond < 5:
            filename=GO
            # update_text = "{}文字/s\nオタク早口やめろ".format(wordpersecond)
        elif wordpersecond < 8:
            filename=SLOW
        else:
            filename=STOP
            # update_text = "{}文字/s\nいいじゃん".format(wordpersecond)
        window['judge'].update(data=get_img_data(filename, first=True))
        window['result'].update("{}文字/s".format(wordpersecond))

window.close()



    
