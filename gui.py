# gui.py
# Campus Connect GUI (Modern Clean Version)

import customtkinter as ctk
import tkinter.messagebox as tkmb
from graph_structure import Graph
from PIL import Image


class CampusConnectApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Campus Connect")
        self.root.geometry("1100x700")

        ctk.set_appearance_mode("light")

        # Theme colors
        self.primary = "#0047AB"   # Cobalt blue
        self.accent = "#2563EB"
        self.bg_color = "#FFFFFF"
        self.text_color = "#1E1E1E"

        self.graph = Graph()
        self.setup_ui()
        self.root.mainloop()

    # ---------------- MAIN UI ----------------
    def setup_ui(self):
        # NAVBAR (horizontal)
        navbar = ctk.CTkFrame(self.root, height=60, fg_color="black", corner_radius=0)
        navbar.pack(fill="x")

        # --- Logo ---
        logo_image = ctk.CTkImage(
            dark_image= Image.open("logo.png"),
            light_image = Image.open("logo.png"),
            size = (40, 40)
        )

        logo_label = ctk.CTkLabel(navbar, image=logo_image, text="")
        logo_label.pack(side="left", padx=(15, 5), pady=10)

        title = ctk.CTkLabel(navbar, text="Campus Connect", font=("Poppins", 22, "bold"), text_color="white")
        title.pack(side="left", padx=25)

        nav_buttons = [
            ("Home", lambda: self.show_page("home")),
            ("Add Student", lambda: self.show_page("add")),
            ("Connections", lambda: self.show_page("connections")),
            ("Graph", lambda: self.show_page("graph")),
            ("Discussions", lambda: self.show_page("discussions")),
        ]

        for text, command in nav_buttons:
            btn = ctk.CTkButton(
                navbar,
                text=text,
                command=command,
                fg_color="transparent",
                text_color="white",
                hover_color=self.accent,
                corner_radius=8,
                width=100,
            )
            btn.pack(side="left", padx=5)

        # CONTENT AREA
        self.content = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        self.content.pack(fill="both", expand=True)

        # --- PAGES ---
        self.pages = {
            "home": self.create_home_page(),
            "add": self.create_placeholder("Add Student Page"),
            "connections": self.create_placeholder("Connections Page"),
            "graph": self.create_placeholder("Graph Page"),
            "discussions": self.create_placeholder("Discussions Page"),
        }

        self.show_page("home")

    # ---------------- HOME PAGE ----------------
    def create_home_page(self):
        page = ctk.CTkFrame(self.content, fg_color=self.bg_color)

        # --- HERO SECTION ---
        hero_height = 300
        hero_frame = ctk.CTkFrame(page, fg_color=self.primary, corner_radius=0, width=1100, height=hero_height)
        hero_frame.pack(fill="x")

        hero_title = ctk.CTkLabel(
            hero_frame,
            text="Welcome to Campus Connect",
            font=("Poppins", 32, "bold"),
            text_color="white"
        )
        hero_title.pack(pady=(40, 5))

        hero_subtitle = ctk.CTkLabel(
            hero_frame,
            text="Find classmates, form study groups, and grow your network.",
            font=("Poppins", 16),
            text_color="white"
        )
        hero_subtitle.pack(pady=(0, 20))

        get_started_btn = ctk.CTkButton(
            hero_frame,
            text="Get Started",
            fg_color="white",
            text_color=self.primary,
            hover_color="#E5E7EB",
            corner_radius=10,
            width=150
        )
        get_started_btn.pack()

        # --- SEARCH SECTION BELOW HERO ---
        search_section = ctk.CTkFrame(page, fg_color=self.bg_color)
        search_section.pack(pady=50)

        search_label = ctk.CTkLabel(
            search_section,
            text="Search Students or Majors",
            font=("Poppins", 18, "bold"),
            text_color=self.text_color
        )
        search_label.pack(pady=(0, 10))

        search_bar = ctk.CTkEntry(
            search_section,
            placeholder_text="Type a name or major...",
            width=400,
            fg_color="#F3F4F6",
            border_color=self.primary,
            text_color=self.text_color
        )
        search_bar.pack()

        return page

    # ---------------- PLACEHOLDER PAGES ----------------
    def create_placeholder(self, text):
        page = ctk.CTkFrame(self.content, fg_color=self.bg_color)
        ctk.CTkLabel(page, text=text, font=("Poppins", 22), text_color=self.text_color).pack(expand=True)
        return page

    # ---------------- PAGE CONTROL ----------------
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_page(self, key):
        for page in self.pages.values():
            page.pack_forget()
        page = self.pages.get(key)
        if page:
            page.pack(fill="both", expand=True)
