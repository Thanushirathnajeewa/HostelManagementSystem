from connection import connect_to_mysql
from rooms import check_availability

from datetime import datetime

def allocate_room():
    try:
        connection = connect_to_mysql()
        cursor = connection.cursor()
        
        # Fetch all students from the database
        cursor.execute("SELECT StudentID, FirstName, LastName FROM students")
        students = cursor.fetchall()
        
        # Display students (Optional)
        print("\nAvailable Students:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]} {student[2]}")
        
        # Input student ID
        student_id = input("Enter Student ID: ")

        # Check if the student ID exists in the database
        cursor.execute("SELECT StudentID FROM students WHERE StudentID = %s", (student_id,))
        student = cursor.fetchone()
        
        # If the student ID does not exist, show the message and exit
        if not student:
            print("(You are not registered. Please contact admin Tp 081-3508715,E-mail usjp@.lk.)")
            return  # Exit the function if student is not found

        # Call check_availability() to see available rooms
        available = check_availability(connection)
        if not available:
            print("No rooms are available.")
            return

        room_id = input("Enter Room ID to allocate: ")

        # Validate date input format
        try:
            allocating_date = datetime.strptime(input("Enter allocation date (YYYY-MM-DD): "), "%Y-%m-%d")
            leaving_date = datetime.strptime(input("Enter leaving date (YYYY-MM-DD): "), "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")
            return

        # Check if the room is available during the given dates
        cursor.execute("SELECT * FROM room_allocations WHERE RoomID = %s AND %s BETWEEN AllocationDate AND LeavingDate",
                       (room_id, allocating_date))
        existing_allocation = cursor.fetchone()
        if existing_allocation:
            print(f"Room {room_id} is already allocated during the specified dates.")
            return

        # Insert the allocation into the database
        cursor.execute(
            "INSERT INTO room_allocations (StudentID, RoomID, AllocationDate, LeavingDate) VALUES (%s, %s, %s, %s)",
            (student_id, room_id, allocating_date, leaving_date)
        )
        
        # Mark the room as occupied
        cursor.execute("UPDATE rooms SET Occupied = 1 WHERE RoomID = %s", (room_id,))
        
        # Commit the transaction
        connection.commit()
        print("Allocation saved successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
