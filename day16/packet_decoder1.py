class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id
        self.subpackets = []
        self.literal = None

    def add_subpackets(self, packets):
        self.subpackets += packets

    def add_subpacket(self, packet):
        self.subpackets.append(packet)

    def set_literal(self, literal):
        self.literal = literal

def convert_hex_to_binary(x):
    return format(int(x, 16), "0>4b")

def convert_transmission_to_binary(trans):
    binary = ""
    for t in trans:
        binary += convert_hex_to_binary(t)

    return binary

def convert_binary_string_to_hex(binstr):
    return (hex(int(binstr, 2))).lstrip("0x")

def read_literals(idx, binary):
    hex_number = ""
    while True:
        if binary[idx] == "1":
            idx += 1
            literal_binary = binary[idx:(idx+4)]
            hex_number += convert_binary_string_to_hex(literal_binary)
            idx += 4
        else:
            idx += 1
            literal_binary = binary[idx:(idx+4)]
            hex_number += convert_binary_string_to_hex(literal_binary)
            idx += 4
            break
    return hex_number, idx

def nothing_but_zeroes(binary):
    for i in binary:
        if i == "1":
            return False

    return True

def read_packets(binary):
    idx = 0
    packets = []
    while idx < (len(binary)-1):
        packet, idx = read_packet(idx, binary)
        packets.append(packet)
        if nothing_but_zeroes(binary[idx:]):
            break

    return packets

def read_packet(idx, binary):
    version = binary[idx:(idx+3)]
    idx += 3
    type_id = binary[idx:(idx+3)]
    idx += 3
    p = Packet(int(version, 2), int(type_id, 2))
    if (p.type_id == 4):
        hex_number, idx = read_literals(idx, binary)
        p.set_literal(int(hex_number, 16))
    else:
        if binary[idx] == "0":
            idx += 1
            packet_length = int(binary[idx:idx+15], 2)
            idx += 15
            p.add_subpackets(read_packets(binary[idx:idx+packet_length]))
            idx += packet_length
        else:
            idx += 1
            number_of_packets = int(binary[idx:idx+11], 2)
            idx += 11
            for i in range(0, number_of_packets):
                packet, idx = read_packet(idx, binary)
                p.add_subpacket(packet)
    return p, idx

def find_sum(packets):
    sum = 0
    for p in packets:
        sum += p.version
        if len(p.subpackets) != 0:
            sum += find_sum(p.subpackets)

    return sum


transmission = open("input16", "r").read()
transmission = transmission.rstrip()
binary = convert_transmission_to_binary(transmission)
idx = 0
packets = read_packets(binary)

print(find_sum(packets))



print("The answer is: ", "?")



