from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')