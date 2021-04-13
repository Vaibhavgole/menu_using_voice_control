
import speech_recognition as sr
import os
import sys
r = sr.Recognizer()
devnull = os.open(os.devnull, os.O_WRONLY)
old_stderr = os.dup(2)
sys.stderr.flush()
os.dup2(devnull, 2)
os.close(devnull)
with sr.Microphone() as target:
    print("i am listening")
    x = r.listen(target,timeout=4,phrase_time_limit=5)
    print("Done")
a = r.recognize_google(x,language="en-in")
print(a)
