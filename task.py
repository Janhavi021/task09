class TourPlanner:
    
    def __init__(self, company_name):
       
        self.company_name = company_name

        self.tour_packages = [
            {'name': 'ujjain', 'price': 12000},
            {'name': 'kedarnath', 'price': 15000},
            {'name': 'ayoddha', 'price': 2000}
        ]

    def book(self, person_name, number_of_people, package_name):

        found_package = None

        if package_name == "ujjain":
            found_package = self.tour_packages[0]
        elif package_name == "kedarnath":
            found_package = self.tour_packages[1]
        elif package_name == "ayoddha":
            found_package = self.tour_packages[2]

        if found_package != None:
            price_per_person = found_package['price']
            total_bill = number_of_people * price_per_person

            print("--- BILL ---")
            print("Company:", self.company_name)
            print("Customer:", person_name)
            print("Package:", package_name)
            print("Total People:", number_of_people)
            print("Total Price: rs", total_bill)
            
        else:
            print("Package not found!")


my_tour = TourPlanner("Jay shree Ram Travels")


my_tour.book(" siya janak", 3, "ayoddha")