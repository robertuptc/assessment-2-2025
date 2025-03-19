import csv, os

class Customer():
    def __init__(self, id, account_type, first_name, last_name, current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals


    @classmethod
    def all_customers(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, '../data/customers.csv')

        with open(path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(Customer(**row))
        return customers


    @classmethod
    def add_new_customer(cls, customer_data):
        new_id = int(cls.all_customers()[len(cls.all_customers()) - 1].id) + 1
        customer_data['id'] = new_id
        field_names = customer_data.keys()

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, '../data/customers.csv')

        with open(path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writerow(customer_data)
            cls.all_customers()