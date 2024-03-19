import pyttsx3
from google02 import get_tweet
from image import newtweett
from video import final_Video
import telebot

bot = telebot.TeleBot('6822661896:AAHiLR9uBE023-x3TaTJHSvRiqgtyKCzDTw')

engine = pyttsx3.init()
engine.setProperty('rate', 175)
import time

tweet = get_tweet()
newtweett(tweet)
engine.save_to_file(tweet, 'test.mp3')

print(tweet)

engine.runAndWait()

final_Video()
with open('reel_with_audio.mp4', 'rb') as f:
    bot.send_document('960867942', f)
