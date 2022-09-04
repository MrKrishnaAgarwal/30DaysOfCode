from time import sleep
import pywhatkit as kit

kit.playonyt('Nyan Cat')
sleep(10)
kit.search('MrKrishnaAgarwal - GitHub')
sleep(10)
kit.info('Elon Musk', lines=3)
sleep(10)
kit.text_to_handwriting('Krishna participated in 30DaysOfCode', rgb=[0, 0, 255])
sleep(10)
kit.sendwhatmsg('+91 1234567890', 'Hello World', 12, 30)
sleep(10)
kit.image_to_ascii_art('test.png', 'test')
print("Check the test.txt file in the current directory")
sleep(10)
kit.shutdown(time=60)
sleep(10)   
print("All done!")