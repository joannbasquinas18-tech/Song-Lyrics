import tkinter as tk
from tkinter import messagebox


def show_lyric_popups():
    # Hide the main Tkinter root window frame
    root = tk.Tk()
    root.withdraw()

    # Window title matching the screenshot header
    title = "Merry Christmas, I Miss You - Alex Crichton"
 
    # Lyrics sequencez``
    lyrics = [
        "But what if I call",
        "And you pick up the phone?",
        "And I use this holiday to make my way to your ghost",
        "Oh, what if you're lonely",
        "And you know I am too?",
        "And I get the chance to say",
        "Merry Christmas, I miss you",
        "I miss you",
       
    ]

    # Display each line in a pop-up message box sequentially
    for line in lyrics:
        messagebox.showinfo(title, line)


if __name__ == "__main__":
    show_lyric_popups()