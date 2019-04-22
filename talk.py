
import speech_recognition as sr
import serial

command = 0
command_2 = 60
command_3 = 120


arduino = serial.Serial('COM6', 9600)   # create serial object named arduino

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=5)
    print('Please Let me know the Number of the File')
    audio = r.listen(source)

    try:
        print("I think you said '" + r.recognize_sphinx(audio) + "'")
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))




while r.recognize_sphinx(audio) != ('stop'): #say stop to terminate the process#


    if r.recognize_sphinx(audio) == ('one') or ('juan') or ('why'): #sometimes speech recognition mishearing my words so i've added the top two words it understands when i say 'one'.
        arduino.write(command)
    elif r.recognize_sphinx(audio) == ('two') or ('true'):
        arduino.write(command_2)
    elif r.recognize_sphinx(audio) == ('three') or ('tree'):
        arduino.write(command_3)
    else:
        print ('Sorry didnt got that')



    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=5)
        print('Please Let me know the Number of the File')
        audio = r.listen(source)

        try:
            print("I think you said '" + r.recognize_sphinx(audio) + "'")
        except sr.UnknownValueError:
            print("I could not understand audio")
        except sr.RequestError as e:
            print("Error; {0}".format(e))


print ('Gotha.C u soon')
