def get_nibbles(byte):
    high = byte >> 4
    low = byte & 0x0f
    return (high, low)

input_file_counter = 0
input_file = open("q1_encr.txt").read()

reg = [0] * 16
counter = 0
flag = 0
opened = True
eof_flag = 0

def process_bytes(command, value):
    global counter
    global flag
    global input_file_counter
    global eof_flag
    global opened
    if command is 1:
        res = reg[get_nibbles(value)[1]] + 1
        reg[get_nibbles(value)[1]] = res
        if res is 0: flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 2:
        res = reg[get_nibbles(value)[1]] - 1
        reg[get_nibbles(value)[1]] = res
        if res is 0: flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 3:
        reg[get_nibbles(value)[1]] = reg[get_nibbles(value)[0]]
        counter += 2
    elif command is 4:
        reg[0] = value
        counter += 2
    elif command is 5:
        res = reg[get_nibbles(value)[1]] << 1
        reg[get_nibbles(value)[1]] = res
        if res is 0: flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 6:
        res = reg[get_nibbles(value)[1]] >> 1
        reg[get_nibbles(value)[1]] = res
        if res is 0:
            flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 7:
        counter += value
    elif command is 8:
        if flag == 1:
            counter += value
        else:
            counter += 2
    elif command is 9:
        if flag == 0:
            counter += value
        else:
            counter += 2
    elif command is 10:
        if eof_flag == 1:
            counter += value
        else:
            counter += 2
    elif command is 11:

        opened = False
        counter += 2
        return
    elif command is 12:
        res = reg[get_nibbles(value)[1]] + reg[get_nibbles(value)[0]]
        reg[get_nibbles(value)[1]] = res
        if res is 0:
            flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 13:
        res = int(reg[get_nibbles(value)[1]]) - int(reg[get_nibbles(value)[0]])
        reg[get_nibbles(value)[1]] = res
        if res is 0:
            flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 14:
        res = reg[get_nibbles(value)[1]] ^ reg[get_nibbles(value)[0]]
        reg[get_nibbles(value)[1]] = res
        if res is 0:
            flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 15:
        res = reg[get_nibbles(value)[1]] | reg[get_nibbles(value)[0]]
        reg[get_nibbles(value)[1]] = res
        if res is 0:
            flag = 1
        else:
            flag = 0
        counter += 2
    elif command is 16:
        reg[get_nibbles(value)[1]] = ord(input_file[input_file_counter])
        if input_file_counter == len(input_file)-1:
            eof_flag = 1
        else:
            eof_flag = 0
            input_file_counter += 1

        counter += 2
    elif command is 17:
        f = open("output.txt", "a+")
        f.write(chr(reg[get_nibbles(value)[1]]))
        f.close()
        counter += 2


def decode():
    print("Working...")
    bytes_read = open("decryptor.bin", "rb").read()
    global opened
    global counter
    while opened:
        if not opened:
            break
        process_bytes(bytes_read[counter], int.from_bytes(bytes_read[counter+1].to_bytes(1, byteorder='little'), byteorder='little', signed=True))
        if counter > len(bytes_read):
            counter %= len(bytes_read)
        if opened == False:
            print("...done!")
