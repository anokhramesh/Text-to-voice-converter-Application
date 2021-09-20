from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
import pyttsx3

root=Tk()
root.title("Text to Voice Converter App")#title of the Application
root.iconbitmap('python_icon1.ico')#icon of the Application
root.geometry('355x370')# Application window size
root.configure(bg='#f08c0a')#Application backgroud color
info_label=Label(root,bg='#07fa48',fg='black',text="Enter your Text below",font=("Georgia 16 bold"))
info_label.grid(row=0,columnspan=3,pady=5)
# Create a function for text to speech
def speak():
    engine=pyttsx3.init()
    audio_string=my_text.get('0.0',END)
    if audio_string:
        engine.setProperty('rate',125)# Speech speed
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)# female voice
        #engine.setProperty('voice', voices[0].id)# male voice
        engine.say(audio_string)
        engine.runAndWait()
        engine.stop()

# Create a function for save text to mp3 audio
def save():
    engine=pyttsx3.init()
    audio_string=my_text.get('0.0',END)
    if audio_string:
        engine.setProperty('rate', 125)  # Speech speed
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # female voice
        # engine.setProperty('voice', voices[0].id)# male voice
        engine.save_to_file(audio_string,'sound.mp3')# Converted audio file name
        engine.runAndWait()
        engine.stop()
        #Create a label to show the result
        result_label=Label(root,fg='red',bg='blue',font=("arial 12 bold"),text="file Saved as sound.mp3")
        result_label.grid(row=3,columnspan=3,pady=4)

my_text=ScrolledText(root,fg='green',bg='white',font=("arial 12 bold"),width=30,height=10,wrap=WORD,padx=10,pady=10,bd=5,relief=RIDGE)
my_text.grid(row=1,columnspan=3,pady=5)

#create a button for speak the text you entered on the scrolltext area
speak_button=Button(root,fg='blue',bg='red',text=" Speech",font=("arial 12 bold"),command=speak)
speak_button.grid(row=2,column=0,padx=5,pady=10)

#Create a button for Clear the text you entered on the scrolltext area
clear_button=Button(root,fg='blue',bg='red',text="Clear text",font=("arial 12 bold"),command=lambda :my_text.delete('0.0',END))
clear_button.grid(row=2,column=1,padx=5,pady=10)

#Create a button for Convert the text to mp3 and Save
save_button=Button(root,fg='blue',bg='red',text="Convert and save",font=("arial 12 bold"),command=save)
save_button.grid(row=2,column=2,padx=5,pady=10)

root.mainloop()