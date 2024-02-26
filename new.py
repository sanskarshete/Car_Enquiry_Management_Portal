import psycopg2
import functions
import users
import admin
from tabulate import tabulate

def connect_to_database():
        conn = psycopg2.connect(
            host="localhost",
            database="Car_Selling",
            user="postgres",
            password="Sshete@ict23",
            port=5432
        )
        if conn:
            print("Connection Successful!")
            return conn
        else:
            print("Error connecting to the database")
            return None


def main():
    conn = connect_to_database()

    if conn is None:
        return

    cursor = conn.cursor()

    print("--------------------------------------------- WELCOME TO S.K. LUXURY CARS ---------------------------------------------")
    print("\nWelcome! Please choose an option:")
    print("1. USER")
    print("2. ADMIN")
    print("3. EXIT")
    choice = input("Enter your choice: ")
    while True:
        if choice == '1':
            users(cursor, conn)
        elif choice == '2':
            admin(cursor, conn)
        elif choice == '3':
            print("EXITING THE PROGRAM. GOODBYE!")
            conn.close()
        return
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
