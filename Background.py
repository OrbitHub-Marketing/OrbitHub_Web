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

# Convert the image to a NumPy array
image_array = np.array(original_image)

# Define the number of rows and columns
rows, cols = 40, 40  

# Create figure with high resolution
fig, axes = plt.subplots(rows, cols, figsize=(20, 20), dpi=100, gridspec_kw={'wspace': 0, 'hspace': 0})
fig.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)

# Iterate over each cell, assigning a random grayscale background
for i in range(rows):
    for j in range(cols):
        # Generate a random grayscale value (between 200 and 255) for each cell
        gray_value = np.random.randint(100, 256)  # Wider range to see variation

        # Create a background with this grayscale value
        bg_color = np.ones_like(image_array) * gray_value  # Ensure it's properly applied

        # Blend the background and original image
        blended_image = np.where(image_array < 200, image_array, bg_color)

        # Display the modified cell
        axes[i, j].imshow(blended_image, cmap="gray", vmin=0, vmax=255)  # Ensure full grayscale range
        axes[i, j].axis("off")  # Hide axes for a seamless effect


# Save the output with high resolution
output_path = "output_40x40.png"
plt.savefig(output_path, dpi=600, bbox_inches="tight")
plt.show()

print(f"✅ Image saved as: {output_path}")

# Save memory after saving
plt.close(fig)