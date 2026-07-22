import sqlite3

DATABASE_NAME = "database.db"


def get_connection():
    """
    Create and return a database connection.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    """
    Create Movies and Bookings tables.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Movies Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name TEXT NOT NULL,
            theatre TEXT NOT NULL,
            show_time TEXT NOT NULL,
            ticket_price REAL NOT NULL,
            available_seats INTEGER NOT NULL
        )
    """)

    # Bookings Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            movie_name TEXT NOT NULL,
            theatre TEXT NOT NULL,
            show_time TEXT NOT NULL,
            seats INTEGER NOT NULL,
            total_amount REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- Movie CRUD ---------------- #

def add_movie(movie_name, theatre, show_time, price, seats):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies
        (movie_name, theatre, show_time, ticket_price, available_seats)
        VALUES(?,?,?,?,?)
    """, (movie_name, theatre, show_time, price, seats))

    conn.commit()
    conn.close()


def get_movies():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")

    data = cursor.fetchall()

    conn.close()

    return data


def update_movie(movie_id, movie_name, theatre, show_time, price, seats):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE movies
        SET movie_name=?,
            theatre=?,
            show_time=?,
            ticket_price=?,
            available_seats=?
        WHERE id=?
    """, (movie_name, theatre, show_time, price, seats, movie_id))

    conn.commit()
    conn.close()


def delete_movie(movie_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM movies WHERE id=?",
        (movie_id,)
    )

    conn.commit()
    conn.close()


# ---------------- Booking CRUD ---------------- #

def book_ticket(customer, movie, theatre, show, seats, amount):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings
        (customer_name, movie_name, theatre, show_time, seats, total_amount)
        VALUES(?,?,?,?,?,?)
    """, (customer, movie, theatre, show, seats, amount))

    conn.commit()
    conn.close()


def get_bookings():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")

    data = cursor.fetchall()

    conn.close()

    return data


def cancel_booking(booking_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM bookings WHERE booking_id=?",
        (booking_id,)
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":

    create_tables()

    print("Database and tables created successfully.")
