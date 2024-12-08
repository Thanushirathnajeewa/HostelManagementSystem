from rooms import check_availability
from connection import connect_to_mysql, create_tables
from complain import add_complaint, read_all_complaints
from announcement import add_announcement, read_all_announcements
from roomallocation import allocate_room
from student_registration import register_student
from payment import collect_payment_details, insert_payment
def admin_login():
    """
    Admin login with hardcoded credentials.
    Returns True if login is successful, else False.
    """
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    # admin username and password
    if username == "admin" and password == "admin123":
        print("Admin login successful!")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

def user_menu(connection):
    """
    Menu for user actions.
    """
    while True:
        print("\n-----------")
        print("User Menu:")
        print("-----------2")
        print("1. View Announcements")
        print("2. Add a Complaint")
        print("3. Check Room Availability")
        print("4. Logout")
        
        user_choice = input("\n----->Enter your choice (1-4): ")

        if user_choice == '1':
            read_all_announcements(connection)
        elif user_choice == '2':
            comment = input("Enter your complaint: ")
            student_id = int(input("Enter your student ID: "))
            add_complaint(connection, comment, student_id)
        elif user_choice == '3':
            check_availability(connection)
        elif user_choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option, please try again.")

def admin_menu(connection):
    """
    Menu for admin actions.
    """
    while True:
        print("\n------------")
        print("Admin Menu:")
        print("------------")
        print("\n1. Add Announcement")
        print("2. Register Student")1
        print("3. Allocate Room")
        print("4. Make Room Available")
        print("5. Read Complaints")
        print("6. Enter Payment Details")
        print("7. Logout")

        admin_choice = input("\n----->Enter your choice (1-7): ")

        if admin_choice == '1':
            message = input("Enter announcement message: ")
            student_id = int(input("Enter student ID: "))  # Only announcement for selected students
            add_announcement(connection, message, student_id)
        elif admin_choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            gender = input("Enter gender (Male/Female/Other): ")
            nationality = input("Enter nationality: ")
            contact_number = input("Enter contact number: ")
            email = input("Enter email: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            role_id = 2  # Default role as User
            register_student(first_name, last_name, gender, nationality, contact_number, email, date_of_birth, role_id)
        elif admin_choice == '3':
            allocate_room()
        elif admin_choice == '4':
            make_room_available()
        elif admin_choice == '5':
            read_all_complaints(connection)
        elif admin_choice == '6':
            # Call the collect_payment_details function to get the payment details
            payment_details = collect_payment_details()
            
            if payment_details:
                # If the details are collected successfully, pass them to the insert_payment function
                payment_id, student_id, invoice_refno, amount, payment_date, payment_method = payment_details
                insert_payment(connection, payment_id, student_id, invoice_refno, amount, payment_date, payment_method)
            else:
                print("Failed to collect valid payment details. Please try again.")
        
        elif admin_choice == '7':
            print("Logging out...")
            break
        else:
            print("Invalid option, please try again.")

def main():
    # Connect to MySQL
    connection = connect_to_mysql()

    if connection:
        create_tables(connection)  # Ensure tables are created

        while True:
            print("\n**************************************")
            print("\nWelcome to the Hostel Management System")
            print("\n**************************************")
            print("\n1. Admin Login")
            print("2. User Menu")
            print("3. Exit")
            print("\n(If you are not registered please contact admin Tp 081-3508715,E-mail usjp@.lk)")

            choice = input("\n-----> Enter your choice (1-3): ")

            if choice == '1':
                # Admin login
                if admin_login():
                    admin_menu(connection)
                else:
                    print("Failed to log in as admin.")
            elif choice == '2':
                # User actions (no login required for user)
                user_menu(connection)
            elif choice == '3':
                print("Exiting system...")
                break
            else:
                print("Invalid option, please try again.")
    else:
        print("Failed to connect to the database. Exiting program.")


main()
