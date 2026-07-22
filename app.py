from tkinter import *
from tkinter import ttk, messagebox
from database import create_tables
from login import LoginWindow
from movie import MovieFrame
from booking import BookingFrame


class MovieBookingApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Movie Booking Application")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        # Create database tables
        create_tables()

        # Show Login Window
        LoginWindow(self.root, self.load_dashboard)

    def load_dashboard(self):

        # Remove Login Screen
        for widget in self.root.winfo_children():
            widget.destroy()

        title = Label(
            self.root,
            text="MOVIE BOOKING APPLICATION",
            font=("Arial", 22, "bold"),
            bg="darkblue",
            fg="white",
            pady=15
        )

        title.pack(fill=X)

        # Notebook Tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Movie Tab
        movie_tab = Frame(notebook)
        notebook.add(movie_tab, text="Movie Management")

        # Booking Tab
        booking_tab = Frame(notebook)
        notebook.add(booking_tab, text="Ticket Booking")

        # Load Frames
        MovieFrame(movie_tab)
        BookingFrame(booking_tab)

        footer = Label(
            self.root,
            text="Developed Using Python | Tkinter | SQLite",
            font=("Arial", 10),
            fg="gray"
        )

        footer.pack(side=BOTTOM, pady=5)


def main():

    root = Tk()

    app = MovieBookingApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
