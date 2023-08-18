# Задание
# Напишите программу «Счет, пожалуйста!».
# Она должна показать пользователю несложное ресторанное меню с блюдами и ценами,
# принять заказ и вывести на экран сумму счета.

from tkinter import *


class Application(Frame):
    """ GUI application """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.cart = 0
        self.check = ""
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose your dishes").grid(row=0, column=0, sticky=W)

        self.egg = BooleanVar()
        Checkbutton(self,
                    text="Egg with butter and salt\t\t0,50 USD",
                    variable=self.egg,
                    command=self.refresh_cart
                    ).grid(row=1, column=0, sticky=W)

        self.porr = BooleanVar()
        Checkbutton(self,
                    text="Oatmeal porridge with raisins\t0,75 USD",
                    variable=self.porr,
                    command=self.refresh_cart
                    ).grid(row=2, column=0, sticky=W)

        self.bred = BooleanVar()
        Checkbutton(self,
                    text="Villagers bread\t\t\t0,20 USD",
                    variable=self.bred,
                    command=self.refresh_cart
                    ).grid(row=3, column=0, sticky=W)

        self.tea = BooleanVar()
        Checkbutton(self,
                    text="Black tea\t\t\t\t0,40 USD",
                    variable=self.tea,
                    command=self.refresh_cart
                    ).grid(row=4, column=0, sticky=W)

        Button(self,
               text="Сформировать заказ",
               command=self.checkout
               ).grid(row=6, column=0)

        self.display_cart()
        self.display_checkout()

    def display_cart(self):
        total_txt = str(self.cart)
        total_txt += " USD"
        Label(self, text=total_txt, width=25, height=1, bg="lightblue", font="22").grid(row=5, column=0, sticky=W)

    def display_checkout(self):
        self.total = Text(self, width=40, height=10, font=("Consolas", 8))
        self.total.grid(row=7, column=0)

    def checkout(self):
        line1, line2, line3, line4 = "", "", "", ""
        if self.egg.get():
            line1 = cafe_menu[0][0]
            dots = 31 - len(line1)
            line1 += "." * dots
            line1 += cafe_menu[0][1] + "\n"
        if self.porr.get():
            line2 = cafe_menu[1][0]
            dots = 31 - len(line2)
            line2 += "." * dots
            line2 += cafe_menu[1][1] + "\n"
        if self.bred.get():
            line3 = cafe_menu[2][0]
            dots = 31 - len(line3)
            line3 += "." * dots
            line3 += cafe_menu[2][1] + "\n"
        if self.tea.get():
            line4 = cafe_menu[3][0]
            dots = 31 - len(line4)
            line4 += "." * dots
            line4 += cafe_menu[3][1] + "\n"

        # Вывод итогов
        total_check = line1 + line2 + line3 + line4
        total_check += "_" * 40

        dollar = self.cart // 1
        cent = self.cart % 1 * 100
        price = "USD: " + str(int(dollar)) + "," + str(int(cent))
        total_check += "\nTOTAL"
        dots = 35 - len(price)
        total_check += "." * dots
        total_check += price
        self.total.delete(0.0, END)
        self.total.insert(0.0, total_check)

    def refresh_cart(self):
        self.cart = 0
        if self.egg.get():
            self.cart += 0.50
        if self.porr.get():
            self.cart += 0.75
        if self.bred.get():
            self.cart += 0.20
        if self.tea.get():
            self.cart += 0.40
        print(self.cart)
        self.display_cart()


# main
cafe_menu = [("Egg with butter and salt", "USD: 0,50", 0.50),
             ("Oatmeal porridge with raisins", "USD: 0,75", 0.75),
             ("Villagers bread", "USD: 0,20", 0.20),
             ("Black tea", "USD: 0,40", 0.40,)]
cart_total = 0
root = Tk()
root.title("Restaurant menu")
app = Application(root)
root.mainloop()
