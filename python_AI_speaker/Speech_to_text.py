import speech_recognition as sr

# 마이크로 음성 듣기
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print('듣고 있어요')
#     audio = r.listen(source)  # 마이크로부터 음성 듣기

# 파일로 음성 불러오기
r = sr.Recognizer()

with sr.AudioFile('sample.wav') as source:
     audio = r.record(source)
     
try:
    text = r.recognize_google(audio, language='ko')   # 구글 API로 인식 (하루 50회)
    print(text)
except sr.UnknownValueError:
    print('인식 실패')   # 음성 인식 실패한 경우
except sr.RequestError as e:
    print(f'요청 실패 : {e}')  # API key 오류 혹은 네트워트 오류

