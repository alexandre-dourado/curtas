import os
import subprocess
from PIL import Image

# Configurações
FILES_DIR = "files"
THUMBS_DIR = "thumbs"
THUMB_SIZE = (400, 400)  # Tamanho máximo da thumb
WEBP_QUALITY = 60        # Qualidade agressiva para menor tamanho em KB

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_image_thumb(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img.thumbnail(THUMB_SIZE)
            # Converte para RGB se necessário para garantir compatibilidade WebP
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.save(output_path, "WEBP", quality=WEBP_QUALITY)
        return True
    except Exception as e:
        print(f"Erro na imagem {input_path}: {e}")
        return False

def generate_video_thumb(input_path, output_path):
    try:
        # Extrai frame aos 1 segundo (ou 0 se for menor) usando ffmpeg
        # -ss 1: tempo, -vframes 1: um frame, -q:v 2: qualidade alta no jpeg intermediário
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-ss", "00:00:01", "-vframes", "1",
            "-f", "image2", "pipe:1"
        ]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            from io import BytesIO
            img = Image.open(BytesIO(stdout))
            img.thumbnail(THUMB_SIZE)
            img.save(output_path, "WEBP", quality=WEBP_QUALITY)
            return True
        else:
            # Tenta aos 0 segundos caso o vídeo seja muito curto
            cmd[4] = "00:00:00"
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, _ = process.communicate()
            if process.returncode == 0:
                from io import BytesIO
                img = Image.open(BytesIO(stdout))
                img.thumbnail(THUMB_SIZE)
                img.save(output_path, "WEBP", quality=WEBP_QUALITY)
                return True
            print(f"Erro no vídeo {input_path}: {stderr.decode()}")
            return False
    except Exception as e:
        print(f"Erro ao processar vídeo {input_path}: {e}")
        return False

def process_all():
    ensure_dir(THUMBS_DIR)
    
    count_new = 0
    count_skip = 0
    
    for root, dirs, files in os.walk(FILES_DIR):
        # Recria estrutura de pastas em thumbs
        rel_path = os.path.relpath(root, FILES_DIR)
        target_dir = os.path.join(THUMBS_DIR, rel_path) if rel_path != "." else THUMBS_DIR
        ensure_dir(target_dir)
        
        for file in files:
            input_path = os.path.join(root, file)
            # A thumb terá o mesmo nome relativo mas extensão .webp
            thumb_name = os.path.splitext(file)[0] + ".webp"
            output_path = os.path.join(target_dir, thumb_name)
            
            if os.path.exists(output_path):
                count_skip += 1
                continue
            
            ext = file.lower().split('.')[-1]
            success = False
            
            if ext in ['jpg', 'jpeg', 'png', 'webp', 'gif', 'bmp']:
                success = generate_image_thumb(input_path, output_path)
            elif ext in ['mp4', 'webm', 'ogg', 'mov', 'm4v']:
                success = generate_video_thumb(input_path, output_path)
                
            if success:
                print(f"Gerado: {output_path}")
                count_new += 1
                
    print(f"\nConcluído!")
    print(f"Novas thumbs: {count_new}")
    print(f"Puladas (já existem): {count_skip}")

if __name__ == "__main__":
    process_all()
