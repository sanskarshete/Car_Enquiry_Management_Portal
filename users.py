
import functions


def users(cursor, conn):
    while True:
        print("\nPlease choose an option:")
        print("1. User login")
        print("2. New user registration")
        print("3. Exit")
        user = input("Give your option: ")

        if user == '1':
            if functions.user_login(cursor, conn):
                while True:
                    print("1. See all cars : ")
                    print("2. See cars applying filters :")
                    print("3. My enquiry : ")
                    print("4. Exit")
                    u_log = input("Give Option: ")

                    if u_log == '1':
                        functions.available_cars(cursor, conn)
                        print("1. Add car to enquiry : ")
                        print("2. Back to User Menu: ")
                        user_view = input("Give one option: ")

                        if user_view == '1':
                            functions.add_enquiry(cursor, conn)
                        elif user_view == '2':
                            print("Returning to User Menu.")
                            continue
                        else:
                            print("Invalid. Please choose from 1 and 2")


                    elif u_log == '2':
                        print("Following are the filter options: ")
                        print("1. Filter by make: ")
                        print("2. Filter by price range: ")
                        print("3. Filter by year of make: ")
                        print("4. Back to User Menu: ")
                        user_filter = input("Give one option: ")

                        if user_filter == '1':
                            functions.filter_by_make(cursor, conn)
                            print("1. Add car to enquiry : ")
                            print("2. Back to User Menu: ")
                            user_view = input("Give one option: ")

                            if user_view == '1':
                                functions.add_enquiry(cursor, conn)
                            elif user_view == '2':
                                print("Returning to User Menu.")
                                continue
                            else:
                                print("Invalid. Please choose from 1 and 2")

                        elif user_filter == '2':
                            functions.filter_by_price_range(cursor, conn)
                            print("1. Add car to enquiry : ")
                            print("2. Back to User Menu: ")
                            user_view = input("Give one option: ")

                            if user_view == '1':
                                functions.add_enquiry(cursor, conn)
                            elif user_view == '2':
                                print("Returning to User Menu.")
                                continue
                            else:
                                print("Invalid. Please choose from 1 and 2")

                        elif user_filter == '3':
                            functions.filter_by_year_of_make(cursor, conn)
                            print("1. Add car to enquiry : ")
                            print("2. Back to User Menu: ")
                            user_view = input("Give one option: ")

                            if user_view == '1':
                                functions.add_enquiry(cursor, conn)
                            elif user_view == '2':
                                print("Returning to User Menu.")
                                continue
                            else:
                                print("Invalid. Please choose from 1 and 2")
                        elif user_filter == '4':
                            print("Returning to User Menu.")
                            break
                        else:
                            print("Invalid. Please choose from 1, 2, 3, and 4")


                    elif u_log == '3':
                        functions.show_my_enquiry(cursor, conn)
                    elif u_log == '4':
                        break
                    else:
                        print("Invalid. Please choose from 1, 2, 3, and 4")

            else:
                print("Login failed. Please try again.")

        elif user == '2':
            functions.user_registration(cursor, conn)
            print("1. See all cars : ")
            print("2. See cars applying filters :")
            print("3. My enquiry : ")
            user_choice = input("Give Option: ")

            if user_choice == '1':
                functions.available_cars(cursor, conn)
                print("1. Add car to enquiry : ")
                print("2. Back to User Menu: ")
                user_view = input("Give one option: ")

                if user_view == '1':
                    functions.add_enquiry(cursor, conn)
                elif user_view == '2':
                    print("Returning to User Menu.")
                    break
                else:
                    print("Invalid. Please choose from 1 and 2")

            elif user_choice == '2':
                print("Following are the filter options: ")
                print("1. Filter by make: ")
                print("2. Filter by price range: ")
                print("3. Filter by year of make: ")
                print("4. Back to User Menu: ")
                user_filter = input("Give one option: ")

                if user_filter == '1':
                    functions.filter_by_make(cursor, conn)
                elif user_filter == '2':
                    functions.filter_by_price_range(cursor, conn)
                elif user_filter == '3':
                    functions.filter_by_year_of_make(cursor, conn)
                elif user_filter == '4':
                    print("Returning to User Menu.")
                    continue
                else:
                    print("Invalid. Please choose from 1, 2, 3, and 4")

            elif user_choice == '3':
                functions.show_my_enquiry(cursor, conn)
                break

        elif user == '3':
            functions.exit()
            break

        else:
            print("Invalid. Please choose from 1, 2, and 3.")