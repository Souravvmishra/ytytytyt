import requests
from PIL import Image, ImageDraw
from io import BytesIO

from turn_to_video import image_to_video
from turn_to_video import make_video

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def create_photo_for_video():
# Fetch the image from URL
    url = 'https://source.unsplash.com/random/1080x1920/?oil-painting-art'
    response = requests.get(url)

    if response.status_code == 200:
        # Request was successful
        fetched_image = Image.open(BytesIO(response.content))

        # Create a black overlay with the same size as the fetched image
        black_overlay = Image.new('RGBA', fetched_image.size, (0, 0, 0, 200))

        # Paste the black overlay onto the fetched image
        fetched_image.paste(black_overlay, (0, 0), black_overlay)

        # Open the image you want to paste over the fetched image
        overlay_image_path = './fake_tweet_with_image.png'
        overlay_image = Image.open(overlay_image_path)
        overlay_image = add_corners(overlay_image, 10)

        # Calculate the new size for the overlay image while maintaining the aspect ratio
        width, height = overlay_image.size
        new_width = int(width * 1.2)  # Adjust the factor as needed to make the image bigger
        new_height = int(height * 1.2)  # Adjust the factor as needed to make the image bigger
        overlay_image_resized = overlay_image.resize((new_width, new_height))

        # Paste the resized overlay image onto the fetched image without using a mask
        fetched_image.paste(overlay_image_resized, (200, 1000))

        # Show the modified image
        fetched_image.save('reel_photo.png')
        
        
    else:
        # Request failed
        print("Error:", response.status_code)

def final_Video():
    create_photo_for_video()
    image_to_video('./reel_photo.png')
    make_video()
