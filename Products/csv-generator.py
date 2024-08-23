import os
import glob
import csv

# List of common image file extensions
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.avif', '*.gif', '*.bmp', '*.tiff', '*.svg', '*.ico', '*.jfif']

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

def generate_img_src(file_name):
    # Generate the image source URL
    return f"https://whatathleteneeds-eg.github.io/cdn/Products/{file_name}"

if __name__ == "__main__":
    # Current directory
    current_directory = os.getcwd() + '/images'
    
    # Find all images in the current directory
    images = find_images_in_directory(current_directory)
    
    # Prepare the data for the CSV file
    data_to_save = []
    
    if images:
        for image in images:
            base_name = extract_base_name(image)
            img_src = generate_img_src(os.path.basename(image))
            data_to_save.append([base_name, img_src])
        
        # sort data by Item ID
        data_to_save.sort(key=lambda x: x[0])

        # Write the data to a CSV file
        csv_file = 'wan-images_to_upload.csv'
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item ID', 'Image Src'])  # Write the header
            writer.writerows(data_to_save)  # Write the data
        
        print(f"Data saved to {csv_file}")

        print("Data:")
        print(data_to_save)
    else:
        print("No image files found in the current directory.")
