from new import *
import psycopg2
from tabulate import tabulate


def user_registration(cursor, conn):
    while True:
        first_name = input("\nFirst Name: ").title()
        last_name = input("Last Name: ").title()
        phone_no = input("Phone Number: ")
        user_id = input("User ID: ")
        pin = input("Pin (at least 3 digits): ")

        if not (first_name.isalpha() and last_name.isalpha()):
            print("Error: First name and last name should contain only letters.")
        elif not (phone_no.isdigit() and len(phone_no) == 10):
            print("Error: Phone number must be a 10-digit number.")
        elif not (pin.isdigit() and len(pin) >= 3):
            print("Error: Pin should be at least 3 digits.")
        else:
            cursor.execute(
                "INSERT INTO customer_details(first_name, last_name, phone_no, user_id, pin)" 
                "VALUES(%s, %s, %s, %s, %s)",
                (first_name, last_name, phone_no, user_id, pin)
            )
            conn.commit()

            print("\nRegistration successful!")
            return True

    print("\nRegistration failed.")
    return False


def user_login(cursor, conn):
    user_id = input("\nUser ID: ")
    pin = input("Pin: ")

    cursor.execute("SELECT * FROM customer_details WHERE user_id=%s AND pin=%s", (user_id, pin))
    result = cursor.fetchone()

    if result is None:
        print("Login failed. User ID or Pin is incorrect.")
        return False
    else:
        print(f"\nLogin successful. Welcome, {result[0]}")
        return user_id


def available_cars(cursor, conn):
    cursor.execute(
        "SELECT * FROM available_cars_for_sale")
    cars = cursor.fetchall()
    for car in cars:
        mk = ['Make', car[1]]
        md = ['Model', car[2]]
        yr = ['Year', car[3]]
        mile = ['Mileage', car[4]]
        pri = ['Price', car[5]]
        caid = ['Car ID', car[0]]

        disp = [mk, md, yr, mile, pri, caid]
        print(tabulate(disp, tablefmt="grid"))
        print(" ")


        

def filter_by_make(cursor, conn):
    make = input("Enter the make of car : ").title()

    cursor.execute(
        "SELECT * FROM available_cars_for_sale WHERE make = %s",
        (make,)
    )
    cars = cursor.fetchall()

    if not cars:
        print(f"No cars found for the brand: {make}.")
    else:
        print(f"Cars available for the brand: {make}")
        for car in cars:
            mk = ['Make', car[1]]
            md = ['Model', car[2]]
            yr = ['Year', car[3]]
            mile = ['Mileage', car[4]]
            pri = ['Price', car[5]]
            caid = ['Car ID', car[0]]

            disp = [mk, md, yr, mile, pri, caid]
            print(tabulate(disp, tablefmt="grid"))
            print(" ")


def filter_by_price_range(cursor, conn):
    price_from = int(input("Enter minimum price of the car: "))
    price_to = int(input("Enter maximum price of the car: "))

    cursor.execute(
        "SELECT * FROM available_cars_for_sale WHERE price >= %s AND price <= %s",
        (price_from, price_to)
    )
    cars = cursor.fetchall()

    if not cars:
        print("No cars found in the specified price range.")
    else:
        print("Cars available in the specified price range:")
        for car in cars:
            mk = ['Make', car[1]]
            md = ['Model', car[2]]
            yr = ['Year', car[3]]
            mile = ['Mileage', car[4]]
            pri = ['Price', car[5]]
            caid = ['Car ID', car[0]]

            disp = [mk, md, yr, mile, pri, caid]
            print(tabulate(disp, tablefmt="grid"))
            print(" ")


def filter_by_year_of_make(cursor, conn):
    year_from = int(input("Enter the year from: "))
    year_to = int(input("Enter the year to: "))

    cursor.execute(
        "SELECT * FROM available_cars_for_sale WHERE year_of_make >= %s AND year_of_make <= %s",
        (year_from, year_to,))
    cars = cursor.fetchall()

    if not cars:
        print(f"No cars found for the year range")
    else:
        print(f"Cars available for the year range: {year_from} to {year_to}")
        for car in cars:
            mk = ['Make', car[1]]
            md = ['Model', car[2]]
            yr = ['Year', car[3]]
            mile = ['Mileage', car[4]]
            pri = ['Price', car[5]]
            caid = ['Car ID', car[0]]

            disp = [mk, md, yr, mile, pri, caid]
            print(tabulate(disp, tablefmt="grid"))
            print(" ")


def add_enquiry(cursor, conn):
    car_id = int(input("Enter car id: "))
    user_id = input("Enter user id: ")
    enquiry = input("Enquiry Statement: ")

    enquiry_data = {"car_id": car_id, "user_id": user_id, "enquiry": enquiry}

    cursor.execute(
        "INSERT INTO customer_enquiry(car_id, user_id, enquiry)" 
        "VALUES(%(car_id)s, %(user_id)s, %(enquiry)s)",
        enquiry_data
    )
    conn.commit()
    print("Enquiry Statement Added Successfully!")


def show_my_enquiry(cursor, conn):
    log_user =  input("user_id :")

    cursor.execute("""
        SELECT 
            customer_details.user_id, 
            available_cars_for_sale.car_id, 
            available_cars_for_sale.make, 
            available_cars_for_sale.car_model, 
            available_cars_for_sale.year_of_make, 
            available_cars_for_sale.mileage, 
            customer_enquiry.enquiry
        FROM 
            customer_enquiry
        JOIN 
            available_cars_for_sale ON customer_enquiry.car_id = available_cars_for_sale.car_id
        JOIN 
            customer_details ON customer_enquiry.user_id = customer_details.user_id
        WHERE 
            customer_details.user_id = %s
    """, (log_user,))

    rows = cursor.fetchall()

    headers = ["User ID", "Car ID", "Make", "Model", "Year of Make", "Mileage", "Enquiry"]

    print(tabulate(rows, headers=headers))

    cursor.close()
    conn.close()


def add_car(cursor,conn):
    make = input("\nEnter Make: ").title()
    car_model = input("Enter Model: ").title()
    year_of_make = int(input("Enter Year of Make (YYYY): "))
    mileage = int(input("Enter Mileage of the car (In KMs): "))
    price = int(input("Enter Expected price of car (In Rs): "))
    cursor.execute(
        "INSERT INTO available_cars_for_sale (make, car_model, year_of_make, mileage, price)" 
        "VALUES (%s, %s, %s, %s, %s)",
            (make, car_model, year_of_make, mileage, price)
    )
    conn.commit()
    print("\nCar Added Successfully")

def remove_car(cursor,conn):
    print("Removing Car ")
    available_cars(cursor, conn)
    car_id = int(input("Enter car_id to remove car : "))
    cursor.execute(
        "DELETE FROM available_cars_for_sale WHERE car_id = %s",
        (car_id,))
    conn.commit()
    print("Car removed successfully")


def update_car_details(cursor, conn):
    print("Update expected price: ")
    available_cars(cursor, conn)

    car_id = int(input("\nEnter Car ID to update price: "))
    price = int(input("Enter updated price (In Rs): "))

    update_data = {"price": price, "car_id": car_id}

    cursor.execute(
        "UPDATE available_cars_for_sale SET price = %(price)s WHERE car_id = %(car_id)s",
        update_data
    )
    conn.commit()
    print("\nPrice updated successfully")


def exit():
    print("Exiting the program. Goodbye!")
    return
