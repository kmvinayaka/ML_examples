from gtts import gTTS 
import time 
mytext = 'engineering college'
import os 
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("enginee.mp3")

time.sleep(2)
import playsound
playsound.playsound('enginee.mp3', True)
  
'''# Playing the converted file 
#os.system("enginee.mp3")'''
