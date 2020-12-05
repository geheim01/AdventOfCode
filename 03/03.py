def load_input():
    with open("Day3_Input.txt", "r") as f:
        inp = f.readlines()
    return inp

def move(x, i):
    return x+i


def snowride(moves):
    traverse_map = load_input()
    height = len(traverse_map)
    weidth = len(traverse_map[0])
    print(height, weidth)
    counts = []
    
    
    #print(moves.pop)
    for x_move, y_move in moves:
        x = 0
        tree_count = 0
        y_counter = 0
        print(f'{x_move} to the right, {y_move} down')
        for row, line in enumerate(traverse_map):
            if y_move == 2:
                y_counter += 1
                if y_counter % 2 == 0:
                    continue
            if x >= 31:
                x = x-31
            if line[x] == "#":
                tree_count += 1
            x = move(x, x_move)
        print(f"Tree Count: {tree_count}")
        counts.append(tree_count)
    
    return multiply_treecounts(counts)

def multiply_treecounts(counts):
    result = 1
    for x in counts:
        result = x * result
    return result


def part1():


   snowride([(3,1)])



def part2():
    snowride([(1,1),(3,1), (5,1), (7,1), (1,2)])
    
part1()
part2()