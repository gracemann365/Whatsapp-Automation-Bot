project : Whatsapp-Automation-Bot
bot :

what is it ? : simple whatsapp chat bot that uses automation libraries.

status : still under initial testing period 

how ?

+ Whatsapp - a class to organise code for readibility
+ wa_bot.nav_green_dot() - navigates the unread notification aka the 'green dot'  using pyautogui
+ wa_bot.nav_x() - navigates and closes any anomalies  if needed 
+ wa_bot.nav_message() - navigates to find the last send message 
+ wa_bot.get_message() - reads and analyses the message and fetches appropriate message from database 
+ wa_bot.nav_input_box() - navigates and finds the input box and types the fetched message in 
+ wa_bot.send_message() - sends the message by mimicking the enter button

features (till 06/11/22):

automatic response for 
+'hi','hello' : 'oi hello there' 
+'da' : 'what do you want ?'  
+ default : 'athe athe ....'

dependencies : 

+ MouseInfo==0.1.3

+ numpy==1.23.4

+ opencv-python==4.6.0.66
+ Pillow==9.3.0
+ PyAutoGUI==0.9.53
+ PyGetWindow==0.0.9
+ PyMsgBox==1.0.9
+ pynput==1.7.6
+ pyperclip==1.8.2
+ PyRect==0.2.0
+ PyScreeze==0.1.28
+ pytweening==1.0.4
+ six==1.16.0



