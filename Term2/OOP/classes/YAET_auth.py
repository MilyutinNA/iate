from tkinter import *
from tkinter import ttk
user = (1,"Ivan","ivan_10", "qwerty", 10000000)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.main()

    def forget_page(self):
        all_frames = [f for f in self.children]
        if all_frames:
            for f_name in all_frames:
                self.nametowidget(f_name).destroy()

    def succes_page(self):
        self.forget_page()
        self.succes_page = Success().pack()

    def main(self):
        self.forget_page()
        self.main = MainPage().pack()

class Field(Frame):
    def __init__(self, text):
        super().__init__()
        self.l1 = Label(self, text = text)
        self.l2 = Label(self, text = "")
        self.e = Entry(self)
        self.l1.pack()
        self.e.pack()
        self.l2.pack()

class MainPage(Frame):

    def __init__(self):
        super().__init__()
        self.field_login = Field("Логин")
        self.field_login.pack()
        self.field_password = Field("Пароль")
        self.field_password.pack()

        self.b1=Button(self, text= 'Войти', command=self.button_enter)
        self.b1.pack()
        self.b2 = Button(self, text='Забыли пароль?')
        self.b2.pack()
        self.b3 = Button(self, text='Регистрация')
        self.b3.pack()

    def button_enter(self):
        # доделать
        login = self.field_login.e.get()
        password = self.field_password.e.get()
        if login == user[2] and password == [3]:
            self.master.succes_page()



class Success(Frame):
    def __init__(self):
        super().__init__()
        self.l1 = Label(self, text=('Вы успешно авторизовались. Остаток на счёте: ' + str(user[-1])))
        self.l1.pack()
        self.button_return = Button(self, text= 'Вернуться назад', command=self.button_return)
        self.button_return.pack()
    def button_return(self):
        self.master.main()
a = App()
a.mainloop()




