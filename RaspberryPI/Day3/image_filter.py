import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def apply_sepia(image):
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    sepia_image = image.dot(sepia_filter.T)
    sepia_image = np.clip(sepia_image, 0, 1)  # Ensure values are within valid range
    return sepia_image

def apply_grayscale(image):
    grayscale_filter = np.array([0.299, 0.587, 0.114])
    grayscale_image = image.dot(grayscale_filter)
    grayscale_image = np.stack((grayscale_image,)*3, axis=-1)  # Convert to 3 channel image
    return grayscale_image

def apply_inverted(image):
    inverted_image = 1 - image  # Invert colors
    return inverted_image

def show_images(original, sepia, grayscale, inverted):
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    axes[0].imshow(original)
    axes[0].set_title('Original')
    axes[0].axis('off')

    axes[1].imshow(sepia)
    axes[1].set_title('Sepia')
    axes[1].axis('off')

    axes[2].imshow(grayscale)
    axes[2].set_title('Grayscale')
    axes[2].axis('off')

    axes[3].imshow(inverted)
    axes[3].set_title('Inverted')
    axes[3].axis('off')

    plt.show()

# Load image
image = mpimg.imread('/home/sorin-wsl/lena.jpg') / 255.0  # Normalize to [0, 1]

# Apply filters
sepia_image = apply_sepia(image)
grayscale_image = apply_grayscale(image)
inverted_image = apply_inverted(image)

# Show images
show_images(image, sepia_image, grayscale_image, inverted_image)
