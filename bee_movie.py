import subprocess, keyboard, time

time.sleep(5) #Time to set up cursor in chat
'''
#Fun random trolling sequence
keyboard.write('Opening /User/nithinsenthil/Bee_Movie_Script.txt')
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.write('\~~Initializing iMessage Security Bypass~~/')
keyboard.press_and_release('enter')
time.sleep(0.25)
keyboard.write('Completion in 5')
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.write('4')
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.write('3')
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.write('2')
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.write('1')
keyboard.press_and_release('enter')
time.sleep(0.25)
keyboard.write('Bypass Complete Program Optimized For Confusion')
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.write('Running Script.....')
keyboard.press_and_release('enter')
time.sleep(1)
'''
#Actual Code
script = open('HP_Chamber_Of_Secrets.txt') #Open file

for line in script: #Iterate through lines in file

    list = line.split() #Turn selected line into list with items seperated by word

    for i in list: #Iterate through words in "line" list

        keyboard.write(i) #Type word
        time.sleep(0) #Small delay
        keyboard.press_and_release('enter') #Press enter

script.close()
