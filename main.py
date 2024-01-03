from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")
print("Выберите картинку")
memes =["cat_with_glasses.png" , "Кот в ресторане.png" , "notsmile.jpg" , "person.jpg", "the_cat_is_in_shock.jpg", "tiredowl.png"]
for i in range(len(memes)):
    print(f"{i} - {memes[i]}")
image = Image.open(memes[int(input("Выберите картинку "))])
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=70)

text_type = int(input("Введите 1, если нужен только нижний текст,2 если верхний и нижний "))
if text_type == 1:
    bottom_text = input("Введите нижний текст: ")
    lower_text = draw.textbbox(((0,0) ), bottom_text, font)
elif text_type == 2:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
    upper_text = draw.textbbox((0, 0), top_text, font)
    lower_text = draw.textbbox((0, 0), bottom_text, font)
else:
    print("Введен неправильный режим. Перезапустите программу.")
    quit()

if text_type == 1:
    draw.text(((width - lower_text[2]) / 2, (height - lower_text[3]) - 10), bottom_text, font=font, fill="black")
elif text_type == 2:
    draw.text(((width - upper_text[2]) / 2, 10), top_text, font=font, fill="black")  # координаты x,y
    draw.text(((width - lower_text[2]) / 2, (height - lower_text[3]) - 10), bottom_text, font=font, fill="black")

image.save("new_meme.jpg")