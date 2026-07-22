from tkinter import *
from tkinter import messagebox


class LoginWindow:

    def __init__(self, root, success_callback):

        self.root = root
        self.success_callback = success_callback

        self.login_frame = Frame(root)
        self.login_frame.pack(expand=True)

        title = Label(
            self.login_frame,
            text="ADMIN LOGIN",
            font=("Arial", 22, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=20)

        Label(
            self.login_frame,
            text="Username",
            font=("Arial", 12)
        ).grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.username = Entry(
            self.login_frame,
            font=("Arial", 12),
            width=25
        )
        self.username.grid(row=1, column=1, padx=10)

        Label(
            self.login_frame,
            text="Password",
            font=("Arial", 12)
        ).grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.password = Entry(
            self.login_frame,
            show="*",
            font=("Arial", 12),
            width=25
        )
        self.password.grid(row=2, column=1, padx=10)

        Button(
            self.login_frame,
            text="Login",
            font=("Arial", 12, "bold"),
            bg="green",
            fg="white",
            width=15,
            command=self.login
        ).grid(row=3, column=0, columnspan=2, pady=20)

        Button(
            self.login_frame,
            text="Clear",
            font=("Arial", 12),
            width=15,
            command=self.clear_fields
        ).grid(row=4, column=0, columnspan=2)

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        # Default Admin Credentials
        if username == "admin" and password == "admin123":

            messagebox.showinfo(
                "Login Successful",
                "Welcome Admin!"
            )

            self.login_frame.destroy()

            self.success_callback()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password."
            )

    def clear_fields(self):

        self.username.delete(0, END)
        self.password.delete(0, END)
