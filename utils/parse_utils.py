
def parse_32_bit_t(hex_str):
    b = bin(int(hex_str, 16))[2:].zfill(32)
    d = b[:5]
    M = b[5:9]
    y = b[9:15]
    h = b[15:20]
    m = b[20:26]
    s = b[26:]
    date = str(int(y, 2) + 2000) + " / " + str(int(M, 2)).zfill(2) + " / " + str(int(d, 2)).zfill(2)
    time = str(int(h, 2)).zfill(2) + " : " + str(int(m, 2)).zfill(2) + " : " + str(int(s, 2)).zfill(2)
    return [date, time]
