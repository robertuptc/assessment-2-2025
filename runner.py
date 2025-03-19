from classes.store import Store
from classes.customer import Customer


new_store = Store()


def show_inventory():
    for movie in new_store.inventory:
        print(f"{movie.id}. {movie.title} || Copies: {movie.copies_available}")


def show_customers():
    for customer in new_store.all_customers:
        print(f"{customer.id}. {customer.first_name} {customer.last_name}")


def customer_current_rentals(id):
    for customer in new_store.all_customers:
        if customer.id == id:
            rentals = customer.current_video_rentals.split('/')
            print(f"\n{customer.first_name} current rentals:")
            for rental in rentals:
                print(f"- {rental}")


def add_customer():
    customer_data = {'id': None}
    customer_data['account_type'] = input('Select customer account type:\n1. sx\n2. sf\n3. px\n4. pf\n')
    if customer_data['account_type'] == '1' or customer_data['account_type'] == 'sx' :
        customer_data['account_type'] = 'sx'
    elif customer_data['account_type'] == '2' or customer_data['account_type'] == 'sf' :
        customer_data['account_type'] = 'sf'
    elif customer_data['account_type'] =='3' or customer_data['account_type'] == 'px' :
        customer_data['account_type'] = 'px'
    else:
        customer_data['account_type'] == 'pf'
    customer_data['first_name'] = input('Enter customer first name: ')
    customer_data['last_name'] = input('Enter customer last name: ')
    customer_data['current_video_rentals'] = ''

    Customer.add_new_customer(customer_data)


def rent_video(title, customer_id):
    title_lower = title.lower()

    def update_rentals_customers(customer, movie, condition):
        if condition == 'elif':
            customer.current_video_rentals = movie.title
            movie.copies_available = int(movie.copies_available) - 1
        else:
            customer.current_video_rentals += f"/{movie.title}"
            movie.copies_available = int(movie.copies_available) - 1
        return new_store.inventory
    
    for movie in new_store.inventory:
        if (movie.title).lower() == title_lower:
            if int(movie.copies_available) > 0:
                
                for customer in new_store.all_customers:
                    if int(customer.id) == int(customer_id):
                        current_rentals_total = len(customer.current_video_rentals.split('/')) if len(customer.current_video_rentals) != 0 else 0

                        if customer.account_type == "sx":
                            if current_rentals_total == 1:
                                return print("You can ONLY rent one movie at the time")
                            elif current_rentals_total == 0:
                                update_rentals_customers(customer, movie, 'elif')
                            else:
                                update_rentals_customers(customer, movie, 'else')
                        elif customer.account_type == "px":
                            if current_rentals_total == 3:
                                return print("You can ONLY rent three movies at the time")
                            elif current_rentals_total == 0:
                                update_rentals_customers(customer, movie, 'elif')
                            else:
                                update_rentals_customers(customer, movie, 'else')
                        elif customer.account_type == "sf":
                            if current_rentals_total == 1 or movie.rating == 'R':
                                return print("You can ONLY rent three movies at the time and they cannot be 'R' rating")
                            elif current_rentals_total == 0:
                                update_rentals_customers(customer, movie, 'elif')
                            else:
                                update_rentals_customers(customer, movie, 'else')
                        elif customer.account_type == "pf":
                            if current_rentals_total == 3 or movie.rating == 'R':
                                return print("You can ONLY rent three movies at the time and they cannot be 'R' rating")
                            elif current_rentals_total == 0:
                                update_rentals_customers(customer, movie, 'elif')
                            else:
                                update_rentals_customers(customer, movie, 'else')
                return print(f"'{movie.title}' has been rented!")
            else: 
                return print("\nMovie is rented out, come back soon!")
    print(f"\nWe currently don't have the '{title}' movie")

def return_video(title, id):
    movie_titled = title.title()

    for customer in new_store.all_customers:
        if customer.id == id:
            rented_copies = customer.current_video_rentals.split('/')
            if movie_titled in rented_copies:
                for movie in new_store.inventory:
                    if movie.title == movie_titled:
                        print(">>>>", movie.id, id, movie.id == id)
                        movie.copies_available = str(int(movie.copies_available) + 1)
                        rented_copies.remove(movie_titled)
                        rented_copies = '/'.join(rented_copies)
                        customer.current_video_rentals = rented_copies
                    
                    # return

while True:
    user_input = input("\n*** Welcome to Triton Woovies ***\n\nSelect one option:\n\n1. View current inventory\n2. View all customers\n3. View customer's current rented videos\n4. Add a new customer\n5. Rent video to customer\n6. Return a video from customer\n7. Exit\n")

    if user_input == '1':
        show_inventory()
    elif user_input == '2':
        show_customers()
    elif user_input == '3':
        customer_id = input("Please type customer ID: ")
        customer_current_rentals(customer_id)
    elif user_input == '4':
        add_customer()
    elif user_input == '5':
        title = input("What movie do you want to rent: \n")
        customer_id = input('Type customer ID: \n')
        rent_video(title, customer_id)
    elif user_input == '6':
        title = input("What movie do you want to return: \n")
        customer_id = input('Type customer ID: \n')
        return_video(title, customer_id)

    else:
        break
