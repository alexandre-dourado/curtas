from PIL import Image
import os

input_dir = "files"
output_dir = "files_webp"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def convert_to_webp(directory):
    for root, dirs, files in os.walk(directory):
        # Create corresponding subdirs in output
        rel_path = os.path.relpath(root, directory)
        target_root = os.path.join(output_dir, rel_path) if rel_path != "." else output_dir
        if not os.path.exists(target_root):
            os.makedirs(target_root)
            
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                input_path = os.path.join(root, file)
                # Keep same filename but change extension
                name_no_ext = os.path.splitext(file)[0]
                output_path = os.path.join(target_root, f"{name_no_ext}.webp")
                
                try:
                    with Image.open(input_path) as img:
                        # Convert to RGB if necessary (for PNGs with alpha to WebP it's fine, 
                        # but some formats might need conversion)
                        img.save(output_path, "WEBP", quality=80)
                    print(f"Converted: {input_path} -> {output_path}")
                except Exception as e:
                    print(f"Failed to convert {input_path}: {e}")

if __name__ == "__main__":
    convert_to_webp(input_dir)
    print("\nConversão concluída. Agora você pode substituir os arquivos originais pelos .webp na pasta 'files'.")
