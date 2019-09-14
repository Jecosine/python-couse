from PIL import Image, ImageFilter
import numpy
from matplotlib import pyplot as plt
im = Image.open("images/test.jpg")
contour = im.filter(ImageFilter.CONTOUR)
emboss = im.filter(ImageFilter.EMBOSS)
edged = im.filter(ImageFilter.FIND_EDGES)
figure = plt.figure(figsize=(10, 10))
# Show origin
ax1 = figure.add_subplot(221)
ax1.imshow(im)
plt.title("Origin")
plt.axis('off')

# Show contour
ax2 = figure.add_subplot(222)
ax2.imshow(contour)
plt.title("Contour")
plt.axis('off')

# Show emboss
ax3 = figure.add_subplot(223)
ax3.imshow(emboss)
plt.title("Emboss")
plt.axis('off')

# Show Edged
ax4 = figure.add_subplot(224)
ax4.imshow(edged)
plt.title("Edged")
plt.axis('off')

figure.show()
