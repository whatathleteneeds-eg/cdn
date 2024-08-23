import os
import glob

# List of common image file extensions
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.avif', '*.gif', '*.bmp', '*.tiff']

def find_images_in_directory(directory):
    image_files = []
    
    # Iterate over all the image extensions
    for ext in image_extensions:
        found_files = glob.glob(os.path.join(directory, ext))
        image_files.extend(found_files)

    return image_files

def extract_base_name(file_path):
    # Extract the file name without the extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    # Split by '-' and take the first part (the base name)
    base_name = file_name.split('-')[0]
    return base_name

if __name__ == "__main__":
    # Current directory
    current_directory = os.getcwd()
    
    # Find all images in the current directory
    images = find_images_in_directory(current_directory)
    
    # Extract and print the base names
    if images:
        print("Base names of the image files:")
        for image in images:
            base_name = extract_base_name(image)
            print(base_name)
    else:
        print("No image files found in the current directory.")
