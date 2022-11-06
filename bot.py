import PIL
import pyautogui as pt 
import pyperclip as pc
from time import sleep 
from pynput import mouse 
from pynput.mouse import Controller,Button
from responses import response
mouse = Controller()

#whatsappbot class 
#all the pixels here our adjusted relatively to windows whatsapp hence if ur on mac , caliberate accordingly !!!
class Whatsapp:
    def __init__(self,speed=.5,click_speed=.3):
        self.speed = speed 
        self.click_speed=click_speed
        self.message=''
        self.lastmessage=''
        
    def nav_green_dot(self):
        try:
            position=pt.locateOnScreen("green_dot.png",confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,10,duration=self.speed)
            mouse.click(Button.left,2)
        except Exception as e:
            print("excepton(nav_green_dots): ", e)
            
    
    def nav_input_box(self):
        try:
            position=pt.locateOnScreen("clipp.png",confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("excepton(nav_input_box): ", e)
            
    def nav_message(self):
        try:
            position=pt.locateOnScreen("clipp.png",confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(70,-70,duration=self.speed)# 1035#
        except Exception as e:
            print("excepton(nav_message): ", e)
            
    def get_message(self):
        mouse.click(Button.left,3)
        sleep(self.speed)
        mouse.click(Button.right,1)
        '''sleep(self.speed)
        mouse.click(Button.left,1)'''
        
        sleep(self.speed)
        pt.moveRel(17,-165,duration=self.speed)# -17#
        mouse.click(Button.left,1)
        sleep(1)
        
        self.message = pc.paste()
        print("user says : ",self.message)   


        ''' pt.tripleClick() #code does not copy the entire message for some unknown reason so using another package
        sleep(self.speed)
        pt.click()
        sleep(self.speed)
        pt.moveRel(70,70,self.speed)
        pt.click()
        sleep(1)
        
        self.message=pc.paste()
        print('user says :',self.message)'''
        
    def send_message(self):
        try:
            if self.message != self.lastmessage:
                bot_response= response(self.message)
                print("u say : ",bot_response)
                pt.typewrite(bot_response,interval=.1)
                pt.typewrite('\n')
                self.last_message=self.message
            else:
                print("no new messages....")
        except Exception as e:
            print('exception (send-message:',e)
            
    def nav_x(self):
         try:
            position=pt.locateOnScreen("x.png",confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(12.5,12.5,duration=self.speed)# #70
            mouse.click(Button.left,1)
         except Exception as e:
            print("excepton(nav_message): ", e)
            



wa_bot=Whatsapp(speed=.5,click_speed=.4)
sleep(2)

while True :
    wa_bot.nav_green_dot()
    wa_bot.nav_x()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()
    sleep(7)

    
    

            
