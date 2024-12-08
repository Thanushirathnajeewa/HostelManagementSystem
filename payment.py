from datetime import datetime

def collect_payment_details():
    """
    Collect payment details from the admin.

    Returns:
        A tuple containing payment details: (payment_id, student_id, invoice_refno, amount, payment_date, payment_method)
    """
    try:
        # Collect payment details from admin
        payment_id = int(input("Enter Payment ID: "))
        student_id = int(input("Enter Student ID: "))
        invoice_refno = input("Enter Invoice Reference Number: ")

        # Ensure that the amount is a valid float and greater than zero
        while True:
            try:
                amount = float(input("Enter Amount: "))
                if amount <= 0:
                    print("Amount must be greater than zero. Please try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for Amount.")

        # Ensure the date is in valid format
        payment_date_input = input("Enter Payment Date (YYYY-MM-DD): ")
        try:
            payment_date = datetime.strptime(payment_date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return None  # Return None if the date format is invalid

        payment_method = input("Enter Payment Method (e.g., Credit Card, PayPal, Bank Transfer): ")

        # Return the collected details as a tuple
        return (payment_id, student_id, invoice_refno, amount, payment_date, payment_method)

    except Exception as e:
        print(f"Error collecting payment details: {e}")
        return None


def insert_payment(connection, payment_id, student_id, invoice_refno, amount, payment_date, payment_method):
    """
    Insert payment details into the payments table.

    Args:
        connection: The MySQL database connection object.
        payment_id: The unique payment ID.
        student_id: The student's ID.
        invoice_refno: The reference number of the invoice.
        amount: The amount paid.
        payment_date: The date the payment was made.
        payment_method: The method of payment (e.g., Credit Card, PayPal, etc.)
    """
    query = """
    INSERT INTO payments (PaymentID, StudentID, InvoiceRefno, Amount, PaymentDate, PaymentMethod)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    
    # Creating a cursor object to interact with the database
    cursor = connection.cursor()
    
    try:
        # Execute the query with the passed parameters
        cursor.execute(query, (payment_id, student_id, invoice_refno, amount, payment_date, payment_method))
        
        # Commit the changes to the database
        connection.commit()
        
        print("Payment added successfully.")
    except Exception as e:
        # Handle exceptions (e.g., database errors)
        print(f"Error while adding payment: {e}")
    finally:
        # Ensure the cursor is closed after execution
        cursor.close()
