#! /usr/bin/python


test_serials = [18, 42]
test_results = [[33,45], [21, 61]]

actual_serial = 7803

def test():
    x = 3
    y = 5
    serial_number = 8

    rack_id = x + 10
    power_level = y * rack_id
    power_level = power_level + serial_number
    power_level = power_level * rack_id
    hundreds_digit = (power_level // 100) % 10
    print(hundreds_digit - 5)

def compute_matrix(serial_number):
    # 300 x 300 matrix
    power_matrix = [[0]*301 for i in range(0, 301)]

    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            power_level = y * rack_id
            power_level = power_level + serial_number
            power_level = power_level * rack_id
            hundreds_digit = (power_level // 100) % 10
            power_matrix[x][y] = hundreds_digit - 5

    return power_matrix

def compute_3x3(matrix):
    max_power = -5 * 9 # lowest possible power is 3x3 grid of all -5s
    grid_id = None
    for x in range(1, 299):
        for y in range(1, 299):
            grid_power = 0
            for k in range(0, 3):
                for j in range(0, 3):
                    grid_power += matrix[x + k][y + j]
            if max_power < grid_power:
                max_power = grid_power
                grid_id = [x, y]
    return str(grid_id[0]) + "," + str(grid_id[1])

def compute_NxN(matrix):
    max_power = -100
    grid_id = None
    n = 1
    i = 299
    while i > (301 - 20):
        for x in range(1, i + 1):
            for y in range(1, i + 1):
                grid_power = 0
                for k in range(0, (301 - i)):
                    for j in range(0, (301 - i)):
                        grid_power += matrix[x + k][y + j]
                if max_power < grid_power:
                    max_power = grid_power
                    grid_id = [x, y]
                    n = 301 - i
        #print("result for size: " + str(301 - i) + ", grid: " + str(grid_id))
        i -= 1
    return str(grid_id[0]) + "," + str(grid_id[1]) + "," +  str(n)

print("(Day 11, Part 1) X,Y coordinates for best fuel: " + compute_3x3(compute_matrix(actual_serial)))
print("(Day 11, Part 2) X,Y,size coordinates for best fuel: " + compute_NxN(compute_matrix(actual_serial)))
