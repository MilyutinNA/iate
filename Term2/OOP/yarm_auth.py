from tkinter import *

user=(1,'Ivan','ivan123','qwerty')


class App(Tk):

    def __init__(self):
        super().__init__()
        self.main_page()

    def del_page(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()

    def main_page(self):
        self.del_page()
        self.main = MainPage()
        self.main.pack()

    def success_page(self):
        self.del_page()
        self.success = Success()
        self.success.pack()


class Field(Frame):

    def __init__(self,some_text):
        super().__init__()
        self.l1 = Label(self, text=some_text)
        self.l1.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.l2 = Label(self, text='')
        self.l2.pack()


class MainPage(Frame):

    def __init__(self):
        super().__init__()
        self.field_login = Field('Логин')
        self.field_password = Field('Пароль')
        self.field_login.pack()
        self.field_password.pack()

        self.b1 = Button(self,text='Войти', command=self.click_sign_in)
        self.b1.pack()
        self.b2 = Button(self,text='Забыли пароль?')
        self.b2.pack()
        self.b3 = Button(self,text='Регистрация')
        self.b3.pack()

    def click_sign_in(self):
        login = self.field_login.e1.get()
        password = self.field_password.e1.get()
        if user[2]==login:
            if user[3]==password:
                self.master.success_page()
            else:
                self.field_login.l2.config(text='')
                self.field_password.l2.config(text='Вы ввели неверный пароль')
        else:
            self.field_login.l2.config(text='Вы ввели неверный логин')
            self.field_password.l2.config(text='')


class Success(Frame):

    def __init__(self):
        super().__init__()
        self.l1=Label(self, text='Вы успешно авторизовались')
        self.l1.pack()
        self.b1=Button(self, text='Вернуться назад', command=self.return_back)
        self.b1.pack()

    def return_back(self):
        self.master.main_page()

a = App()
a.mainloop()