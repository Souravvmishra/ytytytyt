import cv2
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def add_audio_to_video(video_path, audio_path, output_path='reel_with_audio.mp4'):
    # Load the video clip
    video_clip = VideoFileClip(video_path)
    
    # Load the audio clip
    audio_clip = AudioFileClip(audio_path)
    
    # If the audio clip is longer than the video clip, trim it
    if audio_clip.duration > video_clip.duration:
        audio_clip = audio_clip.subclip(0, video_clip.duration)
    
    # Composite the audio onto the video
    video_clip = video_clip.set_audio(CompositeAudioClip([audio_clip]))
    
    # Write the result to a new file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


def image_to_video(image_path, output_video_path="reel_without_audio.mp4"):
    # Read the image
    image = cv2.imread(image_path)
    
    # Get image dimensions
    height, width, _ = image.shape
    
    # Create video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change codec as per your preference
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))
    
    # Calculate number of frames based on duration
    audio_clip = AudioFileClip('test.mp3')
    duration = audio_clip.duration
    num_frames = int(duration) * 30  # Assuming 30 frames per second
    
    # Write image frames to video
    for _ in range(num_frames):
        video_writer.write(image)
    
    # Release video writer object
    video_writer.release()

def make_video():
    image_to_video('reel_photo.png')
    add_audio_to_video('reel_without_audio.mp4', 'test.mp3', )
