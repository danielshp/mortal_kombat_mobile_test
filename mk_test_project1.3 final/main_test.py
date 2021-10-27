# Создание и запуск приложения, программирование интерфейса экранов и действий на них
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from kivy.base import stopTouchApp
from kivy.uix.popup import Popup
from kivy.properties import  NumericProperty
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3
from  scrollLabel import ScrollLabel
#from ruffier import test
#from coloredLayout import ColoredLayout

#from sits import Sits
#from runner import Runner
# Здесь должен быть твой код
Window.clearcolor = (.5 , .2, .73, 1)
btn_color = (.250, .252, .21, .5)

name = ""
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

'''class Scrresult(Screen):
    result_test  = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def answers(self):
        self.result_test  += 1'''


total = 0
class InstrScr(Screen):
    
    def __init__(self, **kwargs):
        
        super().__init__( **kwargs)
        
        instr = ScrollLabel(txt_instruction, textcolor= '#FFFFFF')
        lbl1 = Label(text = 'Введите имя: ', halign = 'right')
        self.in_name = TextInput(multiline = False)
        
        
        self.btn = Button(text = "Начать", size_hint = (0.3, 0.2), pos_hint = {"center-x":0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current = 'pulse1' 
class PulseScr(Screen): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = True
        
        lbl1 = ScrollLabel('Как появился персонаж Ермак?', textcolor= '#FFFFFF')

        self.btn1 = Button(text = 'Из за ошибки в одной из старых частей',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        self.btn2 = Button(text = 'Его добавили в одной из частей как одного из антогонистов ',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        self.btn3 = Button(text = 'Его добавили в одной из частей как одного из протогонистов',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        self.btn4 = Button(text = 'Из за ошибки в одной из новых частей',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        line1 = BoxLayout()
        vlay = BoxLayout(orientation = 'vertical')
        vlay.add_widget(lbl1)
        vlay.add_widget(self.btn1)
        vlay.add_widget(self.btn2)
        vlay.add_widget(self.btn3)
        vlay.add_widget(self.btn4)
        

        line1.add_widget(vlay)
        self.add_widget(line1)
        self.btn1.on_press = self.next
        self.btn2.on_press = self.next
        self.btn3.on_press = self.next
        self.btn4.on_press = self.next
        

    def next(self):
        right = Popup(title='Правильный ответ был: ', content=Label(text='Из за ошибки в одной из старых частей '), size_hint=(None, None), size=(600, 600), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        right.open()
        self.manager.current  = 'pulse2'
        


        



class PulseScr2(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        

        lbl1 = ScrollLabel('Откуда персонаж Ruby', textcolor= '#FFFFFF')
        self.btn2 = Button(text = 'Из первого фильма по Mortl Kombat',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        self.btn3 = Button(text = 'Второстепенный персонаж из 3 части Mortl Kombat',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        self.btn4 = Button(text = 'Второстепенный персонаж из Mortl Kombat Ultimate',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        self.btn1 = Button(text = 'Персонаж из сериала "Смертельная битва: Защитники земли"',size_hint = (1, 0.5), pos_hint = {"center-x":0.5})
        self.btn1.on_press = self.next
        self.btn2.on_press = self.next
        self.btn3.on_press = self.next
        self.btn4.on_press = self.next
        line1 = BoxLayout()
        vlay = BoxLayout(orientation = 'vertical')
        vlay.add_widget(lbl1)
        vlay.add_widget(self.btn1)
        vlay.add_widget(self.btn2)
        vlay.add_widget(self.btn3)
        vlay.add_widget(self.btn4)
        

        line1.add_widget(vlay)
        self.add_widget(line1)



    def next(self):
        right = Popup(title='Правильный ответ был: ', content=Label(text='Персонаж из сериала "Смертельная битва: Защитники земли '), size_hint=(None, None), size=(600, 600), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        right.open()
        self.manager.current = 'pulse3'
        




class PulseScr3(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0
        instr = ScrollLabel(txt_test3, textcolor= '#FFFFFF'  )

        self.lbl1 = ScrollLabel('Напишите 2 правителей внешнего мира, которые имели приставку кан в имени',textcolor='#FFFFFF' )
        line0 = BoxLayout()
        vlay = BoxLayout(orientation = 'vertical', )
        vlay.add_widget(self.lbl1)
        line0.add_widget(instr)
        line0.add_widget(vlay)


        line1 = BoxLayout(size_hint = (0.8, None),height = "30sp")
        lbl_result1 = Label(text = "правил раньше:", halign = "right")
        self.in_result1 = TextInput(text = "_",multiline = False)


        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)


        line2 = BoxLayout(size_hint = (0.8, None),height = "30sp")
        lbl_result2 = Label(text = "правил позже:", halign = "right")
        self.in_result2 = TextInput(text = "_",multiline = False)

        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)



        self.btn = Button(text = "Продолжить",size_hint = (0.3, 0.2), pos_hint = {"center-x":0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line0)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)


    def next(self):
        right = Popup(title='Правильным ответ был:  ', content=Label(text='Шао кан и Коталь кан'), size_hint=(None, None), size=(600, 600), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        right.open()
        self.manager.current = 'pulse4'

class PulseScr4(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0
        instr = ScrollLabel(txt_test3, textcolor= '#FFFFFF'  )

        self.lbl1 = ScrollLabel('Напишите 2 старших бога, между которыми было противостояние',textcolor='#FFFFFF' )
        line0 = BoxLayout()
        vlay = BoxLayout(orientation = 'vertical', )
        vlay.add_widget(self.lbl1)
        line0.add_widget(instr)
        line0.add_widget(vlay)


        line1 = BoxLayout(size_hint = (0.8, None),height = "30sp")
        lbl_result1 = Label(text = "один из главных антогонистов:", halign = "right")
        self.in_result1 = TextInput(text = "_",multiline = False)


        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)


        line2 = BoxLayout(size_hint = (0.8, None),height = "30sp")
        lbl_result2 = Label(text = "один из главных героев:", halign = "right")
        self.in_result2 = TextInput(text = "_",multiline = False)

        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)



        self.btn = Button(text = "Продолжить",size_hint = (0.3, 0.2), pos_hint = {"center-x":0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line0)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)


    def next(self):
        right = Popup(title='Правильным ответом был ', content=Label(text='Шиннок и Рейден'), size_hint=(None, None), size=(600, 600), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        right.open()
        self.manager.current = 'result'  
class Result(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        
        self.btn = Button(text = 'Завершить',size_hint =(0.3, 0.2) , pos_hint ={'center-x':0.5})
        self.btn.background_color = btn_color
        self.instr = Label(text = 'Спасибо за прохождения теста. Хорошего дня')
        self.btn.on_press = self.next
        
        self.outer.add_widget(self.instr)
        self.outer.add_widget(self.btn)
        self.add_widget(self.outer)


    def next(self):
        stopTouchApp()

class HeartCheck(App):
    def build(self):
        sm  = ScreenManager()
        sm.add_widget(InstrScr(name = 'instr'))
        sm.add_widget(PulseScr(name = 'pulse1'))
        sm.add_widget(PulseScr2(name = 'pulse2'))
        sm.add_widget(PulseScr3(name = 'pulse3'))
        sm.add_widget(PulseScr4(name = 'pulse4'))
        sm.add_widget(Result(name = 'result'))
        return sm
app = HeartCheck()
app.run()




