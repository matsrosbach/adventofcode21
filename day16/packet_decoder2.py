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

    def find_sum(self):
        for p in self.subpackets:
            p.find_sum()

        if self.type_id == 0:
            self.literal = 0
            for p in self.subpackets:
                self.literal += p.literal
        elif self.type_id == 1:
            self.literal = None
            for p in self.subpackets:
                if self.literal is None:
                    self.literal = p.literal
                else:
                    self.literal *= p.literal
        elif self.type_id == 2:
            self.literal = self.subpackets[0].literal
            for p in self.subpackets:
                if p.literal < self.literal:
                    self.literal = p.literal
        elif self.type_id == 3:
            self.literal = 0
            for p in self.subpackets:
                if p.literal > self.literal:
                    self.literal = p.literal
        elif self.type_id == 5:
            if self.subpackets[0].literal > self.subpackets[1].literal:
                self.literal = 1
            else:
                self.literal = 0
        elif self.type_id == 6:
            if self.subpackets[0].literal < self.subpackets[1].literal:
                self.literal = 1
            else:
                self.literal = 0
        elif self.type_id == 7:
            if self.subpackets[0].literal == self.subpackets[1].literal:
                self.literal = 1
            else:
                self.literal = 0


def convert_hex_to_binary(x):
    return format(int(x, 16), "0>4b")

def convert_transmission_to_binary(trans):
    binary = ""
    for t in trans:
        binary += convert_hex_to_binary(t)

    return binary

def convert_binary_string_to_hex(binstr):
    if int(binstr, 2) == 0:
        return "0"
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
    packets = []
    i = 0
    while i < (len(binary)):
        if nothing_but_zeroes(binary[i:]):
            break
        packet, i = read_packet(i, binary)
        packets.append(packet)

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


transmission = open("input16", "r").read()
transmission = transmission.rstrip()
binary = convert_transmission_to_binary(transmission)
idx = 0
packets = read_packets(binary)
for p in packets:
    p.find_sum()


print("The answer is: ", p.literal)



