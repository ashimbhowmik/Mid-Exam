class Star_Cinema:
    __hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.__hall_list.append(hall)
        return hall


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = []
        row_seats=[]
        for i in range(self.__rows):
            row_seats.append(0)
        for j in range(self.__cols):
            self.__seats[id].append(row_seats)

    def book_seats(self, id, row, col):
        if id in self.__seats:
            if row > self.__rows or row < 1 or col > self.__cols or col < 1:
                print("\n-> Invalid Seat Number.\n")
            else:
                if self.__seats[id][row - 1][col - 1] == 1:
                    print("\n-> Seat Not Available. Please Try Another one.\n")
                else:
                    self.__seats[id][row - 1][col - 1] = 1
                    print(f"\n-> Seat ({row},{col}) Successfully Booked.\n")
        else:
            print("\n-> Invalid \n")

    def view_show_list(self):
        print("\n---------- Shows Airing Today ----------")
        for show in self.__show_list:
            print(f"Movies Name: {show[1]} \tShow Id: {show[0]} \tTime: {show[2]}")
        print("----------------------------------------\n")

    def view_available_seats(self, id):
        if id in self.__seats:
            count = 0
            print(f"\nSeats Matrix for Hall {self.__hall_no} Show {id}\n")
            for row in self.__seats[id]:
                print("[", end=" ")
                for col in row:
                    print(col, end=" ")
                    if col == "-":
                        count += 1
                print("] ")
            print("\n-> [ 0 ] Available, [ 1 ] Booked")
            print(f"-> Available Seats: {count}\n")
        else:
            print("\n-> Invalid Show ID\n")

counter = Star_Cinema().entry_hall(9, 9, 1)
counter.entry_show(1, "Solo Leveling", "10:00 AM")
counter.entry_show(2, "Classroom of the Elite", "11:00 PM")
counter.entry_show(3, "Dr. STONE", "12:00 PM")
counter.entry_show(4, "Naruto", "2:00 PM")
counter.entry_show(5, "Attack on Titan", "3:00 PM")

while True:
    print(
        """1. View All Show Today
2. View Available Seats
3. Book Ticket
4. Exit"""
        )

    op = int(input("Select Option: "))

    if op == 1:
        counter.view_show_list()
    elif op == 2:
        movie_id = int(input("Enter Show Id: "))
        counter.view_available_seats(movie_id)
    elif op == 3:
        show_id = int(input("Enter Show Id: "))
        tickets_count = int(input("Enter Number of Tickets: "))
        for i in range(tickets_count):
            print(f"\n{i+1} No Ticket")
            seat_row = int(input("Enter Row No: "))
            seat_col = int(input("Enter Column No: "))
            counter.book_seats(show_id, seat_row, seat_col)
    elif op == 4:
        print("----------Thank You----------\n")
        break
    else:
        print("----------Invalid. Please try again----------\n")