from datetime import datetime
from kivy.app import App
from random import random
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup


class Base(BoxLayout):

    def relogio(self,*args):
        '''Function to generate random numbers for rgba color property of the clock.
            Then, it gets the current hour, minuts and seconds and send it to the label on kv file, formatted to show 2
            digits'''

        r = random()
        g = random()
        b = random()
        a = random()
        self.cor = r, g, b, a
        #print(cor)


        h = datetime.today().hour
        m = datetime.today().minute
        sec = datetime.today().second
        time = f'{h:02d}:{m:02d}:{sec:02d}'
        self.ids.relogio_lbl.text = time
        return time


class Pop1(Popup):
    pass

pop = Pop1()


class RelogioApp(App):
    def build(self):
        base = Base()
        Clock.schedule_interval(base.relogio, 1)
        


        return base

RelogioApp().run()