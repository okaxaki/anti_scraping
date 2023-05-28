from PIL import Image
import random

img = Image.open('input.jpg')
w, h = img.size

print('<!DOCTYPE html><html><head><link rel="stylesheet" href="index.css"></head>')
print('<body><div class="obfuscated-image">')
print('<img src="output.png">')

lines=[]
for x in range(w):
    line=[]
    for y in range(h):
        if random.random() > 0.9:
            r,g,b = img.getpixel((y,x))
            color = 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')';
            line.append('<div style="background-color:' + color + '"></div>')
            img.putpixel((y,x), (0,255,0))
        else:
            line.append('<div></div>')
    lines.append(''.join(line))

print('<div class="obfuscated-layer">')
print('\n'.join(lines))
print('</div>')

print('</div></body>')
print('</html>')

img.save('output.png')