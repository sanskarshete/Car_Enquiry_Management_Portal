import functions
from tabulate import tabulate


def admin(cursor,conn):
    while True:
        admin_id = input("\nEnter your admin ID: ")
        password = input("Enter your admin password: ")
        if admin_id == "admin" and password == "admin":
            print("Admin login successful!")

            print("\n1. Add Car Details")
            print("2. Remove Car")
            print("3. update car")
            print("4. View enquieries")
            admin = input("Give your option: ")
            if admin == '1':
                print("\nAdd New Car : ")
                functions.add_car(cursor, conn)
                break
            elif admin == '2':
                print("Remove Car : ")
                functions.remove_car(cursor, conn)
                break
            elif admin == '3':
                print("Update Car Details : ")
                functions.update_car_details(cursor, conn)
                break
            elif admin == '4':
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
                """)

                rows = cursor.fetchall()

                headers = ["User ID", "Car ID", "Make", "Model", "Year of Make", "Mileage", "Enquiry"]

                print(tabulate(rows, headers=headers))

                cursor.close()
                conn.close()

                break
            else:
                print("Invalid. Please choose from 1, 2, 3 and 4")
        else:
            print("Invalid admin ID or password. Unauthorized access detected")
