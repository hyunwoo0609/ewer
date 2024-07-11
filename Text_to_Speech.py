from gtts import gTTS
import pygame 

file_name = 'sample.mp3'

# 영어 문장
# text = 'One of Molly Bloom\'s soliloquies in James Joyce\'s epic novel \'Ulysses\' features a sentence of 4,491 words'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# 한글 문장
# text = '저는 고양이가 세상에서 제일 좋아요'
# tts_kr = gTTS(text=text, lang='ko')
# tts_kr.save(file_name)

# 긴 문장 (파일에서 불러와서 처리)
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)

def playsound(audio):
    pygame.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

audio = file_name
playsound(audio)   #  mp3 파일 재생










