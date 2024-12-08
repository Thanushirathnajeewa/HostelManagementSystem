import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Database connection and setup
def connect_db():
    conn = sqlite3.connect("hostelmanagementsystem.db")  # Creates or connects to the database
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            nationality TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            email TEXT NOT NULL,
            dob TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def register_student():
    student_id = id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    gender = gender_var.get()
    nationality = nationality_entry.get()
    contact_number = contact_entry.get()
    email = email_entry.get()
    dob = dob_entry.get()

    # Input validation
    if not (student_id and first_name and last_name and gender and nationality and contact_number and email and dob):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        conn = sqlite3.connect("student_register.db")
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO students (student_id, first_name, last_name, gender, nationality, contact_number, email, DateOfBirth) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (int(student_id), first_name, last_name, gender, nationality, contact_number, email, dob))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student registered successfully!")

        # Clear input fields
        id_entry.delete(0, tk.END)
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        gender_var.set("")  # Reset dropdown
        nationality_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        dob_entry.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Student ID must be unique!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Tkinter GUI
root = tk.Tk()
root.title("Student Register Form")

# Labels and Entry Fields
tk.Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="First Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Last Name").grid(row=2, column=0, padx=10, pady=5, sticky="w")
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender").grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"], state="readonly")
gender_dropdown.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Nationality").grid(row=4, column=0, padx=10, pady=5, sticky="w")
nationality_entry = tk.Entry(root)
nationality_dropdown = ttk.Combobox(root, textvariable=nationality_entry, values=["Sinhala", "Tamil","Muslim", "Other"], state="readonly")
nationality_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Contact Number").grid(row=5, column=0, padx=10, pady=5, sticky="w")
contact_entry = tk.Entry(root)
contact_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=6, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Date of Birth (YYYY-MM-DD)").grid(row=7, column=0, padx=10, pady=5, sticky="w")
dob_entry = tk.Entry(root)
dob_entry.grid(row=7, column=1, padx=10, pady=5)

# Register Button
register_button = tk.Button(root, text="Register", command=register_student)
register_button.grid(row=8, columnspan=2, pady=10)

# Connect to the database
connect_db()

# Run the application
root.mainloop()