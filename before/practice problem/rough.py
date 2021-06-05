# for i in range(1, 5):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print("\n")


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == "__main__":
    speak("I am Prashant")
