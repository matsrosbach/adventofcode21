class Scanner_Result:
    def __init__(self, scanner_number, rotation, orientation, x_offset, y_offset, z_offset):
        self.scanner_number = scanner_number
        self.rotation = rotation
        self.orientation = orientation
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.z_offset = z_offset


def read_all_scanners_from_input(input_file):
    input = open(input_file, "r").readlines()

    for i in range(0, len(input)):
        input[i] = input[i].rstrip()

    scanners = []
    scanner_number = -1
    for row in input:
        if row.startswith("---"):
            scanner_number += 1
            scanners.append([])
        elif row == "":
            continue
        else:
            scanners[scanner_number].append([int(x) for x in row.split(",")])

    return scanners


def get_no_of_overlaps(s1, s2, x_offset, y_offset, z_offset):
    no_overlaps = 0
    for b1 in s1:
        for b2 in s2:
            b2_aligned = [b2[0] + x_offset, b2[1] + y_offset, b2[2] + z_offset]
            if b1 == b2_aligned:
                no_overlaps += 1

    return no_overlaps


def rotate_scanner(scanner, rotation, orientation):
    rotated_scanner = []
    for beacon in scanner:
        rotated_scanner.append(
            [beacon[orientation[0]] * rotation[orientation[0]], beacon[orientation[1]] * rotation[orientation[1]],
             beacon[orientation[2]] * rotation[orientation[2]]])

    return rotated_scanner


# Check if 12 beacons overlap
def check_if_overlaps(scanner1, scanner2):
    rotations = [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, -1], [-1, -1, 1]]
    orientations = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    for rotation in rotations:
        for orientation in orientations:
            for beacon1 in scanner1:
                rotated_scanner2 = rotate_scanner(scanner2, rotation, orientation)
                for beacon2 in rotated_scanner2:
                    x_offset = beacon1[0] - beacon2[0]
                    y_offset = beacon1[1] - beacon2[1]
                    z_offset = beacon1[2] - beacon2[2]
                    overlaps = get_no_of_overlaps(scanner1, rotated_scanner2, x_offset, y_offset, z_offset)
                    if overlaps >= 12:
                        return x_offset, y_offset, z_offset, rotation, orientation

    return None, None, None, None, None


def already_found(idx, results):
    for result in results:
        if result.scanner_number == idx:
            return True
    return False

def beacon_exists(beacon, list):
    for element in list:
        if element == beacon:
            return True

    return False

scanners = read_all_scanners_from_input("input19")
results = []
results.append(Scanner_Result(0, [-1, -1, -1], [0, 1, 2], 0, 0, 0))
while len(results) < len(scanners):
    for scanner_idx in range(1, len(scanners)):
        if already_found(scanner_idx, results):
            continue
        for result in results:
            rotated_result = rotate_scanner(scanners[result.scanner_number], result.rotation, result.orientation)
            x_offset, y_offset, z_offset, rotation, orientation = check_if_overlaps(rotated_result,
                                                                                    scanners[scanner_idx])
            if x_offset is not None:
                results.append(Scanner_Result(scanner_idx, rotation, orientation, result.x_offset - x_offset,
                                              result.y_offset - y_offset, result.z_offset - z_offset))
                print(result.x_offset - x_offset, result.y_offset - y_offset, result.z_offset - z_offset, rotation,
                      orientation)
                break

beacons = []
for result in results:
    scanner = scanners[result.scanner_number]
    orientation = result.orientation
    rotation = result.rotation
    x_offset = result.x_offset
    y_offset = result.y_offset
    z_offset = result.z_offset

    for beacon in scanner:
        new_beacon = [beacon[orientation[0]] * rotation[orientation[0]] * -1 + x_offset, beacon[orientation[1]] * rotation[orientation[1]] * -1 + y_offset,
                      beacon[orientation[2]] * rotation[orientation[2]] * -1 + z_offset]
        if not beacon_exists(new_beacon, beacons):
            beacons.append(new_beacon)
            print("Scanner: ", result.scanner_number, " beacon: ", new_beacon)

print()
print("The answer is: ", len(beacons))
