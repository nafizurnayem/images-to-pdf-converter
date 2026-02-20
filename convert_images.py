import img2pdf
import os

# Define the directory containing images
image_dir = "F:\\AIUB\\11th Semester\\Computer Vision & Pattern Recognization\\Book\\Books"  # Change this to your desired directory

# Collect all image files (supports common formats like .png, .jpg, .jpeg, .gif, .bmp)
image_files = []
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        image_files.append(os.path.join(image_dir, filename))

# Convert the list of images to a PDF
with open("Modern Computer Vision with PyTorch.pdf", "wb") as f:
    f.write(img2pdf.convert(image_files))

print("✅ PDF created successfully: Modern Computer Vision with PyTorch.pdf")
