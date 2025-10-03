from PIL import Image
import os

def format_size(size):
    """Convert size in bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}GB"

input_dir = 'img-not-convert'
output_dir = 'img'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("\nImage Conversion and Size Comparison:")
print("-" * 60)
print(f"{'Original File':<30} {'Original Size':<15} {'WebP Size':<15} {'Savings'}")
print("-" * 60)

total_original_size = 0
total_webp_size = 0

# Get all files from the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Open the image
        input_path = os.path.join(input_dir, filename)
        original_size = os.path.getsize(input_path)
        total_original_size += original_size
        
        img = Image.open(input_path)
        
        # Create output filename (change extension to .webp)
        output_filename = os.path.splitext(filename)[0] + '.webp'
        output_path = os.path.join(output_dir, output_filename)
        
        # Convert and save as WebP
        img.save(output_path, 'WEBP', quality=80)
        
        # Get size of converted file
        webp_size = os.path.getsize(output_path)
        total_webp_size += webp_size
        
        # Calculate size reduction
        size_reduction = ((original_size - webp_size) / original_size) * 100
        
        # Print comparison
        print(f"{filename:<30} {format_size(original_size):<15} {format_size(webp_size):<15} {size_reduction:.1f}%")

# Print totals
print("-" * 60)
total_reduction = ((total_original_size - total_webp_size) / total_original_size) * 100
print(f"{'Total:':<30} {format_size(total_original_size):<15} {format_size(total_webp_size):<15} {total_reduction:.1f}%")
print("-" * 60)