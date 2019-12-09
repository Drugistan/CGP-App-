
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import numpy as np
from Entry import Entry


sm = ScreenManager()


class MenuScreen(Screen):
    def switch_screen(self):
        sm.switch_to(screen= Buttons() , direction='right')


class Buttons(Screen):
    def List(self):
        sm.switch_to(screen= List_page(), direction= 'up')


class List_page(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(List_page, self).__init__(**kwargs)
        self.data = list()

    def fetch_data(self):
        data = list()
        int_list = list()
        str_list = list()
        grade_list = list()
        total_list = list()
        for a_child in reversed(self.container.children):
            if isinstance( a_child, TextInput):
                data.append(a_child.text)
        print(data)
        self.__process_data(data)
        self.__validation()
        self.__parse_int(data, int_list, str_list, grade_list)
        self.__calculation(int_list, grade_list, total_list)

    def __process_data(self, data):
        self.data.append(Entry(data[0], data[1], data[2]))
        self.data.append(Entry(data[3], data[4], data[5]))
        self.data.append(Entry(data[6], data[7], data[8]))
        self.data.append(Entry(data[9], data[10], data[11]))
        self.data.append(Entry(data[12], data[13], data[14]))
        self.data.append(Entry(data[15], data[16], data[17]))
        self.data.append(Entry(data[18], data[19], data[20]))

    def __validation(self):
        for an_entry in self.data:
            an_entry.validate_field()

    def __calculation(self, int_list, grade_list, total_list):
        total_value = 0
        for value in int_list:
            total_value = total_value + value
        print("{} Total value is int_list".format(total_value))
        for value in grade_list:
            if value >= 85:
                gd_value = 4.00
                total_list.append(gd_value)
            elif value >= 80 and value<=84:
                gd_value = 3.70
                total_list.append(gd_value)
            elif value>= 75 and value<=79:
                gd_value = 3.40
                total_list.append(gd_value)
            elif value>= 70 and value<=74:
                gd_value = 3.00
                total_list.append(gd_value)
            elif value>=65 and value<=69:
                gd_value = 2.50
                total_list.append(gd_value)
            elif value>=60 and value<=64:
                gd_value = 2.00
                total_list.append(gd_value)
            elif value>=55 and value<=59:
                gd_value = 1.50
                total_list.append(gd_value)
            elif value>=50 and value<=54:
                gd_value = 1.00
                total_list.append(gd_value)
            elif value <= 49:
                gd_value = 0.00
                total_list.append(gd_value)
            print(total_list)
        np_list = np.array(int_list)
        np_list2 = np.array(total_list)
        save_values = np_list * np_list2
        countGp = list(save_values)
        print("multi play ")
        print(countGp)
        total = 0
        for add in countGp:
            total = total + add
        print("sab add")
        print(total)
        try:
            final_opr = (total / total_value)
            num = ("%.2f"%final_opr)
            show = Pop()
            show.ids.result.text = str(num)
            window = Popup(title="Final GPA", content=show, size_hint=(None, None), size=(300, 300), auto_dismiss=True)
            window.open()
        except:
            erro = Messg()
            anss = "Data Requires"
            throw = Popup(title="Value Error", content=erro, size_hint=(None, None), size=(300, 300), auto_dismiss=True)
            throw.open()

    def __parse_int(self, data, int_list, str_list, grade_list):
        print("__Parse items")
        print(data)
        for x in data:
            if len(x) > 2 and type(x) == str:
                str_list.append(x)
            elif len(x) == 1:
                int_list.append(int(x))
            elif len(x) >=2  and len(x) <=4:
                grade_list.append(int(x))
        print(int_list)
        print(str_list)
        print(grade_list)

    def move_back(self):
        sm.switch_to(screen=Buttons(), direction="up")
        pass


class Pop(BoxLayout):
    pass


class Messg(BoxLayout):
    pass


class Callheros(App):
    def build(self):
        sm.add_widget(MenuScreen())
        sm.add_widget(Buttons())
        sm.add_widget(List_page())
        return sm


if __name__ == "__main__":
    Callheros().run()
