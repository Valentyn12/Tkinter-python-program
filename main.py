import tkinter 
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from store import connect
from tkinter.messagebox import showinfo, askyesno, showerror
import sys
import os


class Main(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.main_menu()
        connect()

    def main_menu(self):
        con = sqlite3.connect('store.db')
        cur = con.cursor()

        def update():
            for i  in self.tree.get_children():
                self.tree.delete(i)
                self.tree.pack()
            history = cur.execute('SELECT * FROM history').fetchall()
            for row in history:
                self.tree.insert("", tkinter.END, values = row)
            self.tree.pack()

        def delete(id):
            ID = id.get()
            cur.execute('DELETE FROM history WHERE ID = ?', (ID,))
            con.commit()
            update()
        tool_panel = tkinter.Frame(background="#C0C0C0", border=2)
        tool_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.add_icon_shop = tkinter.PhotoImage(file=resource_path("icon/store.png"))
        btn_choice_product = tkinter.Button(tool_panel, text="Вибір товару", command=shop, background="#C0C0C0", bd=0,
        compound=tkinter.TOP, image=self.add_icon_shop)
        btn_choice_product.pack(side=tkinter.TOP)


        self.add_icon_about = tkinter.PhotoImage(file=resource_path("icon/about.png"))
        btn_aboutme = tkinter.Button(tool_panel, text="Про програму", command=about, background="#C0C0C0", bd=0,
        compound=tkinter.TOP, image=self.add_icon_about)
        btn_aboutme.pack(side=tkinter.TOP)

        columns = ("ID","names_id","names","amount","price_non_PDW","total_price")
        self.tree = ttk.Treeview(self, show="headings", columns=columns, height=25)
        self.tree.heading("ID", text="№")
        self.tree.heading("names_id", text="ID товару")
        self.tree.heading("names", text="Назва товару")
        self.tree.heading("amount", text="кількість товару")
        self.tree.heading("price_non_PDW", text="Вартість")
        self.tree.heading("total_price", text='Вартісь з ПДВ')

        self.tree.column("ID", width=80, anchor=tkinter.CENTER)
        self.tree.column("names_id", width=110, anchor=tkinter.CENTER)
        self.tree.column("names", width=100, anchor=tkinter.CENTER)
        self.tree.column("amount", width=80, anchor=tkinter.CENTER)
        self.tree.column("price_non_PDW", width=100, anchor=tkinter.CENTER)
        self.tree.column("total_price", width=110, anchor=tkinter.CENTER)
        self.tree.pack()


        label_number = tkinter.Label(self, text='№')
        Entry_number = tkinter.Entry(self)
        but_delete = tkinter.Button(self, text="Прибрати", command=partial(delete, Entry_number))
        but_update = tkinter.Button(self, text="Оновити", command=update)
        but_update.pack(side=tkinter.BOTTOM, fill=X)
        but_delete.pack(side=tkinter.BOTTOM, fill=X)
        Entry_number.pack(side=tkinter.BOTTOM, fill=X)
        label_number.pack(side=tkinter.BOTTOM, fill=X)


class Shop(tkinter.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_Shop()

        def init_Shop(self):
            con = sqlite3.connect('store.db')
            cur = con.cursor()
            self.title("Shop")
            self.iconbitmap(resource_path(r'./icon/shop.ico'))

            def View():
                for i in self.tree.get_children():
                    self.tree.delete(i)
                    self.tree.pack()
                history = cur.execute('Select * from shop').fetchall()
                for row in history:
                    self.tree.insert("", tkinter.END, values=row)
                    self.tree.pack()
            self.geometry(child_window())
            columns = ("ID", "names_id", "names", "amount", "price_non_PDW")
            self.tree = ttk.Treeview(self, columns=columns, show="headings",height=25)
            self.tree.heading("ID", text="ID")
            self.tree.heading("names_id", text="Назва товару")
            self.tree.heading("names", text="кількість товару")
            self.tree.heading("amount", text="Ціна")
            self.tree.heading("price_non_PDW", text="Вартість з ПДВ")
            
            self.tree.column("ID", width=110, anchor=tkinter.CENTER)
            self.tree.column("names_id", width=110, anchor=tkinter.CENTER)
            self.tree.column("names", width=100, anchor=tkinter.CENTER)
            self.tree.column("amount", width=80, anchor=tkinter.CENTER)
            self.tree.column("price_non_PDW", width=100, anchor=tkinter.CENTER)
            self.tree.pack()

            but_view = tkinter.Button(self, text="Подивитись в наявності", command=View)
            but_item_select = tkinter.Button(self, text="Оформлення покупки", command=Items)
            but_item_select.pack(side=tkinter.BOTTOM, fill=X)
            but_view.pack(side=tkinter.BOTTOM, fill=X)
            self.resizable(False, False)
            self.focus_set()
            self.grab_set()


class about_programs(tkinter.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_new_program()
        

    def init_new_program(self):
        self.iconbitmap(resource_path(r'./icon/shop.ico'))
        self.title("Про програму")
        self.geometry(child_window())
        self.resizable(FALSE, FALSE)
        self.grab_set()
        self.focus_set()
        label = Label(self, text="Про програму Equipment store 1.0 ", font=("Times, 18"), pady=100)
        label1 = Label(self, text="Дана програма є моделлю роботи файлової системи магазину побутової техніки. \n""Equipment store 1.0 був розроблений в рамках курсового проекту.", font='Times, 14', pady=100, anchor=tkinter.CENTER)
        label2 = Label(self, text="Розробник програми: \n""Гладких В.Д.", font='Times, 14', anchor=tkinter.SW)
        label.pack()
        label1.pack()
        label2.pack()


class Items(tkinter.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_ItemSelect()

    def init_ItemSelect(self):
        self.title("Оформлення покупки")
        self.geometry("400x220")
        self.iconbitmap(resource_path(r'./icon/shop.ico'))

        def Buy(id,amount):
            buy_id = int(id.get())
            buy_amount = int(amount.get())
            con = sqlite3.connect('store.db')
            cur = con.cursor()
            total_amount = cur.execute('SELECT amount FROM shop WHERE ID = ? ',(buy_id,)).fetchall()[0][0]
            if total_amount >= buy_amount:
                result = askyesno(title="Підтвердить покупку", message=f"Підтверджуете покупку товару за номером: {buy_id} у кількості: {buy_amount}?")
                if result:
                    cur.execute('UPDATE shop SET amount = ? WHERE ID = ?',(total_amount - buy_amount,buy_id,))
                    data = cur.execute('SELECT * FROM shop WHERE ID = ?', (buy_id,)).fetchall()[0]
                    price = cur.execute('SELECT price FROM shop WHERE ID = ?', (buy_id,)).fetchall()[0][0]
                    tmp = list(data)

                    tmp[2] = buy_amount
                    cur.execute(
                        'INSERT INTO history (names_id, names, amount, price_non_PDW, price_with_pdw, glob_price ) VALUES (?,?,?,?,?,?)',
                        (tmp + [int(buy_amount) * int(price.replace(' ', ''))]))
                    con.commit()
                    showinfo("Результат", "Операция пройшла")
                else:
                    showinfo("Результат", "Відміна")
            else:
                showerror(title="Помилка", message="Недостатньо у товару")

        self.entry_ID = tkinter.Entry(self)
        self.entry_ID.place(x=200, y=50)

        self.entry_amount = tkinter.Entry(self)
        self.entry_amount.place(x=200, y=80)

        label1_1 = Label(self, text="ID")
        label1_1.place(x=50, y=50)

        label1_2 = Label(self, text="Amount")
        label1_2.place(x=50, y=80)

        btn_cancel = tkinter.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_add = tkinter.Button(self, text='Добавить', command=partial(Buy, self.entry_ID, self.entry_amount))
        btn_add.place(x=220, y=170)

        self.focus_set()
        self.grab_set()

def shop():
    Shop()

def about():
    about_programs()

def root_Frame():
    w = 1024
    h = 770
    center = f"{w}x{h}+{(root.winfo_screenwidth() - w) // 2}+{(root.winfo_screenheight() - h) // 2}"
    return center

def child_window():
    w = 900
    h = 720
    center = f"{w}x{h}+{(root.winfo_screenwidth() - w) // 2}+{(root.winfo_screenheight() - h) // 2}"
    return center

def on_closing():
    if messagebox.askokcancel("Quit", "Ви хочете вийти?"):
        root.destroy()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    app.pack()
    root.title("Магазин побутової техніки")
    icon = root.iconbitmap(resource_path(r'./icon/shop.ico'))
    root.geometry(root_Frame())
    root.resizable(FALSE, FALSE)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()