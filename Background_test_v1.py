import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def crop_to_square(image):
    width, height = image.size
    if width > height:
        # Crop left & right to make it square
        left = (width - height) // 2
        right = left + height
        image = image.crop((left, 0, right, height))
    elif height > width:
        # Crop top & bottom to make it square
        top = (height - width) // 2
        bottom = top + width
        image = image.crop((0, top, width, bottom))
    return image

#  Load the image and crop it to square
image_path = "hero.jpg"
original_image = Image.open(image_path)
original_image = crop_to_square(original_image).convert("L")

image_array = np.array(original_image)

# Define test grid size
rows, cols = 4, 4  

# Create figure with forced tight layout
fig, axes = plt.subplots(rows, cols, figsize=(8, 8), dpi=200, 
                         gridspec_kw={"wspace": 0, "hspace": 0})

# Remove extra padding in the layout
plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)

# Iterate over the grid
for i in range(rows):
    for j in range(cols):
        # Generate a random grayscale background
        gray_value = np.random.randint(200, 256)
        bg_color = np.full_like(image_array, gray_value)

        # Blend the background and original image
        blended_image = bg_color.copy()
        blended_image[image_array < 200] = image_array[image_array < 200]

        # Display in grid
        axes[i, j].imshow(blended_image, cmap="gray")  
        axes[i, j].set_xticks([])  # Remove ticks
        axes[i, j].set_yticks([])  # Remove ticks
        axes[i, j].axis("off")  # Hide axes

# **🔹 Save Image with No White Borders**
plt.savefig("test_fixed_4x4.png", dpi=300, bbox_inches="tight", pad_inches=0)

# Show image
plt.show()

print("✅ Image saved as test_fixed_4x4.png")

# Free memory
plt.close(fig)