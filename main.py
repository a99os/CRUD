import psycopg2

import os
import time


class User():
    def __init__(self, name, surname, age, telnumber, jinsi, login, parol):
        self.name = name
        self.surname = surname
        self.age = age
        self.telnumber = telnumber
        self.jinsi = jinsi
        self.login = login
        self.parol = parol
        
    def connection(self):
        pass

    def register(self):
        print("Ro'yhatdan o'tish uchun sorovnomani to'ldiring!\n")
        self.name = input('Ismingizni kirintg: ')
        self.surname = input("Familiyangizni kirintg: ")
        self.age = int(input("Yoshingizni kiritng: "))
        self.telnumber = int(input("Telefon raqamingizni kirintg: "))
        self.jinsi = input("[1] erkak\n[2] ayol\n")
        if self.jinsi == '1' or 'erkak':
            self.jinsi = str("erkak")
        else:
            self.jinsi = str("ayol")
        

        self.login = input(f"{self.name} yangi login kiriting: ")

        self.parol = input("Parolni kirintg: ")
        os.system('clear')
        print(f"Tabriklaymi!\nMuvaffaqiyatli ro'yhatdan o'tdingiz\n\nlogin:{self.login}\nparol:{self.parol}\n\n")
        time.sleep(2.4)
        os.system('clear')
        b.signIn()



    def signIn(self):
        a = input("[1] Shahsiy sahifaga kirish\n[2] Ro'yhatdan o'tish\nAmalni tartib raqamini kiritishingiz mumkin!\n\n: ")
        
        if a == '1' or a == 'Shahsiy sahifaga kirish':
            b.checkLogin()
        elif a == '2' or a == "Ro'yhatdan o'tish":
            b.register()
            

    #login bormi yo'qmi
    def checkLogin(self):
        pass

    def changePassword(self):
        a = self.parol
        self.parol = input("Ortga qaytish uchun 0 kiritng\nYangi parolni kirintg: ")
        
        if self.parol == '0':
            self.parol = a
            b.signIn()

    def generatePassword():
        pass

    def getById():
        pass

    def deleteById():
        pass

    def checkLoginAndPassword():
        pass

    def check():
        pass



b = User(' ', " ", 0, 0, 0, ' ', ' ')
b.signIn()