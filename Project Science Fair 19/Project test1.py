input1 = input("Enter what you want to speech:")


def speech(text):
    from gtts import gTTS
    from pygame import mixer

    speech = gTTS(text)

    speech.save("test.mp3")

    mixer.init()
    mixer.music.load("C:/Users/Aized Sumbal/Documents/Web class/Python/python_for_everyone/test.mp3")
    mixer.music.play()


speech(input1)
