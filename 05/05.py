with open("input_05.txt", "r") as f:
    inp = f.readlines()

def divide(letter, seats):
    len_seats = len(seats)
    if letter in ["F", "L"]:
        return seats[:len_seats//2]
    if letter in ["B", "R"]:
        return seats[len_seats//2:]


def part1():
    seat_ids = []

    for seat in inp:
        rows = list(range(0,128))
        columns = list(range(0,8))
        #print(seat)
        for letter in seat:
            if letter in ["F", "B"]:
                rows = divide(letter, rows)
            if letter in ["L", "R"]:
                columns = divide(letter, columns)

        seat_id = rows[0]*8+columns[0]
        seat_ids.append(seat_id)

    print(max(seat_ids))

 
def part2():
    
    available_seats = []
    for row in range(0,128):
        for column in range(0,8):
            available_seats.append((row,column))
    seat_ids = []

    for seat in inp:
        rows = list(range(0,128))
        columns = list(range(0,8))
        for letter in seat:
            if letter in ["F", "B"]:
                rows = divide(letter, rows)
            if letter in ["L", "R"]:
                columns = divide(letter, columns)

        available_seats.remove((rows[0], columns[0]))
        seat_id = rows[0]*8+columns[0]
        seat_ids.append(seat_id)
    
    for row, column in available_seats:
        my_seat_id = row*8+column
        if my_seat_id + 1 in seat_ids and my_seat_id -1 in seat_ids:
            print(my_seat_id)
part1()
part2()