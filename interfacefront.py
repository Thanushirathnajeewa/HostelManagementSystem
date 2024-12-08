import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hostel Management System of ABC Univercity")
root.geometry("1000x700")
# Frame 1 (Page 1)
frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True)

#Horizontal ruler (separator line)
ruler = tk.Frame(frame1, height=18, bg="blue", bd=2, relief="flat")
ruler.pack(fill=tk.X, pady=10)  # fill horizontally and add space around it

# Label and Button for Frame 1
label1 = tk.Label(frame1, text="Hostel Management System", font=("didot", 38, "bold"),background="light blue",width="50",height="2",relief="solid" )
label1.pack(pady=1)

#Horizontal ruler (separator line)
ruler = tk.Frame(frame1, height=18, bg="blue", bd=2, relief="flat")
ruler.pack(fill=tk.X, pady=10)  # fill horizontally and add space around it

#register
window_title = tk.Label(frame1, text="If you are login at first time please,register here", font=("Helvetica", 15, "bold"),background="light green",width="45",height="1",relief="solid")
window_title.pack(pady=1)

# Function to switch to Page 3
def go_to_page3():
    frame1.pack_forget()  # Hide Frame 1
    frame3.pack(fill="both", expand=True)  # Show Frame 3

insert_button = tk.Button(frame1, text="Register", command=go_to_page3)
insert_button.pack(pady=20)

# Frame 3 (Page 3)
frame3 = tk.Frame(root)

# Label and Button for Frame 3
label2 = tk.Label(frame3, text=" New Registration", font=("Helvetica", 16),background="light green",width="30",height="2",relief="solid")
label2.pack(pady=50)

# Function to switch to Page 1
def go_to_page1():
    frame3.pack_forget()  # Hide Frame 3
    frame1.pack(fill="both", expand=True)  # Show Frame 1

button3 = tk.Button(frame3, text="back", command=go_to_page1)
button3.pack(pady=10)

# Start with Frame 1
frame1.pack(fill="both", expand=True)

#Horizontal ruler (separator line)
ruler = tk.Frame(frame1, height=18, bg="blue", bd=2, relief="flat")
ruler.pack(fill=tk.X, pady=10)  # fill horizontally and add space around it

#login
window_title = tk.Label(frame1, text="Student/Admin Login", font=("Helvetica", 20, "bold"),background="light green",width="30",height="2",relief="solid")
window_title.pack(pady=15)
label = tk.Label(frame1, text="Enter user ID:",font=("Helvetica", 15),background="light blue",width="25",height="2")
label.pack(pady=1)
entry = tk.Entry(frame1)
entry.pack(pady=10)
label = tk.Label(frame1, text="password:",font=("Helvetica", 15),background="light blue",width="25",height="2")
label.pack(pady=1)
entry = tk.Entry(frame1)
entry.pack(pady=5)

# Function to switch to Page 2
def go_to_page2():
    frame1.pack_forget()  # Hide Frame 1
    frame2.pack(fill="both", expand=True)  # Show Frame 2

button1 = tk.Button(frame1, text="I am a student: LOGIN here", command=go_to_page2)
button1.pack(side=tk.BOTTOM,pady=10)

# Function to switch to Page 4
def go_to_page4():
    frame1.pack_forget()  # Hide Frame 1
    frame4.pack(fill="both", expand=True)  # Show Frame 4

# Frame 4 (Page 4)
frame4 = tk.Frame(root)

button4 = tk.Button(frame1, text="I am an admin: LOGIN here", command=go_to_page4)
button4.pack(side=tk.BOTTOM,pady=10)


# Label and Button for Frame 4
label2 = tk.Label(frame4, text="Notice", font=("Helvetica", 16),background="light green",width="30",height="2",relief="solid")
label2.pack(pady=50)
label2 = tk.Label(frame4, text="Room allocation", font=("Helvetica", 16),background="light green",width="30",height="2",relief="solid")
label2.pack(pady=50)

# Function to switch to Page 1
def go_to_page1():
    frame4.pack_forget()  # Hide Frame 2
    frame1.pack(fill="both", expand=True)  # Show Frame 1

button4 = tk.Button(frame4, text="back", command=go_to_page1)
button4.pack(pady=10)

# Start with Frame 1
frame1.pack(fill="both", expand=True)
# Frame 2 (Page 2)
frame2 = tk.Frame(root)

# Label and Button for Frame 2
label2 = tk.Label(frame2, text="Room Allocation", font=("Helvetica", 16),background="light green",width="30",height="2",relief="solid")
label2.pack(pady=50)
label2 = tk.Label(frame2, text="Complains", font=("Helvetica", 16),background="light green",width="30",height="2",relief="solid")
label2.pack(pady=50)
label2 = tk.Label(frame2, text="Payments", font=("Helvetica", 16),background="light green",width="30",height="2",relief="solid")
label2.pack(pady=50)

# Function to switch to Page 1
def go_to_page1():
    frame2.pack_forget()  # Hide Frame 2
    frame1.pack(fill="both", expand=True)  # Show Frame 1

button2 = tk.Button(frame2, text="back", command=go_to_page1)
button2.pack(pady=10)

# Start with Frame 1
frame1.pack(fill="both", expand=True)

# Run the Tkinter event loop
root.mainloop()