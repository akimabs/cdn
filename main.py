import ffmpeg
import subprocess

# Input file
input_file = "soundtrack.mp3"
output_file = "trimmed_soundtrack.mp3"

# Start time: 1 minute 26 seconds = 86 seconds
start_time = 86

# Use ffmpeg to trim from 1:26 to end
try:
    (
        ffmpeg
        .input(input_file, ss=start_time)
        .output(output_file, acodec='mp3')
        .overwrite_output()
        .run(quiet=True)
    )
    print(f"Trim selesai. File disimpan sebagai {output_file}")
except ffmpeg.Error as e:
    print(f"Error: {e}")
    print("Trying with subprocess...")
    
    # Fallback to subprocess
    cmd = [
        'ffmpeg', '-i', input_file, 
        '-ss', str(start_time), 
        '-c', 'copy', 
        output_file, '-y'
    ]
    subprocess.run(cmd, check=True)
    print(f"Trim selesai. File disimpan sebagai {output_file}")
