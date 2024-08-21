from PIL import Image, ImageDraw, ImageFont
import random

def LoadPannel():
    global base_image
    base_image = Image.open("Canvas.png")
    base_image = base_image.convert("RGBA")
    global rand
    global Row
    rand = 0
    Row = 0

def main():
    global pages
    global Clmn
    pages = 0
    Clmn = 0

def SingularPannel(Setting, Character, Bubble, i, InvertedCharacters):
    Box = (140, 160, 1780, 920)
    Pannel = Image.open(f"Backgrounds/{Setting}.png")
    Pannel = Pannel.crop(Box)
    if Character != "narrator":
        CharacterImg = Image.open(f"Characters/{Character}.png")
        CharacterImg = CharacterImg.convert("RGBA")
        Cwidth, Cheight = CharacterImg.size
        CharacterImg = CharacterImg.resize((int(Cwidth / 1.4), int(Cheight / 1.4)))
    BubbleImg = Image.open(f"BubblesTemp/{Bubble}")
    BubbleImg = BubbleImg.convert("RGBA")

    Bwidth, Bheight = BubbleImg.size
    BubbleImg = BubbleImg.resize((int(Bwidth / 1.5), int(Bheight / 1.5)))

    positionCharacter = (280, 0)  # Change to your desired position
    if Character in InvertedCharacters:
        positionBubble = (200, 0)
    else:
        positionBubble = (1050, 0)

    # Resize overlay image if needed
    if Character == "narrator":
        BubbleImg = BubbleImg.resize((600, 600))  # Adjust size as needed
        positionBubble = (200, 50)

    Pannel.paste(BubbleImg, positionBubble, BubbleImg)
    if Character != "narrator":
        # Paste the overlay image on the base image using the overlay's alpha channel as the mask
        Pannel.paste(CharacterImg, positionCharacter, CharacterImg)

    global Row
    if Row == 0:
        positionPannel = (30, 30)
        Row += 1
    elif Row == 1:
        positionPannel = (30, 820)
        Row += 1
    elif Row == 2:
        positionPannel = (30, 1610)
        Row += 1
        

    base_image.paste(Pannel, positionPannel, Pannel)
    Pannel.save(f"RawPannels/result_img {i}.png")
    global pages
    if Row == 3:
        base_image.save(f"Manga/Page {pages}.png")
        pages = pages + 1
        Row = 0
        LoadPannel()

def DoublePannel(Setting, Character, Bubble, i, InvertedCharacters):
    Box = (557.5, 160, 1362.5, 920)
    Pannel = Image.open(f"Backgrounds/{Setting}.png")
    Pannel = Pannel.crop(Box)
    if Character != "narrator":
        CharacterImg = Image.open(f"Characters/{Character}.png")
        CharacterImg = CharacterImg.convert("RGBA")
        Cwidth, Cheight = CharacterImg.size
        CharacterImg = CharacterImg.resize((int(Cwidth / 1.4), int(Cheight / 1.4)))
    BubbleImg = Image.open(f"BubblesTemp/{Bubble}")
    BubbleImg = BubbleImg.convert("RGBA")

    Bwidth, Bheight = BubbleImg.size
    BubbleImg = BubbleImg.resize((int(Bwidth / 1.8), int(Bheight / 1.8)))

    if Character in InvertedCharacters:
        positionBubble = (15, 0)
        positionCharacter = (-450, 0)
    else:
        positionBubble = (475, 50)
        positionCharacter = (-50, 0)

    # Resize overlay image if needed
    if Character == "narrator":
        #BubbleImg = BubbleImg.resize((750, 750))  # Adjust size as needed
        positionBubble = (50, 0)

    if Character != "narrator":
        # Paste the overlay image on the base image using the overlay's alpha channel as the mask
        Pannel.paste(CharacterImg, positionCharacter, CharacterImg)

    Pannel.paste(BubbleImg, positionBubble, BubbleImg)

    global Row
    global Clmn
    if Row == 0 and Clmn != 1:
        positionPannel = (30, 30)
        Clmn += 1
    elif Row == 1 and Clmn != 1:
        positionPannel = (30, 820)
        Clmn += 1
    elif Row == 2 and Clmn != 1:
        positionPannel = (30, 1610)
        Clmn += 1
    elif Row == 0 and Clmn == 1:
        positionPannel = (865, 30)
        Clmn = 0
        Row += 1
    elif Row == 1 and Clmn == 1:
        positionPannel = (865, 820)
        Clmn = 0
        Row += 1
    elif Row == 2 and Clmn == 1:
        positionPannel = (865, 1610)
        Clmn = 0
        Row += 1
        

    base_image.paste(Pannel, positionPannel, Pannel)
    Pannel.save(f"RawPannels/result_img {i}.png")
    global pages
    if Row == 3:
        base_image.save(f"Manga/Page {pages}.png")
        pages = pages + 1
        Row = 0
        LoadPannel()
    

def RandomPannel(Setting, Character, Bubble, i, InvertedCharacters):
    rand = random.randint(0, 2)
    if rand == 0 and Clmn == 0:
        SingularPannel(Setting, Character, Bubble, i, InvertedCharacters)
    else:
        DoublePannel(Setting, Character, Bubble, i, InvertedCharacters)

def lastSave():
    base_image.save(f"Manga/Page {pages}.png")
