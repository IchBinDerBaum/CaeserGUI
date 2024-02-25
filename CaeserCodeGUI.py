from tkinter import *
from tkinter import ttk

route = Tk()
route.geometry("1280x600")
route.title("Caeser Coder")
route.resizable(False, False)
mode = IntVar()
mode.set(1)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
maxkey = len(alphabet)

TranslatedMessage = ""

def copy():
    route.clipboard_clear()
    route.clipboard_append(Translation["text"])

def clearList():
    crackTranslation.delete(0, END)

def clearText():
    IncomingMessage.delete(1.0, END)

def enter():
    global message
    key1 = key.get()
    if mode.get() == 2 or mode.get() == 3:
        key1 = -key1
    message = IncomingMessage.get(1.0, END)
    TranslatedMessage = ""
    for i in message:
        if i not in alphabet:
            TranslatedMessage += i
        else:
            symbolindex = alphabet.find(i)
            symbolindex += key1
            if symbolindex >= len(alphabet):
                symbolindex -= len(alphabet)
            elif symbolindex < 0:
                symbolindex += len(alphabet)
            TranslatedMessage += alphabet[symbolindex]
    Translation.configure(text = TranslatedMessage)
    if mode.get() == 3:
        crack()
def crack():
    message = IncomingMessage.get(1.0, END)
    translatedlist = []
    for key1 in range(1, maxkey + 1):
        TranslatedMessage = ""
        for h in message:
            if h not in alphabet:
                TranslatedMessage += h
            else:
                symbolindex = alphabet.find(h)
                symbolindex -= key1
                if symbolindex >= len(alphabet):
                    symbolindex -= len(alphabet)
                elif symbolindex < 0:
                    symbolindex += len(alphabet)
                TranslatedMessage += alphabet[symbolindex]
        string = f"{key1}: {TranslatedMessage}"
        translatedlist.append(string)
    for i in translatedlist:
        crackTranslation.insert(END, i)

codeButton = Radiobutton(route, text="Code", variable=mode, value=1)
codeButton.place(x=200, y=200)
decodeButton = Radiobutton(route, text="Decode", variable=mode, value=2)
decodeButton.place(x=200, y=230)
crackButton = Radiobutton(route, text="Crack", variable=mode, value=3)
crackButton.place(x=200, y=260)

def getkey():
    keyslist = list(range(1, maxkey+1))
    return keyslist
Intro = Label(route, text="Choose your mode and key and type in your text. After that press 'Start'", font=(None, 15))
Intro.place(x=200, y=100)

Translation = Label(route, text="Click 'Start' to see your translation")
Translation.place(x=300, y=400)

crackTranslation = Listbox(route, height=18, width=60)
crackTranslation.place(x=800, y=200)

IncomingMessage = Text(route, height=10, width=50)
IncomingMessage.place(x=300, y=200)

startButton = Button(route, text="Start", command = enter)
startButton.place(x=200, y=290)

copyButton = Button(route, text="Copy", command=copy)
copyButton.place(x=300, y=430)

clearButtonList = Button(route, text = "Clear", command=clearList)
clearButtonList.place(x = 800, y = 155)

clearButtonText = Button(route, text = "Clear", command=clearText)
clearButtonText.place(x=350, y=430)

key = IntVar()
keys = ttk.Combobox(route, textvariable = key, value = getkey())
keys.place(x=300, y=150)



route.mainloop()