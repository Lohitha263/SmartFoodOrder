from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from PIL import ImageTk, Image
from tkinter import StringVar, OptionMenu
import sqlite3
from twilio.rest import Client

root = Tk()
root.geometry("2000x2000")
class Home():
    def _init_(self, root):
        self.root = root
        self.root.title("Order Food")
        
        self.back_hovered=False
        self.cart_items = []
        
        self.initialize_database()
        self.initialize_pastries_database()
        
        
        self.bg_img = Image.open('art.png')
        self.bg_img = self.bg_img.resize((650,450))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_lbl = Label(root, image= self.bg_img)
        self.bg_lbl.place(x = 0, y = 0)
             
        self.home_title = Label(root, text= 'CAFETERIA', font = ('Courier New', 15, 'bold'),fg='white',bg='black',bd='12',relief='ridge')
        self.home_title.pack()
        self.b_btn = Button(root, text = 'PUFFS', font=('Courier New', 14, 'bold'),fg='white',bg='black',command= self.enter_puff_page,width=9)
        self.b_btn.place(x= 60, y = 100)
        self.enter_pa = Button(root, text= 'BEVERAGES', font= ('Courier New', 14,'bold'),fg='white',bg='black',command=self.enter_beverage_page,width=9)
        self.enter_pa.place(x = 310, y = 200)
        self.enter_pi= Button(root, text= 'PASTRY', font= ('Courier New', 14,'bold'),fg='white',bg='black',command=self.enter_past_page,width=9)
        self.enter_pi.place(x = 310, y = 100)
        self.enter_pu = Button(root, text= 'PIZZAS', font= ('Courier New', 14,'bold'),fg='white',bg='black',command=self.enter_pizza_page,width=9)
        self.enter_pu.place(x = 60, y = 200)
        
        self.e1=None
        self.e2=None
        self.e3=None
        self.e4=None
        self.e5=None
        self.e6=None
        self.e7=None
        self.e21=None
        self.e22=None
        self.e23=None
        self.e24=None
        self.e25=None
        self.e11=None
        self.e12=None
        self.e13=None
        self.e14=None
        self.e15=None
        self.e16=None
        self.e17=None
        self.e31=None
        self.e32=None 
        self.e33=None
        self.e34=None
        self.e35=None
        self.e36=None
        self.e37=None
       
        
    
    def initialize_database(self):
    # Connect to SQLite database
        self.conn = sqlite3.connect('beverages.db')
        self.cursor = self.conn.cursor()

        try:
        # Drop the beverages table if it exists
            self.cursor.execute('DROP TABLE IF EXISTS beverages')
            self.conn.commit()

        # Create a new table for beverages
            self.cursor.execute('''
            CREATE TABLE beverages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                beverage_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                dropdown_selection TEXT NOT NULL
            )
        ''')
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
            self.conn.rollback()

        finally:
            self.conn.close()

    
    def enter_beverage_page(self):
        self.home_title.destroy()
        self.b_btn.destroy()
        self.enter_pa.destroy()
        self.enter_pi.destroy()
        self.enter_pu .destroy()
        root = self.root
        self.enter_pin_page_title = Label(root, text= 'BEVERAGES', font=('Courier New',15,'bold'))
        self.enter_pin_page_title.pack(fill = 'x')
        self.pin_label1 = Label(root, text= "No.of items", font=('Courier New', 7, 'bold'))
        self.pin_label1.place(x = 335, y = 33)

        self.pin_label1 = Label(root, text= "Sprite", font=('Courier New', 13, 'bold'))
        self.pin_label1.place(x = 40, y = 50)
        self.dropdown1 = ttk.Combobox(root, values=["Rs.20", "Rs.50","Rs.100"], state="readonly",width=15)
        self.dropdown1.set("select")
        self.dropdown1.place(x=200, y=50)
        self.e1=Entry(root,width=5)
        self.e1.place(x=350,y=50)

        self.pin_label2 = Label(root, text= "Coke", font=('Courier New', 13, 'bold'))
        self.pin_label2.place(x = 40, y = 75)
        self.dropdown2 = ttk.Combobox(root, values=["Rs.20", "Rs.50","Rs.100"], state="readonly",width=15)
        self.dropdown2.set("select")
        self.dropdown2.place(x=200, y=75)
        self.e3=Entry(root,width=5)
        self.e3.place(x=350,y=75)

        self.pin_label3 = Label(root, text= "Mazaa", font=('Courier New', 13, 'bold'))
        self.pin_label3.place(x = 40, y = 100)
        self.dropdown3 = ttk.Combobox(root, values=["Rs.20", "Rs.50","Rs.100"], state="readonly",width=15)
        self.dropdown3.set("select")
        self.dropdown3.place(x=200, y=100)
        self.e4=Entry(root,width=5)
        self.e4.place(x=350,y=100)

        self.pin_label4 = Label(root, text= "ThumsUp", font=('Courier New', 13, 'bold'))
        self.pin_label4.place(x = 40, y = 125)
        self.dropdown4 = ttk.Combobox(root, values=["Rs.20", "Rs.50","Rs.100"], state="readonly",width=15)
        self.dropdown4.set("select")
        self.dropdown4.place(x=200, y=125)
        self.e5=Entry(root,width=5)
        self.e5.place(x=350,y=125)

        self.pin_label5 = Label(root, text= "Coffee", font=('Courier New', 13, 'bold'))
        self.pin_label5.place(x = 40, y = 150)
        self.dropdown5 = ttk.Combobox(root, values=["Rs.120"], state="readonly",width=15)
        self.dropdown5.set("Rs.120")
        self.dropdown5.place(x=200, y=150) 
        self.e2=Entry(root,width=5)
        self.e2.place(x=350,y=150)

        self.pin_label6 = Label(root, text= "Cold Coffee",  font=('Courier New', 13, 'bold'))
        self.pin_label6.place(x = 40, y = 175)
        self.dropdown6 = ttk.Combobox(root, values=["Rs.150"], state="readonly",width=15)
        self.dropdown6.set("Rs.150")
        self.dropdown6.place(x=200, y=175) 
        self.e6=Entry(root,width=5)
        self.e6.place(x=350,y=175)

        self.pin_label7=Label(root, text= "Black Coffee", font=('Courier New', 13, 'bold'))
        self.pin_label7.place(x = 40, y = 200)
        self.dropdown7 = ttk.Combobox(root, values=["Rs.100"], state="readonly",width=15)
        self.dropdown7.set("Rs.100")
        self.dropdown7.place(x=200, y=200) 
        self.e7=Entry(root,width=5) 
        self.e7.place(x=350,y=200)

        self.submit_btn = Button(root, text='CART', font=('Courier New',12, 'bold'), bd = 4,command= self.show_cart_window)
        self.submit_btn.place(x = 350, y =  240)
        self.bck_btn = Button(root, text = 'Main Menu', font=('Courier New', 12,'bold'), bd = 4, width= 10, command= self.back_to_home1)
        self.bck_btn.place(x = 40, y = 240)
        self.save_btn = Button(root, text='Save', font=('Courier New', 12, 'bold'), bd=4, command=self.save_beverages)
        self.save_btn.place(x=200, y=240)
        self.bck_btn.bind("<Enter>",self.check_back_hover)

    def enter_past_page(self):
        self.home_title.destroy()
        self.b_btn.destroy()
        self.enter_pa.destroy()
        self.enter_pi.destroy()
        self.enter_pu .destroy()
        root = self.root
        self.enter_pin_page_title = Label(root, text= 'PASTRY', font=('Courier New',15,'bold'))
        self.enter_pin_page_title.pack(fill = 'x')
        self.pin_label1 = Label(root, text= "Red velvet Pastry", font=('Courier New', 13, 'bold'))
        self.pin_label1.place(x = 40, y = 50)
        self.pin_label1 = Label(root, text= "No.of items", font=('Courier New', 7, 'bold'))
        self.pin_label1.place(x = 360, y = 30)
        self.dropdown11 = ttk.Combobox(root, values=["Rs.60"], state="readonly",width=15)
        self.dropdown11.set("Rs.60")
        self.dropdown11.place(x=240, y=50) 
        self.e11=Entry(root,width=5)
        self.e11.place(x=370,y=50)

        self.pin_label2 = Label(root, text= "Pineapple Pastry", font=('Courier New', 13, 'bold'))
        self.pin_label2.place(x = 40, y = 75)
        self.dropdown12 = ttk.Combobox(root, values=["Rs.65"], state="readonly",width=15)
        self.dropdown12.set("Rs.65")
        self.dropdown12.place(x=240, y=75) 
        self.e12=Entry(root,width=5)
        self.e12.place(x=370,y=75)

        self.pin_label3 = Label(root, text= "Oreo Pastry", font=('Courier New', 13, 'bold'))
        self.pin_label3.place(x = 40, y = 100)
        self.dropdown13 = ttk.Combobox(root, values=["Rs.80"], state="readonly",width=15)
        self.dropdown13.set("Rs.80")
        self.dropdown13.place(x=240, y=100) 
        self.e13=Entry(root,width=5)
        self.e13.place(x=370,y=100)

        self.pin_label4 = Label(root, text= "Chocolate Pastry", font=('Courier New', 13, 'bold'))
        self.pin_label4.place(x = 40, y = 125)
        self.dropdown14= ttk.Combobox(root, values=["Rs.75"], state="readonly",width=15)
        self.dropdown14.set("Rs.75")
        self.dropdown14.place(x=240, y=125) 
        self.e14=Entry(root,width=5)
        self.e14.place(x=370,y=125)

        self.pin_label5 = Label(root, text= "Strawberry Pastry", font=('Courier New', 13, 'bold'))
        self.pin_label5.place(x = 40, y = 150)
        self.dropdown15= ttk.Combobox(root, values=["Rs.75"], state="readonly",width=15)
        self.dropdown15.set("Rs.75")
        self.dropdown15.place(x=240, y=150) 
        self.e15=Entry(root,width=5)
        self.e15.place(x=370,y=150)

        self.pin_label6 = Label(root, text= "Black Forest Pastry", font=('Courier New', 13, 'bold'))
        self.pin_label6.place(x = 40, y = 175)
        self.dropdown16 = ttk.Combobox(root, values=["Rs.90"], state="readonly",width=15)
        self.dropdown16.set("Rs.90")
        self.dropdown16.place(x=240, y=175) 
        self.e16=Entry(root,width=5)
        self.e16.place(x=370,y=175)

        self.pin_label7=Label(root, text= "Fruit Pastry", font=('Courier New', 13, 'bold'))
        self.pin_label7.place(x = 40, y = 200)
        self.dropdown17 = ttk.Combobox(root, values=["Rs.60"], state="readonly",width=15)
        self.dropdown17.set("Rs.60")
        self.dropdown17.place(x=240, y=200) 
        self.e17=Entry(root,width=5)
        self.e17.place(x=370,y=200)

        self.save_btn = Button(root, text='Save', font=('Courier New', 12, 'bold'), bd=4, command=self.save_pastries)
        self.save_btn.place(x=200, y=240)

        
        self.submit_btn = Button(root, text='CART', font=('Courier New',12, 'bold'), bd = 4,command= self.show_cart_window)
        self.submit_btn.place(x = 350, y =  240)

        self.bck_btn = Button(root, text = 'Main Menu', font=('Courier New', 12,'bold'), bd = 4, width=10, command= self.back_to_home2)
        self.bck_btn.place(x = 40, y = 240)
        self.bck_btn.bind("<Enter>",self.check_back_hover)

  

    def clear_database(db_file):
        try:
        # Connect to the database
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

        # Get the list of table names in the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

        # Clear data from each table in the database
            for table in tables:
                table_name = table[0]
                cursor.execute(f"DELETE FROM {table_name};")

        # Commit the changes
            conn.commit()

            print(f"Data cleared from {db_file}.")

        # Close the database connection
            conn.close()

        except sqlite3.Error as e:
            print(f"Error occurred while clearing data from {db_file}: {e}") 

        finally:
            # Close the database connection in the finally block
            if conn:
                conn.close()
        

