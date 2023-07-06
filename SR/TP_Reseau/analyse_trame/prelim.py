import struct

chaine = b'\x04\x00\x00\x00\n\x10hi'
unmask_chaine = struct.unpack("!BLB2s",chaine)
print(unmask_chaine)

chaine2 = b'\x00\x01\x00\x02trois\x00\x00\x00\x04\x05\x00\x00\x00\x06'
unmask_chaine2 = struct.unpack("!HH5sLBL", chaine2)

print(unmask_chaine2)

print((237 >> 4) == 0b1110)