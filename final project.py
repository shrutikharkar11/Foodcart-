import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import mysql.connector
from PIL import Image, ImageTk
import pandas as pd

class FoodCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FoodCart App")
        self.root.geometry('750x550+100+50')
        self.root.configure(bg='#fff')
        self.root.resizable(False, False)

        # Connect to MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="your_database_name"
        )

        self.create_table()
        self.shopping_cart = []  # Initialize the shopping cart list

        # Set background image
        self.background_image = tk.PhotoImage(file="C:\\Users\\Pujan Kharkar\\Downloads\\app\\vegetables.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        # Placeholder images (replace these paths with your image paths)
        self.image1_path ="C:\\Users\\Pujan Kharkar\\Downloads\\app\\vegetables.png"
        self.image2_path ="C:\\Users\\Pujan Kharkar\\Downloads\\app\\fish.png"
        self.image3_path ="C:\\Users\\Pujan Kharkar\\Downloads\\app\\dairy products.png"
        self.image4_path ="C:\\Users\\Pujan Kharkar\\Downloads\\app\\fruits.png"


        # Create a frame for the login page
        self.login_frame = tk.Frame(self.root, bg="black", width=450, height=600)
        self.login_frame.place(x=300, y=120)

        # UI elements
        self.create_login_page()

    def create_table(self):
        # Create a 'users' table if it doesn't exist
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                password VARCHAR(255),
                address VARCHAR(255),
                contact VARCHAR(20),
                email VARCHAR(255)
            )
        ''')
        self.conn.commit()

    def create_login_page(self):
        # Clear previous widgets
        for widget in self.login_frame.winfo_children():
            widget.destroy()

        # Create login widgets
        self.label_username = tk.Label(self.login_frame, text="Username:")
        self.entry_username = tk.Entry(self.login_frame)
        self.label_password = tk.Label(self.login_frame, text="Password:")
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.button_login = tk.Button(self.login_frame, text="Login", command=self.login)
        self.button_register = tk.Button(self.login_frame, text="Register", command=self.create_register_window)

        # Place widgets in the grid
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_register.grid(row=5, column=0, columnspan=2, pady=10)
        #forget button
        self.button_forget=tk.Button(self.login_frame,text="Forget password",command=self.forget_password ,bg='black',fg='white')
        self.button_forget.grid(row=2, column=1, columnspan=2, pady=10)

    def create_register_window(self):
        # Create a new window for registration
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")
        register_window.configure(bg="black")

        # Create register widgets
        self.label_register_username = tk.Label(register_window, text="Username:")
        self.entry_register_username = tk.Entry(register_window)
        self.label_register_contact = tk.Label(register_window, text="Contact Number:")
        self.entry_register_contact = tk.Entry(register_window)
        self.label_register_address = tk.Label(register_window, text="Address:")
        self.entry_register_address = tk.Entry(register_window)
        self.label_register_email = tk.Label(register_window, text="Email:")
        self.entry_register_email = tk.Entry(register_window)
        self.label_register_password = tk.Label(register_window, text="Password:")
        self.entry_register_password = tk.Entry(register_window, show="*")
        self.button_generate_otp = tk.Button(register_window, text="Generate OTP", command=self.generate_otp)
        self.label_otp = tk.Label(register_window, text="Enter OTP:")
        self.entry_otp = tk.Entry(register_window)
        self.button_register_user = tk.Button(register_window, text="Register", command=self.register_user)

        # Place widgets in the grid
        self.label_register_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_register_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_register_contact.grid(row=1, column=0, padx=10, pady=10)
        self.entry_register_contact.grid(row=1, column=1, padx=10, pady=10)
        self.label_register_address.grid(row=2, column=0, padx=10, pady=10)
        self.entry_register_address.grid(row=2, column=1, padx=10, pady=10)
        self.label_register_email.grid(row=3, column=0, padx=10, pady=10)
        self.entry_register_email.grid(row=3, column=1, padx=10, pady=10)
        self.label_register_password.grid(row=4, column=0, padx=10, pady=10)
        self.entry_register_password.grid(row=4, column=1, padx=10, pady=10)
        self.button_generate_otp.grid(row=5, column=0, columnspan=2, pady=10)
        self.label_otp.grid(row=6, column=0, padx=10, pady=10)
        self.entry_otp.grid(row=6, column=1, padx=10, pady=10)
        self.button_register_user.grid(row=7, column=0, columnspan=2, pady=10)

    def clear_widgets(self):
        # Clear all widgets from the grid
        for widget in self.login_frame.winfo_children():
            widget.destroy()

    def generate_otp(self):
        # Generate a random 4-digit OTP
        otp = random.randint(1000, 9999)
        messagebox.showinfo("OTP", f"Your OTP is: {otp}")

    def register_user(self):
        # Get user inputs
        username = self.entry_register_username.get()
        contact = self.entry_register_contact.get()
        address = self.entry_register_address.get()
        email = self.entry_register_email.get()
        password = self.entry_register_password.get()
        otp = self.entry_otp.get()

     # Check if OTP is valid (for simplicity, assuming the OTP is correct)
        if not otp.isdigit() or len(otp) != 4:
            messagebox.showerror("Error", "Invalid OTP. Please generate a new OTP.")
            return

        # Check if username already exists
        if self.check_username_exists(username):
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
            return

        # Register the user in the database
        self.register_user_in_db(username, password, address, contact, email)

        # Inform the user about successful registration
        messagebox.showinfo("Registration Successful", "User registered successfully. You can now log in.")

        # Close the register window
        self.root.focus_set()

    def check_username_exists(self, username):
        # Check if username already exists in the database
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s', (username,))
        return cursor.fetchone() is not None

    def register_user_in_db(self, username, password, address, contact, email):
        # Register the user in the database
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (username, password, address, contact, email) VALUES (%s, %s, %s, %s, %s)',
                       (username, password, address, contact, email))
        self.conn.commit()

    def forget_password(self):
        username = simpledialog.askstring("Forget Password", "Enter your username:")
        if username:
            if self.check_username_exists(username):
                # Generate a new password and update it in the database
                new_password = self.generate_random_password()
                self.update_password_in_db(username, new_password)

                # Send the new password to the user's email
                self.send_password_reset_email(username, new_password)

                messagebox.showinfo("Password Reset", "A new password has been sent to your email.")
            else:
                messagebox.showerror("Error", "Invalid username. Please check your username.")

   
    def update_password_in_db(self, username, new_password):
        # Update the password in the database
        cursor = self.conn.cursor()
        cursor.execute('UPDATE users SET password=%s WHERE username=%s', (new_password, username))
        self.conn.commit()

    def send_password_reset_email(self, username, new_password):
        # Replace these values with your SMTP server details
        smtp_server = 'your_smtp_server'
        smtp_port = 587
        smtp_username = 'your_email@example.com'
        smtp_password = 'your_email_password'

        # Create the email content
        subject = 'Password Reset'
        body = f'Your new password is: {new_password}'
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = smtp_username
        message['To'] = self.get_user_email(username)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, [message['To']], message.as_string())

    def get_user_email(self, username):
        # Get the email associated with the given username
        cursor = self.conn.cursor()
        cursor.execute('SELECT email FROM users WHERE username=%s', (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def login(self):
        # Get user inputs
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if username exists
        if not self.check_username_exists(username):
            messagebox.showerror("Error", "Invalid username. Please check your username.")
            return

        # Check if password is correct
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
        if cursor.fetchone() is None:
            messagebox.showerror("Error", "Incorrect password. Please check your password.")
            return

        # Inform the user about successful login
        messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
        self.create_homepage(username)

    def create_homepage(self, username):
        homepage_window = tk.Toplevel(self.root)
        homepage_window.geometry('750x550+100+50')
        homepage_window.title("Homepage")
        homepage_window.configure(bg="black")
         
        # Create buttons with images using the grid method
        veg_button = tk.Button(homepage_window, text="Vegetables", command=self.open_vegetables_window)
        veg_image = ImageTk.PhotoImage(Image.open("C:\\Users\\Pujan Kharkar\\Downloads\\app\\veg.png"))
        veg_button.config(image=veg_image, compound=tk.TOP)
        veg_button.image = veg_image
        veg_button.grid(row=0, column=0, padx=20, pady=20)

        fish_button = tk.Button(homepage_window, text="Fish", command=self.open_fish_window)
        fish_image = ImageTk.PhotoImage(Image.open("C:\\Users\\Pujan Kharkar\\Downloads\\app\\fish.png"))
        fish_button.config(image=fish_image, compound=tk.TOP)
        fish_button.image = fish_image
        fish_button.grid(row=0, column=1, padx=20, pady=20)

        dairy_button = tk.Button(homepage_window, text="Dairy", command=self.open_dairy_window)
        dairy_image = ImageTk.PhotoImage(Image.open("C:\\Users\\Pujan Kharkar\\Downloads\\app\\dairy products.png"))
        dairy_button.config(image=dairy_image, compound=tk.TOP)
        dairy_button.image = dairy_image
        dairy_button.grid(row=1, column=0, padx=20, pady=20)

        fruits_button = tk.Button(homepage_window, text="Fruits", command=self.open_fruits_window)
        fruits_image = ImageTk.PhotoImage(Image.open("C:\\Users\\Pujan Kharkar\\Downloads\\app\\fruits.png"))
        fruits_button.config(image=fruits_image, compound=tk.TOP)
        fruits_button.image = fruits_image
        fruits_button.grid(row=1, column=1, padx=20, pady=20)

    def open_vegetables_window(self):
        vegetables_window = tk.Toplevel(self.root)
        vegetables_window.title("Vegetables Window")
        vegetables_window.geometry('800x600')
        vegetables_window.configure(bg="black")

        # Create a dictionary to store prices for each vegetable
        self.vegetable_prices = {
            "Carrot": 1.99,
            "Broccoli": 2.49,
            "Spinach": 1.79,
            "Tomato": 2.99,
            "Cucumber": 0.99,
            "Bell Pepper": 1.49,
            "Zucchini": 1.29,
            "Lettuce": 2.19,
            "Onion": 0.79,
            "Garlic": 3.99,
        }
# Function to handle button click event
        def button_click(vegetable, price, quantity_var):
            quantity_str = quantity_var.get()

            # Extract numeric part and unit from the quantity string
            quantity, unit = self.extract_quantity_and_unit(quantity_str)

            # Convert quantity to grams (1kg = 1000g)
            if unit == 'kg':
                quantity *= 1

            total_price = price * quantity
            messagebox.showinfo("Order Summary", f"You ordered {quantity_str} of {vegetable}. Total price: ${total_price:.2f}")

            # Add the item to the shopping cart
            self.shopping_cart.append({"item": vegetable, "quantity": quantity_str, "price": total_price})

            # Optional: Print the updated shopping cart
            print(self.shopping_cart)

        # Create buttons for each vegetable with price and quantity options
        row_num = 0
        for vegetable, price in self.vegetable_prices.items():
            label = tk.Label(vegetables_window, text=f"{vegetable} - ${price:.2f}", font=("Arial", 12), fg="white", bg="black")
            label.grid(row=row_num, column=0, padx=10, pady=5)

            # Create a StringVar to store the selected quantity
            quantity_var = tk.StringVar()
            quantity_var.set("250g")  # Set default quantity

            # Create a menu button for quantity
            quantity_menu = tk.OptionMenu(vegetables_window, quantity_var, "250g", "500g", "1kg")
            quantity_menu.config(font=("Arial", 12), fg="black", bg="white")
            quantity_menu.grid(row=row_num, column=1, padx=10, pady=5)

            # Create a button to add the item to the cart
            button = tk.Button(vegetables_window, text="Add to Cart", command=lambda veg=vegetable, pr=price, var=quantity_var: button_click(veg, pr, var))
            button.grid(row=row_num, column=2, padx=10, pady=5)

            row_num += 1

    def extract_quantity_and_unit(self, quantity_str):
        # Extract numeric part and unit from the quantity string
        quantity = ''
        unit = ''
        for char in quantity_str:
            if char.isdigit() or char == '.':
                quantity += char
            else:
                unit += char
        if quantity:
            quantity = float(quantity)
        return quantity, unit.lower()




    

 
    def open_fish_window(self):
        # Create fish_window as an instance variable to make it accessible in other methods
        self.fish_window = tk.Toplevel(self.root)
        self.fish_window.title("Fish Window")
        self.fish_window.geometry('600x400')
        label = tk.Label(self.fish_window, font=("Arial", 16))
        label.grid(pady=20)
        self.fish_window.configure(bg="black")

        # Create a dictionary to store prices for each fish
        fish_prices = {
            "Salmon": 9.99,
            "Tuna": 7.49,
            "Cod": 5.79,
            "Sardines": 3.99,
            "Shrimp": 12.99,
            "Mackerel": 6.49,
            "Trout": 8.19,
            "Catfish": 4.99,
            "Halibut": 10.29,
            "Snapper": 11.49,
        }

        def button_click(fish, price, quantity_var):
            quantity_str = quantity_var.get()
            quantity, unit = self.extract_quantity_and_unit(quantity_str)

            # Convert quantity to grams (1kg = 1000g)
            if unit == 'kg':
                quantity *= 12

            total_price = price * quantity
            messagebox.showinfo("Order Summary", f"You ordered {quantity_str} of {fish}. Total price: ${total_price:.2f}")

            # Add the item to the shopping cart
            self.shopping_cart.append({"item": fish, "quantity": quantity_str, "price": total_price})

        # Create buttons for each fish with price and quantity options
        row_num = 0
        for fish, price in fish_prices.items():
            label = tk.Label(self.fish_window, text=f"{fish} - ${price:.2f}", font=("Arial", 12), fg="white", bg="black")
            label.grid(row=row_num, column=0, padx=10, pady=5)

            # Create a StringVar to store the selected quantity
            quantity_var = tk.StringVar()
            quantity_var.set("250g")  # Set default quantity

            # Create a menu button for quantity
            quantity_menu = tk.OptionMenu(self.fish_window, quantity_var, "250g", "500g", "1kg")
            quantity_menu.config(font=("Arial", 12), fg="black", bg="white")
            quantity_menu.grid(row=row_num, column=1, padx=10, pady=5)

            # Create a button to add the item to the cart
            button = tk.Button(self.fish_window, text="Add to Cart", command=lambda f=fish, pr=price, var=quantity_var: button_click(f, pr, var))
            button.grid(row=row_num, column=2, padx=10, pady=5)

            row_num += 1

    def extract_quantity_and_unit(self, quantity_str):
        # Extract numeric part and unit from the quantity string
        quantity = ''
        unit = ''
        for char in quantity_str:
            if char.isdigit() or char == '.':
                quantity += char
            else:
                unit += char
        if quantity:
            quantity = float(quantity)
        return quantity, unit.lower()

    
    def open_dairy_window(self):
        # Create dairy_window as an instance variable to make it accessible in other methods
        self.dairy_window = tk.Toplevel(self.root)
        self.dairy_window.title("Dairy Window")
        self.dairy_window.geometry('600x400')
        self.dairy_window.configure(bg="black")

        # Create a dictionary to store prices for each dairy product
        dairy_prices = {
            "Milk": 1.99,
            "Cheese": 3.49,
            "Yogurt": 2.79,
            "Butter": 2.99,
            "Cream": 1.49,
            "Eggs": 2.19,
            "Sour Cream": 1.29,
            "Cottage Cheese": 2.49,
            "Whipped Cream": 3.99,
            "Condensed Milk": 2.49,
        }

        # Function to handle button click event
        def button_click(dairy, price, quantity_var):
            quantity_str = quantity_var.get()
            quantity, unit = self.extract_quantity_and_unit(quantity_str)

            # Convert quantity to grams (1kg = 1000g)
            if unit == 'kg':
                quantity *= 1000

            total_price = price * quantity
            messagebox.showinfo("Order Summary", f"You ordered {quantity_str} of {dairy}. Total price: ${total_price:.2f}")

            # Add the item to the shopping cart
            self.shopping_cart.append({"item": dairy, "quantity": quantity_str, "price": total_price})

        # Create buttons for each dairy product with price and quantity options
        row_num = 0
        for dairy, price in dairy_prices.items():
            label = tk.Label(self.dairy_window, text=f"{dairy} - ${price:.2f}", font=("Arial", 12), fg="white", bg="black")
            label.grid(row=row_num, column=0, padx=10, pady=5)

            # Create a StringVar to store the selected quantity
            quantity_var = tk.StringVar()
            quantity_var.set("250g")  # Set default quantity

            # Create a menu button for quantity
            quantity_menu = tk.OptionMenu(self.dairy_window, quantity_var, "250g", "500g", "1kg")
            quantity_menu.config(font=("Arial", 12), fg="black", bg="white")
            quantity_menu.grid(row=row_num, column=1, padx=10, pady=5)

            # Create a button to add the item to the cart
            button = tk.Button(self.dairy_window, text="Add to Cart", command=lambda d=dairy, pr=price, var=quantity_var: button_click(d, pr, var))
            button.grid(row=row_num, column=2, padx=10, pady=5)

            row_num += 1

    def extract_quantity_and_unit(self, quantity_str):
        # Extract numeric part and unit from the quantity string
        quantity = ''
        unit = ''
        for char in quantity_str:
            if char.isdigit() or char == '.':
                quantity += char
            else:
                unit += char
        if quantity:
            quantity = float(quantity)
        return quantity, unit.lower()


    def extract_quantity_and_unit(self, quantity_str):
        # Extract numeric part and unit from the quantity string
        quantity = ''
        unit = ''
        for char in quantity_str:
            if char.isdigit() or char == '.':
                quantity += char
            else:
                unit += char
        if quantity:
            quantity = float(quantity)
        return quantity, unit.lower()
        

    def open_fruits_window(self):
        fruits_window = tk.Toplevel(self.root)
        fruits_window.title("Fruits Window")
        fruits_window.geometry('600x400')
        fruits_window.configure(bg="black")

        # Create a dictionary to store prices for each fruit
        fruit_prices = {
            "Apple": 1.49,
            "Banana": 0.99,
            "Orange": 1.29,
            "Grapes": 2.99,
            "Strawberry": 3.49,
            "Watermelon": 4.99,
            "Pineapple": 2.79,
            "Mango": 1.79,
            "Kiwi": 1.19,
            "Peach": 1.69,
        }

        # Function to handle button click event
        def button_click(fruit, price, quantity_var):
            quantity_str = quantity_var.get()
            quantity, unit = self.extract_quantity_and_unit(quantity_str)

            # Convert quantity to grams (1kg = 1000g)
            if unit == 'kg':
                quantity *= 12

            total_price = price * quantity
            messagebox.showinfo("Order Summary", f"You ordered {quantity_str} of {fruit}. Total price: ${total_price:.2f}")

            # Add the item to the shopping cart
            self.shopping_cart.append({"item": fruit, "quantity": quantity_str, "price": total_price})

        # Create buttons for each fruit with price and quantity options
        row_num = 0
        for fruit, price in fruit_prices.items():
            label = tk.Label(fruits_window, text=f"{fruit} - ${price:.2f}", font=("Arial", 12), fg="white", bg="black")
            label.grid(row=row_num, column=0, padx=10, pady=5)

            # Create a StringVar to store the selected quantity
            quantity_var = tk.StringVar()
            quantity_var.set("250g")  # Set default quantity

            # Create a menu button for quantity
            quantity_menu = tk.OptionMenu(fruits_window, quantity_var, "250g", "500g", "1kg")
            quantity_menu.config(font=("Arial", 12), fg="black", bg="white")
            quantity_menu.grid(row=row_num, column=1, padx=10, pady=5)

            # Create a button to add the item to the cart
            button = tk.Button(fruits_window, text="Add to Cart", command=lambda f=fruit, pr=price, var=quantity_var: button_click(f, pr, var))
            button.grid(row=row_num, column=2, padx=10, pady=5)

            row_num += 1

    def extract_quantity_and_unit(self, quantity_str):
        # Extract numeric part and unit from the quantity string
        quantity = ''
        unit = ''
        for char in quantity_str:
            if char.isdigit() or char == '.':
                quantity += char
            else:
                unit += char
        if quantity:
            quantity = float(quantity)
        return quantity, unit.lower()



if __name__ == "__main__":
    root = tk.Tk()
    app = FoodCartApp(root)
    root.mainloop()
