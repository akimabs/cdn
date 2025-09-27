import ffmpeg
import subprocess

# Input file
input_file = "backsound.mp3"
output_file = "fadein_backsound.mp3"

# Fade in duration: 2 detik
fade_duration = 2

# Use ffmpeg to add fade in only (no trim)
try:
    (
        ffmpeg
        .input(input_file)
        .filter('afade', t='in', st=0, d=fade_duration)
        .output(output_file, acodec='mp3')
        .overwrite_output()
        .run(quiet=True)
    )
    print(f"Fade in selesai. File disimpan sebagai {output_file}")
except ffmpeg.Error as e:
    print(f"Error: {e}")
    print("Trying with subprocess...")
    
    # Fallback to subprocess
    cmd = [
        'ffmpeg', '-i', input_file, 
        '-af', f'afade=t=in:st=0:d={fade_duration}',
        '-c:a', 'mp3',
        output_file, '-y'
    ]
    subprocess.run(cmd, check=True)
    print(f"Fade in selesai. File disimpan sebagai {output_file}")
