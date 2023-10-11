from PIL import Image

image = Image.open(r"maps\4.png")
image = image.convert('RGB')
width, height = image.size

output = open('output.txt', 'w', encoding='utf-8')
for y in range(width):
    for x in range(height):
        pix = image.getpixel((x,y))
        b = "".join(['1' if x else '0' for x in pix])
        b = chr(int('C' + b, 16))
        output.write(b)
output.close()