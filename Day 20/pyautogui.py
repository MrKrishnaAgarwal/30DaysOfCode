import pyautogui

pyautogui.click()
pyautogui.typewrite('Hello, World!', interval=0.25)
pyautogui.click()
pyautogui.alert('This is an alert box.')
pyautogui.confirm('Shall I proceed?')
pyautogui.prompt('What is your name?')
pyautogui.password('Enter password (text will be hidden)')
pyautogui.alert('Thanks for your time.')
