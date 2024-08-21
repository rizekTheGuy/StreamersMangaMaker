import tkinter as tk
from PIL import Image, ImageTk
import Main
import threading

def Read():
    global AIinput
    global CharactersImgName
    global InvertedCharacters

    with open("AIinput.txt", "r") as file:
        AIinput = file.read()
    with open("CharactersImgName.txt", "r") as file:
        CharactersImgName = file.read()
    with open("InvertedCharacters.txt", "r") as file:
        InvertedCharacters = file.read()
    
    global UpdatedAIinput
    UpdatedAIinput = AIinput.format(STATES=CharactersImgName)

Read()

def UpdateText(Text):
    label.config(text=Text)

def RunMain():
    Theme = entry.get()
    text_box = textbox.get("1.0", tk.END)
    text_box2 = textbox2.get("1.0", tk.END)
    text_box3 = textbox3.get("1.0", tk.END)

    with open("AIinput.txt", "w") as file:
        file.write(text_box)
    with open("CharactersImgName.txt", "w") as file:
        file.write(text_box3)
    with open("InvertedCharacters.txt", "w") as file:
        file.write(text_box2)

    Read()

    Main.Main(Finished, UpdateText, Theme, UpdatedAIinput, text_box2, text_box3)

# Create the main window
root = tk.Tk()
root.title("AI Streamer Manga")
root.iconbitmap('Icon.ico')

# Set the window size
root.geometry("600x600")
root.resizable(False, False)

options_hidden = False

# Load the background image
image_path = "Background.png"  # Replace with your image path
image = Image.open(image_path)
image = image.resize((600, 600))
background_image = ImageTk.PhotoImage(image)

# Create a label with the image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Define a function that will be called when the button is clicked
def on_button_click():
    global label
    button.config(text="Generating Please Wait...")
    label = tk.Label(root, text="")
    label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    button.config(state=tk.DISABLED)
    threading.Thread(target=RunMain).start()

def MoreOptions():
    global options_hidden
    if options_hidden:
        textbox.place(relx=0.5, rely=0.57, anchor=tk.CENTER)
        labelCIN.place(relx=0.5, rely=0.74, anchor=tk.CENTER)
        textbox3.place(relx=0.5, rely=0.79, anchor=tk.CENTER)
        labelIC.place(relx=0.5, rely=0.84, anchor=tk.CENTER)
        textbox2.place(relx=0.5, rely=0.89, anchor=tk.CENTER)
        button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
        
        button2.config(text="Less Options")
    else:
        textbox.place_forget()
        labelCIN.place_forget()
        textbox3.place_forget()
        labelIC.place_forget()
        textbox2.place_forget()
        button2.config(text="More Options")
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    options_hidden = not options_hidden
    
def Finished():
    button.config(state=tk.NORMAL)
    button.config(text="Start Generating")
    label.config(text="Finished Generating :D")

label = tk.Label(root, text="Write the Theme")
label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

textbox = tk.Text(root, height=10, width=60)
textbox.insert(tk.END, AIinput)
textbox.pack(pady=10)
textbox.place(relx=0.5, rely=0.57, anchor=tk.CENTER)

labelCIN = tk.Label(root, text="Characters Image Names")
labelCIN.place(relx=0.5, rely=0.74, anchor=tk.CENTER)

textbox3 = tk.Text(root, height=1, width=60)
textbox3.insert(tk.END, CharactersImgName)
textbox3.pack(pady=10)
textbox3.place(relx=0.5, rely=0.79, anchor=tk.CENTER)

labelIC = tk.Label(root, text="The Inverted Characters")
labelIC.place(relx=0.5, rely=0.84, anchor=tk.CENTER)

textbox2 = tk.Text(root, height=1, width=60)
textbox2.insert(tk.END, InvertedCharacters)
textbox2.pack(pady=10)
textbox2.place(relx=0.5, rely=0.89, anchor=tk.CENTER)

# Create a button widget
button = tk.Button(root, text="Start Generating", command=on_button_click)
button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

button2 = tk.Button(root, text="More Options", command=MoreOptions)
button2.place(relx=0.9, rely=0.15, anchor=tk.CENTER)

MoreOptions()

# Start the Tkinter event loop
root.mainloop()