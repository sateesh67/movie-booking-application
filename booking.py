from tkinter import *
from tkinter import ttk, messagebox
from database import get_movies, book_ticket, get_bookings, cancel_booking


class BookingFrame:

    def __init__(self, root):

        self.root = root

        # ================= Variables =================
        self.customer = StringVar()
        self.movie = StringVar()
        self.seats = IntVar()

        # ================= Booking Form =================
        title = Label(
            root,
            text="Ticket Booking",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        form = Frame(root)
        form.pack(pady=10)

        Label(form, text="Customer Name").grid(row=0, column=0, padx=10, pady=10)
        Entry(form, textvariable=self.customer, width=30).grid(
            row=0, column=1, padx=10, pady=10
        )

        Label(form, text="Movie").grid(row=1, column=0, padx=10, pady=10)

        self.movie_combo = ttk.Combobox(
            form,
            textvariable=self.movie,
            width=28,
            state="readonly"
        )
        self.movie_combo.grid(row=1, column=1, padx=10, pady=10)

        self.load_movies()

        Label(form, text="Number of Seats").grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        Entry(
            form,
            textvariable=self.seats,
            width=30
        ).grid(row=2, column=1, padx=10, pady=10)

        Button(
            form,
            text="Book Ticket",
            width=15,
            command=self.save_booking
        ).grid(row=3, column=0, pady=10)

        Button(
            form,
            text="Cancel Booking",
            width=15,
            command=self.delete_booking
        ).grid(row=3, column=1, pady=10)

        # ================= Booking Table =================
        columns = (
            "ID",
            "Customer",
            "Movie",
            "Theatre",
            "Show",
            "Seats",
            "Amount"
        )

        self.booking_table = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:
            self.booking_table.heading(col, text=col)
            self.booking_table.column(col, width=120)

        self.booking_table.pack(fill=X, padx=20, pady=10)

        self.load_bookings()

    # ================= Load Movies =================
    def load_movies(self):

        movie_data = get_movies()

        movie_names = []

        for movie in movie_data:
            movie_names.append(movie[1])

        self.movie_combo["values"] = movie_names

    # ================= Book Ticket =================
    def save_booking(self):

        customer = self.customer.get()
        movie_name = self.movie.get()
        seat_count = self.seats.get()

        if customer == "" or movie_name == "" or seat_count <= 0:
            messagebox.showerror(
                "Error",
                "Please fill all fields correctly."
            )
            return

        movies = get_movies()

        selected_movie = None

        for movie in movies:
            if movie[1] == movie_name:
                selected_movie = movie
                break

        if selected_movie is None:
            messagebox.showerror(
                "Error",
                "Movie not found."
            )
            return

        theatre = selected_movie[2]
        show_time = selected_movie[3]
        price = selected_movie[4]

        total_amount = seat_count * price

        book_ticket(
            customer,
            movie_name,
            theatre,
            show_time,
            seat_count,
            total_amount
        )

        messagebox.showinfo(
            "Success",
            "Ticket booked successfully."
        )

        self.customer.set("")
        self.movie.set("")
        self.seats.set(0)

        self.load_bookings()

    # ================= View Bookings =================
    def load_bookings(self):

        for row in self.booking_table.get_children():
            self.booking_table.delete(row)

        bookings = get_bookings()

        for booking in bookings:
            self.booking_table.insert("", END, values=booking)

    # ================= Cancel Booking =================
    def delete_booking(self):

        selected = self.booking_table.focus()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a booking first."
            )
            return

        booking_data = self.booking_table.item(selected)["values"]

        booking_id = booking_data[0]

        cancel_booking(booking_id)

        messagebox.showinfo(
            "Success",
            "Booking cancelled successfully."
        )

        self.load_bookings()
