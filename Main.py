import re
import MangaPannel
import StoryWriter
import MangaPannels

def Main(callback, UpdateText, Theme, AIinput, InvertedCharacters, CharactersImgName):
    import os

    def delete_all_files(folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)

    folder_path = 'Manga'
    delete_all_files(folder_path)


    MangaPannels.LoadPannel()
    MangaPannels.main()

    Characters = CharactersImgName.split()
    
    Settings = ["[Car]", "[Classroom]", "[JschlattRoom]", "[Park]", "[SchoolHallway]", "[SchoolRooftop]", "[ShopInside]", "[ShopOutside]"]

    Text = StoryWriter.Writer(Theme, AIinput)

    line = Text.splitlines()
    lines = []

    for i in line:
        if i != '':
            lines.append(i)
    t = 0
    for i in lines:
        for j in Settings:
            if j in i:
                Setting = j

                UpdateText(j)
        for j in Characters:
            if j in i:
                Character = j

                UpdateText(j)

        pattern = r'\((.*?)\)'
        match = re.search(pattern, i)
        if match:

            UpdateText(match.group(1))
            MangaPannel.BubbleOfSpeech(match.group(1), t, Character, Setting, InvertedCharacters)
            t += 1
    
    MangaPannels.lastSave()
    callback()