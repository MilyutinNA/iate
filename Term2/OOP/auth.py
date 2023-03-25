from tkinter import *
from tkinter import ttk

def _del_all_frames(self, func):
    def wrapper():
        #перед добавлением новых фреймов удаляем все отображающиеся на данный момент
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        #добавляем ноый элемент
    return wrapper


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title('Auth')
        self.put_main_page()

    def put_main_page(self):
        self.main_page = MainPage().pack()

    def put_info_page(self):
        self.main_page = InfoPage().pack()



class InfoPage(Frame):

    def __init__(self):
        super().__init__()
        self.l = Label(self, text = 'Страница InfoPage', font=30)
        self.l.grid(row=0,column=0,columnspan=1)
        self.b = Button(self,text = 'Вернуться назад', command=self.return_back)
        self.b.grid(row=1,column=0,columnspan=1)

    def return_back(self):
        self.master.put_main_page()


class MainPage(Frame):

    """Элементы на главной странице"""

    def __init__(self):
        super().__init__()
        #создаем элементы на главной странице
        self.l = Label(self, text='Страница MainPage', font=30)
        self.l.pack()
        self.b = Button(self,text = 'Перейти на страницу InfoPage', command=self.return_back)
        self.b.pack()



app = App()
app.mainloop()
#%%
