from PIL import Image, ImageDraw, ImageFont
import MangaPannels

def wrap_text(text, font, max_words_per_line=2):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if len(word) <= 8:
            current_line.append(word)
            if len(current_line) == max_words_per_line:
                lines.append(" ".join(current_line))
                current_line = []
        else:
            lines.append(" ".join(current_line))
            current_line = []
            lines.append("".join(word))
    
    if current_line:
        lines.append(" ".join(current_line))
    
    return lines

def BubbleOfSpeech(text, i, Character, Setting, InvertedCharacters):
    # Choose the correct bubble image
    if Character == "[narrator]":
        bubble_path = "NarratorBubble.png"
        TextSize = 35
    else:
        bubble_path = "Bubble.png"
        TextSize = 40
    
    # Load bubble image
    Bubble = Image.open(bubble_path)
    draw = ImageDraw.Draw(Bubble)
    
    # Load font
    try:
        font = ImageFont.truetype("mangatb.ttf", TextSize)  # Adjust size as needed
    except IOError:
        print("Font file not found. Falling back to default font.")
        font = ImageFont.load_default()  # Fallback to default font
    
    # Wrap text
    lines = wrap_text(text, font)
    
    # Calculate text positioning
    bubble_width, bubble_height = Bubble.size
    margin = 10  # Margin from the edges of the bubble

    # Calculate total text height
    total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines) + (len(lines) - 1) * 5  # Adding space between lines
    y = (bubble_height - total_text_height) / 2  # Start position for Y

    # Draw each line of text
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (bubble_width - text_width) / 2  # Center text horizontally
        draw.text((x, y), line, font=font, fill=(0, 0, 0))  # Black color text
        y += text_height + 5  # Move Y position for the next line (with space between lines)

    # Save the result
    Bubble.save(f"BubblesTemp/BubbleOf{i}.png")
    MangaPannel(Setting, Character, f"BubbleOf{i}.png", i, InvertedCharacters)

def MangaPannel(Setting, Character, Bubble, i, InvertedCharactersString):
    Setting = Setting[1:-1]
    InvertedCharacters = InvertedCharactersString.split()

    # Load the base image
    base_image = Image.open(f"Backgrounds/{Setting}.png")  # Replace with your base image path

    # Convert base image to RGBA (if it's not already in that mode)
    base_image = base_image.convert("RGBA")

    Character = Character[1:-1]
    # Load the overlay image
    if Character != "narrator":
        Character_image = Image.open(f"Characters/{Character}.png")  # Replace with your overlay image path

        # Convert overlay image to RGBA (if it's not already in that mode)
        Character_image = Character_image.convert("RGBA")

    # Load the overlay image
    Bubble_image = Image.open(f"BubblesTemp/{Bubble}")  # Replace with your overlay image path

    # Convert overlay image to RGBA (if it's not already in that mode)
    Bubble_image = Bubble_image.convert("RGBA")

    # Position where you want to paste the overlay image
    positionCharacter = (0, 0)  # Change to your desired position
    if Character in InvertedCharacters:
        positionBubble = (200, 0)
    else:
        positionBubble = (1050, 0)

    # Resize overlay image if needed
    if Character == "narrator":
        Bubble_image = Bubble_image.resize((600, 600))  # Adjust size as needed
        positionBubble = (200, 0)

    base_image.paste(Bubble_image, positionBubble, Bubble_image)
    if Character != "narrator":
        # Paste the overlay image on the base image using the overlay's alpha channel as the mask
        base_image.paste(Character_image, positionCharacter, Character_image)
    # Save the result
    base_image.save(f"BeautifulPannels/result_image {i}.png")  # Save as PNG to preserve transparency if needed

    MangaPannels.RandomPannel(Setting, Character, Bubble, i, InvertedCharacters)