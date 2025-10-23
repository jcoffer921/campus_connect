# gui.py
# Builds the graphical interface for Campus Connect

import customtkinter as ctk
import tkinter.messagebox as tkmb
from campusconnect.graph_structure import Graph


class CampusConnectApp:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Campus Connect")
        self.root.geometry("1000x600")
        self.graph = Graph()
        self.pages = {}
        self.login()

    def run(self):
        self.root.mainloop()

    def show_page(self, page_class):
        frame = self.pages[page_class]
        frame.tkraise()

    def login(self, user_entry=None, user_pass=None):
        # Create a shadow frame first
        shadow = ctk.CTkFrame(
            self.root,
            width=410,
            height=310,
            corner_radius=20,
            fg_color="#1a1a1a" # dark gray shadow
        )
        shadow.place(relx=0.5, rely=0.5, anchor="center", x=4, y=4)

        # Create main login card
        login_frame = ctk.CTkFrame(
            self.root,
            width=400,
            height=300,
            corner_radius=20,
            fg_color="#2b2b2b" # a lighter gray
        )
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add widgets inside the card
        title_label = ctk.CTkLabel(login_frame, text="Campus Connect Login", font=("Arial", 20, "bold"))
        title_label.pack(pady=(20, 10))

        # Username filed
        user_entry = ctk.CTkEntry(login_frame, placeholder_text="Username")
        user_entry.pack(pady=10, ipadx=50)

        # Password field
        user_pass = ctk.CTkEntry(login_frame, placeholder_text="Password")
        user_pass.pack(pady=10, ipadx=50)

        # Checks if credentials are currect when button is pressed
        def check_login():

            # Set username
            username = "Campus"

            # Set password
            password = ("Connect123")

            if user_entry.get() == username and user_pass.get() == password:
                tkmb.showinfo(title = "Login Success", message = "You have successfully logged in")
                login_frame.destroy() # removes login card
                shadow.destroy() # removes shadow frame
                self.setup_main_interface() # builds main UI
            elif user_entry.get() == username and user_pass.get() != password:
                tkmb.showwarning(title="Wrong Password", message="Please check your password")
            elif user_entry.get() != username and user_pass.get() == password:
                tkmb.showwarning(title="Wrong Username", message = "Please checj your username")
            else:
                tkmb.showerror(title="Login Failed", message="Please check your username and password")

        login_button = ctk.CTkButton(login_frame, text="Login", command=check_login)
        login_button.pack(pady=20)

    def setup_main_interface(self):
        navbar = ctk.CTkFrame(self.root, height=50)
        navbar.pack(side="top", fill="x")

        home_btn = ctk.CTkButton(navbar, text="Home", command=lambda: self.show_page("home"))
        home_btn.pack(side="left", padx=10)

        '''
     # GUI Pages
    #Home
    def homePage(self):

    def addStudentPage(self):

    def connectionsPage(self):

    def graphsPage(self):

    def aboutPage(self):
'''