# Clear data from each database
    clear_database("beverages.db")
    clear_database("puffs.db")
    clear_database("pastries.db")
    clear_database("pizzas.db")

    def enter_puff_page(self):
        
        self.home_title.destroy()
        self.b_btn.destroy()
        self.enter_pa.destroy()
        self.enter_pi.destroy()
        self.enter_pu .destroy()
        
        root = self.root
        self.enter_pin_page_title = Label(root, text= 'PUFF', font=('Courier New',15,'bold'))
        self.enter_pin_page_title.pack(fill = 'x')
        self.pin_label1 = Label(root, text= "No.of items", font=('Courier New', 8, 'bold'))
        self.pin_label1.place(x = 340, y = 30)        

        self.pin_label1 = Label(root, text= "CHICKEN PUFF", font=('Courier New', 12, 'bold'))
        self.pin_label1.place(x = 40, y = 50)
        self.dropdown21 = ttk.Combobox(root, values=["Rs.35"], state="readonly",width=15)
        self.dropdown21.set("Rs.35")
        self.dropdown21.place(x=200, y=50) 
        self.e21=Entry(root,width=5)
        self.e21.place(x=370,y=50)

        self.pin_label2 = Label(root, text= "EGG PUFF", font=('Courier New', 12, 'bold'))
        self.pin_label2.place(x = 40, y = 75)
        self.dropdown25 = ttk.Combobox(root, values=["Rs.25"], state="readonly",width=15)
        self.dropdown25.set("Rs.25")
        self.dropdown25.place(x=200, y=75) 
        self.e25=Entry(root,width=5)
        self.e25.place(x=370,y=75)

        self.pin_label3 = Label(root, text= "PANEER PUFF", font=('Courier New', 12, 'bold'))
        self.pin_label3.place(x = 40, y = 100)
        self.dropdown22 = ttk.Combobox(root, values=["Rs.35"], state="readonly",width=15)
        self.dropdown22.set("Rs.30")
        self.dropdown22.place(x=200, y=100) 
        self.e22=Entry(root,width=5)
        self.e22.place(x=370,y=100)

        self.pin_label4 = Label(root, text= "MEAT PUFF", font=('Courier New', 12, 'bold'))
        self.pin_label4.place(x = 40, y = 125)
        self.dropdown23 = ttk.Combobox(root, values=["Rs.45"], state="readonly",width=15)
        self.dropdown23.set("Rs.45")
        self.dropdown23.place(x=200, y=125) 
        self.e23=Entry(root,width=5)
        self.e23.place(x=370,y=125)

        self.pin_label5 = Label(root, text= "MUSHROOM PUFF", font=('Courier New', 12, 'bold'))
        self.pin_label5.place(x = 40, y = 150)
        self.dropdown24 = ttk.Combobox(root, values=["120Rs"], state="readonly",width=15)
        self.dropdown24.set("Rs.40")
        self.dropdown24.place(x=200, y=150) 
        self.e24=Entry(root,width=5)
        self.e24.place(x=370,y=150)

        self.save_btn = Button(root, text='Save', font=('Courier New', 12, 'bold'), bd=4, command=self.save_puffs)
        self.save_btn.place(x=200, y=240)
        
        self.submit_btn = Button(root, text='CART', font=('Courier New',12, 'bold'), bd = 4,command= self.show_cart_window)
        self.submit_btn.place(x = 350, y =  240)

        self.bck_btn = Button(root, text = 'Main Menu', font=('Courier New', 12,'bold'), bd = 4, width= 10, command= self.back_to_home4)
        self.bck_btn.place(x = 40, y = 240)
        self.bck_btn.bind("<Enter>",self.check_back_hover)

    def enter_pizza_page(self):
        
        self.home_title.destroy()
        self.b_btn.destroy()
        self.enter_pa.destroy()
        self.enter_pi.destroy()
        self.enter_pu .destroy()
        
        root = self.root
        self.enter_pin_page_title = Label(root, text= 'Pizzas', font=('Courier New',15,'bold'))
        self.enter_pin_page_title.pack(fill = 'x')
        
        self.pin_label1 = Label(root, text= "No.of items", font=('Courier New', 7, 'bold'))
        self.pin_label1.place(x = 335, y = 30)

        self.pin_label1 = Label(root, text= "CHEESE PIZZA", font=('Courier New', 12, 'bold'))
        self.pin_label1.place(x = 50, y = 45)
        self.dropdown31 = ttk.Combobox(root, values=["Small-Rs.120", "Medium-Rs.170","Large-Rs.220"], state="readonly",width=15)
        self.dropdown31.set("select")
        self.dropdown31.place(x=200, y=45)
        self.e31=Entry(root,width=5)
        self.e31.place(x=350,y=45)

        self.pin_label2 = Label(root, text= "VEGGIE PIZZA", font=('Courier New', 12, 'bold'))
        self.pin_label2.place(x = 50, y = 75)
        self.dropdown32 = ttk.Combobox(root, values=["Small-Rs.120", "Medium-Rs.170","Large-Rs.220"], state="readonly",width=15)
        self.dropdown32.set("select")
        self.dropdown32.place(x=200, y=75)
        self.e32=Entry(root,width=5)
        self.e32.place(x=350,y=75)

        self.pin_label3 = Label(root, text= "CHICKEN PIZZA", font=('Courier New', 12, 'bold'))
        self.pin_label3.place(x = 50, y = 105)
        self.dropdown33 = ttk.Combobox(root, values=["Small-Rs.120", "Medium-Rs.170","Large-Rs.220"], state="readonly",width=15)
        self.dropdown33.set("select")
        self.dropdown33.place(x=200, y=105)
        self.e33=Entry(root,width=5)
        self.e33.place(x=350,y=105)

        self.pin_label4 = Label(root, text= "MEAT PIZZA", font=('Courier New', 12, 'bold'))
        self.pin_label4.place(x = 50, y = 135)
        self.dropdown34 = ttk.Combobox(root, values=["Small-Rs.120", "Medium-Rs.170","Large-Rs.220"], state="readonly",width=15)
        self.dropdown34.set("select")
        self.dropdown34.place(x=200, y=135)
        self.e34=Entry(root,width=5)
        self.e34.place(x=350,y=135)

        self.pin_label5 = Label(root, text= "BBQ PIZZA", font=('Courier New', 12, 'bold'))
        self.pin_label5.place(x = 50, y = 165)
        self.dropdown35 = ttk.Combobox(root, values=["Small-Rs.120", "Medium-Rs.170","Large-Rs.220"], state="readonly",width=15)
        self.dropdown35.set("select")
        self.dropdown35.place(x=200, y=165)
        self.e35=Entry(root,width=5)
        self.e35.place(x=350,y=165)

        self.pin_label6 = Label(root, text= "HAWAIIAN PIZZA", font=('Courier New', 12, 'bold'))
        self.pin_label6.place(x = 50, y = 195)
        self.dropdown36 = ttk.Combobox(root, values=["Small-Rs.120", "Medium-Rs.170","Large-Rs.220"], state="readonly",width=15)
        self.dropdown36.set("select")
        self.dropdown36.place(x=200, y=195)
        self.e36=Entry(root,width=5)
        self.e36.place(x=350,y=195)
        
        self.pin_label7=Label(root, text= "PANEER PIZZA", font=('Courier New', 12, 'bold'))
        self.pin_label7.place(x = 50, y = 225)
        self.dropdown37 = ttk.Combobox(root, values=["Small-Rs.120", "Medium-Rs.170","Large-Rs.220"], state="readonly",width=15)
        self.dropdown37.set("select")
        self.dropdown37.place(x=200, y=225)
        self.e37=Entry(root,width=5)
        self.e37.place(x=350,y=225)

        self.save_btn = Button(root, text='Save', font=('Courier New', 12, 'bold'), bd=4, command=self.save_pizzas)
        self.save_btn.place(x=200, y=250)
 
        self.submit_btn = Button(root, text='CART', font=('Courier New',12, 'bold'), bd = 4,command= self.show_cart_window)
        self.submit_btn.place(x = 350, y =  250)

        self.bck_btn = Button(root, text = 'Main Menu', font=('Courier New', 12,'bold'), bd = 4, width= 10, command= self.back_to_home3)
        self.bck_btn.place(x = 50, y = 250)
        self.bck_btn.bind("<Enter>",self.check_back_hover)
    def show_home_window(self):
    # Destroy the cart frame to hide it
       
        if self.cart_frame:
            self.cart_frame.destroy()

    def show_cart_window(self):
        total_quantity = 0
        items = []

    # Retrieve data from the databases
        data = self.retrieve_data_from_databases()
    
    # Print the retrieved data for debugging
        print("Retrieved Data:", data)
        self.enter_pin_page_title.destroy()
    
        beverages_data = data.get("Beverages", [])
        puffs_data = data.get("Puffs", [])
        pastries_data = data.get("Pastries", [])
        pizzas_data = data.get("Pizzas", [])

        items_list = [
        ("Beverage", beverages_data),
        ("Puff", puffs_data),
        ("Pastry", pastries_data),
        ("Pizza", pizzas_data)
    ]

        self.cart_frame = tk.Frame(self.root)
        self.cart_frame.pack(fill=tk.BOTH, expand=True)

        cart_label = tk.Label(self.cart_frame, text="Items in Cart:", font=('Courier New', 15, 'bold'))
        cart_label.pack()
    
        btn_back = tk.Button(self.cart_frame, text="Back", font=('Courier New', 15, 'bold'), command=self.show_home_window)
        btn_back.place(x=110,y=220)

        btn_place_order = tk.Button(self.cart_frame, text="Confirm", font=('Courier New', 15, 'bold'), command=self.open_order_page)
        btn_place_order.place(x=260,y=220)
        for category, entries in items_list:
            for entry in entries:
                quantity = entry.get("quantity", 0)
                name = entry.get("name", "")
                if quantity > 0:
                    items.append(f"{quantity} {name} ({category})")
                    total_quantity += quantity
                    print(f"Processing: {quantity} {name} ({category})")

        if items:
            for item in items:
                item_label = tk.Label(self.cart_frame, text=item, font=('Courier New', 8))
                item_label.pack()
        else:
            empty_label = tk.Label(self.cart_frame, text="No items saved in the cart.", font=('Courier New', 8))
            empty_label.pack()

        total_label = tk.Label(self.cart_frame, text=f"Total Quantity: {total_quantity}", font=('Courier New', 8))
        total_label.pack()

        self.delete_items_from_databases()
    def clear_cart(self):
    # Destroy all widgets in the cart frame
        for widget in self.cart_frame.winfo_children():
            widget.destroy()
    def open_order_page(self):
        # Create a new frame for the Order page
        self.order_frame = tk.Frame(self.root)
        self.order_frame.pack(fill=tk.BOTH, expand=True)

        # Add widgets to the Order page
        order_label = tk.Label(self.order_frame, text="You're almost there!", font=('Courier New', 10, 'bold'))
        order_label.place(x=180, y=0)

        name_label = tk.Label(self.order_frame, text="Name:", font=('Courier New', 12))
        name_label.place(x=180, y=80)
        self.name_entry = tk.Entry(self.order_frame)
        self.name_entry.place(x=200, y=100)

        phone_label = tk.Label(self.order_frame, text="Phone Number:", font=('Courier New', 12))
        phone_label.place(x=180, y=120)
        self.phone_entry = tk.Entry(self.order_frame)
        self.phone_entry.place(x=200, y=140)

        # Add a button to close the Order page
        close_button = tk.Button(self.order_frame, text="Order", font=('Courier New', 15, 'bold'), command=self.place_orde)
        close_button.place(x=200, y=210)

        # You may want to destroy the cart frame here
        if self.cart_frame:
            self.cart_frame.destroy()
    def place_orde(self):
        messagebox.showinfo("Order Placed", "Order placed successfully!")
    def place_order(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        # Validate name (only characters allowed)
        if not name.isalpha():
            messagebox.showerror("Error", "Name should contain only alphabetic characters.")
            return

        # Validate phone number (only ten-digit integer allowed)
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Phone number should be a ten-digit integer.")
            return
           
        # Validate name (only characters allowed)
        if not name.isalpha():
            messagebox.showerror("Error", "Name should contain only alphabetic characters.")
            return

        # Validate phone number (only ten-digit integer allowed)
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Phone number should be a ten-digit integer.")
            return

        # Store the name and phone number for later use
        self.order_name = name
        self.order_phone = phone

        # Fetch data from pastries database
        conn_pastries = sqlite3.connect('pastries.db')
        cursor_pastries = conn_pastries.cursor()
        cursor_pastries.execute("SELECT * FROM pastries")
        pastries_data = cursor_pastries.fetchall()
        conn_pastries.close()

        # Fetch data from beverages database
        conn_beverages = sqlite3.connect('beverages.db')
        cursor_beverages = conn_beverages.cursor()
        cursor_beverages.execute("SELECT * FROM beverages")
        beverages_data = cursor_beverages.fetchall()
        conn_beverages.close()

        # Fetch data from puffs database
        conn_puffs = sqlite3.connect('puffs.db')
        cursor_puffs = conn_puffs.cursor()
        cursor_puffs.execute("SELECT * FROM puffs")
        puffs_data = cursor_puffs.fetchall()
        conn_puffs.close()

        # Fetch data from pizzas database
        conn_pizzas = sqlite3.connect('pizzas.db')
        cursor_pizzas = conn_pizzas.cursor()
        cursor_pizzas.execute("SELECT * FROM pizzas")
        pizzas_data = cursor_pizzas.fetchall()
        conn_pizzas.close()

        # Format the data into strings
        print("Pastries data fetched:", pastries_data)

# Format the data into strings
        pastries_str = "\n".join([f"{row[1]}: {row[2]}" for row in pastries_data])

# Debugging: Print pastries_str to verify formatted string
        print("Pastries string:", pastries_str)
        beverages_str = "\n".join([f"{row[1]}: {row[2]}" for row in beverages_data])
        puffs_str = "\n".join([f"{row[1]}: {row[2]}" for row in puffs_data])
        pizzas_str = "\n".join([f"{row[1]}: {row[2]}" for row in pizzas_data])

        # Send the SMS message
        message = self.client.messages.create(
        body=f'Order received.\n\nName: {self.order_name}\nPhone: {self.order_phone}\n\nPastries:\n{pastries_str}\n\nBeverages:\n{beverages_str}\n\nPuffs:\n{puffs_str}\n\nPizzas:\n{pizzas_str}',
            from_='+14402188001',
            to='+Your_Phone_number'
        )
        messagebox.showinfo("Order Placed", "Order placed successfully!")
        



# Your Twilio account SID and auth token
    
# Example usage


    # Gmail SMTP server configuration
       
    def retrieve_data_from_databases(self):
        database_files = {
            "Beverages": "beverages.db",
            "Puffs": "puffs.db",
            "Pastries": "pastries.db",
            "Pizzas": "pizzas.db"
        }
        data = {}

        for category, db_file in database_files.items():
            try:
                conn = sqlite3.connect(db_file)
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {category.lower()}")
                rows = cursor.fetchall()
                items = [{"name": row[1], "quantity": row[2]} for row in rows]
                data[category] = items
                conn.close()
            except sqlite3.Error as e:
                print(f"Error occurred while retrieving data from {db_file}: {e}")

        return data

    def delete_items_from_databases(self):
        data = self.retrieve_data_from_databases()
        beverages_data = data.get("Beverages", [])
        puffs_data = data.get("Puffs", [])
        pastries_data = data.get("Pastries", [])
        pizzas_data = data.get("Pizzas", [])
        self.delete_items_from_database("beverages.db", "Beverages", beverages_data)
        self.delete_items_from_database("puffs.db", "Puffs", puffs_data)
        self.delete_items_from_database("pastries.db", "Pastries", pastries_data)
        self.delete_items_from_database("pizzas.db", "Pizzas", pizzas_data)

    def delete_items_from_database(self, db_file, table_name, items):
        try:
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            for item in items:
                name = item["name"]
                quantity = item["quantity"]
                if quantity > 0:
                # Corrected the query to use the correct column name based on the table structure
                    cursor.execute(f"UPDATE {table_name.lower()} SET quantity = quantity - ? WHERE pastry_name = ?", (quantity, name))

            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print(f"Error occurred while deleting items from {db_file}: {e}")
    def test_add_items_to_cart(self):
    # Manually create some test items
        test_items = [
        {"category": "Beverages", "name": "Coffee", "quantity": 2},
        {"category": "Pizza", "name": "Margherita", "quantity": 1}
    ]
    
    # Add test items to the cart
        for item in test_items:
            category = item["category"]
            name = item["name"]
            quantity = item["quantity"]
        
        # Create a mock entry similar to the database entries
            entry = {"name": name, "quantity": quantity}
        
        # Add the mock entry to the corresponding category list
            if category == "Beverages":
                self.beverages_data.append(entry)
            elif category == "Pizza":
                self.pizzas_data.append(entry)
    
    # Display the cart window
        self.show_cart_window()
 # Assuming you're using Tkinter for GUI
     # Assuming you're using Tkinter for GUI

    def save_beverages(self):  # Assuming this function is within a class
        beverages = {
        "Sprite": self.e1.get(),
        "Coke": self.e3.get(),
        "Mazaa": self.e4.get(),
        "Thumsup": self.e5.get(),
        "Cold coffee": self.e6.get(),
        "Coffee": self.e2.get(),
        "Black coffee": self.e7.get()
    }
       
        items = [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7]
        for i, entry in enumerate(items, start=1):
            if entry.get().isdigit() and int(entry.get()) > 12:
                messagebox.showerror("Error", f"Item {i} quantity cannot exceed 12.")
                return
    # Your existing code to save the beverages goes here


        valid_beverages = {beverage: quantity for beverage, quantity in beverages.items() if quantity.isdigit() and int(quantity) > 0}

        if valid_beverages:
            try:
                conn = sqlite3.connect("beverages.db")
                cursor = conn.cursor()

            # Begin a transaction
                cursor.execute("BEGIN")

            # Drop table if it exists
                cursor.execute("DROP TABLE IF EXISTS beverages")

            # Create table
                cursor.execute('''
                CREATE TABLE beverages (
                    id INTEGER PRIMARY KEY,
                    beverage_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL
                )
            ''')

            # Insert beverage quantities
                for beverage, quantity in valid_beverages.items():
                    if not beverage.strip() or not quantity.strip() or not quantity.isdigit() or int(quantity) <= 0:
                        print(f"Invalid entry for {beverage}: {quantity}")
                        continue
                    cursor.execute("INSERT INTO beverages (beverage_name, quantity) VALUES (?, ?)", (beverage, quantity))

            # Commit the transaction
                cursor.execute("COMMIT")

                conn.close()
                messagebox.showinfo("Beverages Saved", "Beverages have been saved successfully!")
            except sqlite3.Error as e:
                print(f"Error occurred while connecting to the database: {e}")
                messagebox.showerror("Database Error", f"Error occurred while saving beverages: {e}")
        else:
            messagebox.showwarning("No Valid Beverages", "Please enter valid quantities (greater than 0) for beverages before saving.")

    

    
                
    def initialize_pastries_database(self):
        
        try:
            conn = sqlite3.connect('pastries.db')
            cursor = conn.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS pastries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pastry_name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
            ''')

            conn.commit()

        except sqlite3.Error as e:
            print(f"Error occurred while creating table: {e}")
            conn.rollback()

        finally:
            conn.close()

    


   
    def save_puffs(self): 
        puffs = {
        "CHICKEN PUFF": self.e21.get(),
        "PANEER PUFF": self.e22.get(),
        "MEAT PUFF": self.e23.get(),
        "MUSHROOM PUFF": self.e24.get(),
        "EGG PUFF": self.e25.get()
    }
        
        items = [self.e21, self.e22, self.e23, self.e24, self.e25]
        for i, entry in enumerate(items, start=1):
            if entry.get().isdigit() and int(entry.get()) > 12:
                messagebox.showerror("Error", f"Item {i} quantity cannot exceed 12.")
                return

    # Filter out invalid entries: either they are not numbers or they are <= 0
        valid_puffs = {puff: quantity for puff, quantity in puffs.items() if quantity.isdigit() and int(quantity) > 0}

        if valid_puffs:
        # Convert the dictionary to a list of tuples
            data_to_insert = [(puff, int(quantity)) for puff, quantity in valid_puffs.items()]

            try:
            # Connect to SQLite database
                self.conn = sqlite3.connect('puffs.db')
                self.cursor = self.conn.cursor()

            # Insert valid puff quantities into the database
                self.cursor.executemany('INSERT INTO puffs (puff_name, quantity) VALUES (?, ?)', data_to_insert)
                self.conn.commit()

            # Convert the dictionary to a string format for display
                puffs_str = "\n".join([f"{puff}: {quantity}" for puff, quantity in valid_puffs.items()])

            # Display the saved puffs in a message dialog
                messagebox.showinfo("Puffs Saved", f"Puffs have been saved successfully!\n\n{puffs_str}")

            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error occurred while saving data: {e}")

            finally:
                self.conn.close()

        else:
            messagebox.showwarning("No Valid Puffs", "Please enter valid quantities (greater than 0) for puffs before saving.")
        def initialize_pastries_database():
            try:
            # Connect to SQLite database
                conn = sqlite3.connect('pastries.db')
                cursor = conn.cursor()

        # Create a table for pastries if it doesn't exist
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS pastries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pastry_name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')

                conn.commit()

            except sqlite3.Error as e:
                print(f"Error occurred while creating table: {e}")
                conn.rollback()

            finally:
                conn.close()

    def save_pastries(self):
        pastries = {
        "Red Velvet Pastry": self.e11.get(),
        "Pineapple Pastry": self.e12.get(),
        "Oreo Pastry": self.e13.get(),
        "Chocolate Pastry": self.e14.get(),
        "Strawberry Pastry": self.e15.get(),
        "Black Forest Pastry": self.e16.get(),
        "Fruit Pastry": self.e17.get()
    }
        items = [self.e11, self.e12, self.e13, self.e14, self.e15, self.e16, self.e17]
        for i, entry in enumerate(items, start=1):
            if entry.get().isdigit() and int(entry.get()) > 12:
                messagebox.showerror("Error", f"Item {i} quantity cannot exceed 12.")
                return

        valid_pastries = {pastry: quantity for pastry, quantity in pastries.items() if quantity.isdigit() and int(quantity) > 0}

        if valid_pastries:
            data_to_insert = [(pastry, int(quantity)) for pastry, quantity in valid_pastries.items()]

            try:
                conn = sqlite3.connect('pastries.db')
                cursor = conn.cursor()

                cursor.executemany('INSERT INTO pastries (pastry_name, quantity) VALUES (?, ?)', data_to_insert)
                conn.commit()

                pastries_str = "\n".join([f"{pastry}: {quantity}" for pastry, quantity in valid_pastries.items()])
                messagebox.showinfo("Pastries Saved", f"Pastries have been saved successfully!\n\n{pastries_str}")

            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error occurred while saving data: {e}")

            finally:
                conn.close()

        else:
            messagebox.showwarning("No Valid Pastries", "Please enter valid quantities (greater than 0) for pastries before saving.")
    
   
    

    def save_pizzas(self):
        pizzas = {
            "CHEESE PIZZA": self.e31.get(),
            "VEGGIE PIZZA": self.e32.get(),
            "CHICKEN PIZZA": self.e33.get(),
            "MEAT PIZZA": self.e34.get(),
            "BBQ PIZZA": self.e35.get(),
            "HAWAIIAN PIZZA": self.e36.get(),
            "PANEER PIZZA": self.e37.get()
        }
        
        items = [self.e31, self.e32, self.e33, self.e34, self.e35, self.e36, self.e37]
        for i, entry in enumerate(items, start=1):
            if entry.get().isdigit() and int(entry.get()) > 12:
                messagebox.showerror("Error", f"Item {i} quantity cannot exceed 12.")
                return

        valid_pizzas = {pizza: quantity for pizza, quantity in pizzas.items() if quantity.isdigit() and int(quantity) > 0}

        if valid_pizzas:
            try:
                conn = sqlite3.connect("pizzas.db")
                cursor = conn.cursor()

                # Create table if not exists
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS pizzas (
                    id INTEGER PRIMARY KEY,
                    pizza_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL
                )
                ''')

                # Insert pizza quantities
                for pizza, quantity in valid_pizzas.items():
                    cursor.execute("INSERT INTO pizzas (pizza_name, quantity) VALUES (?, ?)", (pizza, quantity))

                conn.commit()
                messagebox.showinfo("Pizzas Saved", "Pizzas have been saved successfully!")
                conn.close()
            except sqlite3.Error as e:
                print(f"Error occurred while connecting to the database: {e}")
                messagebox.showerror("Database Error", f"Error occurred while saving pizzas: {e}")
        else:
            messagebox.showwarning("No Valid Pizzas", "Please enter valid quantities (greater than 0) for pizzas before saving.")

        
    def check_back_hover(self, event):
        """Check if the BACK button is hovered over and display a message if it's the first time."""
        if not self.back_hovered:  # Only show if not shown before
            messagebox.showinfo("Reminder", "Make sure you saved your order!")
            self.back_hovered = True  # Update the flag
    
    
    def back_to_home1(self):
        self.enter_pin_page_title.destroy()
        self.pin_label1.destroy()
        self.pin_label2.destroy()
        self.pin_label3.destroy()
        self.pin_label4.destroy()
        self.pin_label5.destroy()
        self.pin_label6.destroy()
        self.pin_label7.destroy()
        self.pin_label7.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        self.e4.destroy()
        self.e5.destroy()
        self.e6.destroy()
        self.e7.destroy()
        self.submit_btn.destroy()
        self.bck_btn.destroy()
        home = Home(root)
    def back_to_home2(self):
        self.enter_pin_page_title.destroy()
        self.pin_label1.destroy()
        self.pin_label2.destroy()
        self.pin_label3.destroy()
        self.pin_label4.destroy()
        self.pin_label5.destroy()
        self.pin_label6.destroy()
        self.pin_label7.destroy()
        self.e11.destroy()
        self.e12.destroy()
        self.e13.destroy()
        self.e14.destroy()
        self.e15.destroy()
        self.e16.destroy()
        self.e17.destroy()
        self.submit_btn.destroy()
        self.bck_btn.destroy()
        home = Home(root)
    def back_to_home3(self):
        self.enter_pin_page_title.destroy()
        self.pin_label1.destroy()
        self.pin_label2.destroy()
        self.pin_label3.destroy()
        self.pin_label4.destroy()
        self.pin_label5.destroy()
        self.pin_label6.destroy()
        self.pin_label7.destroy()
        self.e31.destroy()
        self.e32.destroy()
        self.e33.destroy()
        self.e34.destroy()
        self.e35.destroy()
        self.e36.destroy()
        self.e37.destroy()
        self.submit_btn.destroy()
        self.bck_btn.destroy()
        home = Home(root)
    def back_to_home4(self):
        self.enter_pin_page_title.destroy()
        self.pin_label1.destroy()
        self.pin_label2.destroy()
        self.pin_label3.destroy()
        self.pin_label4.destroy()
        self.pin_label5.destroy()
        self.submit_btn.destroy()
        self.bck_btn.destroy()
        home = Home(root)
home =Home(root)

root.geometry('500x300+550+150')


root.mainloop()