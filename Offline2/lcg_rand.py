# Class to generate random numbers using the linear congruential generator
# from L'Ecuyer (1990).
#
# The generator uses a modulus of 2^31 - 1, a multiplier of 24112, and
# an additive constant of 26143.
#
# The seed must be an integer between 1 and 2^31 - 2.  The first random
# number generated is always equal to the seed.
#
# The generator returns a pseudo-random number between 0 and 1.
#
# 
class Lcgrand:
    def __init__(self):
        self.MODLUS = 2 ** 31 - 1
        self.MULT1 = 24112
        self.MULT2 = 26143
        self.zrng = [1, 1973272912, 281629770, 20006270, 1280689831, 2096730329, 1933576050, 913566091, 246780520, 1363774876, 604901985, 1511192140, 1259851944, 824064364, 150493284, 242708531, 75253171, 1964472944, 1202299975, 233217322, 1911216000, 726370533, 403498145, 993232223, 1103205531, 762430696, 1922803170, 1385516923, 76271663, 413682397, 726466604, 336157058, 1432650381, 1120463904, 595778810, 877722890, 1046574445, 68911991, 2088367019, 748545416, 622401386, 2122378830, 640690903, 1774806513, 2132545692, 2079249579, 78130110, 852776735, 1187867272, 1351423507, 1645973084, 1997049139, 922510944, 2045512870, 898585771, 243649545, 1004818771, 773686062, 403188473, 372279877, 1901633463, 498067494, 2087759558, 493157915, 597104727, 1530940798, 1814496276, 536444882, 1663153658, 855503735, 67784357, 1432404475, 619691088, 119025595, 880802310, 176192644, 1116780070, 277854671, 1366580350, 1142483975, 2026948561, 1053920743, 786262391, 1792203830, 1494667770, 1923011392, 1433700034, 1244184613, 1147297105, 539712780, 1545929719, 190641742, 1645390429, 264907697, 620389253, 1502074852, 927711160, 364849192, 2049576050, 638580085, 547070247]
        self.stream = 0

    def lcgrand(self, stream):
        self.stream = stream % self.zrng.__len__()
        zi = self.zrng[self.stream]
        lowprd = (zi & 0xFFFF) * self.MULT1
        hi31 = (zi >> 16) * self.MULT1 + (lowprd >> 16)
        zi = ((lowprd & 0xFFFF) - self.MODLUS) + ((hi31 & 0x7FFF) << 16) + (hi31 >> 15)
        if (zi < 0): 
            zi += self.MODLUS
        lowprd = (zi & 0xFFFF) * self.MULT2
        hi31 = (zi >> 16) * self.MULT2 + (lowprd >> 16)
        zi = ((lowprd & 0xFFFF) - self.MODLUS) + ((hi31 & 0x7FFF) << 16) + (hi31 >> 15)
        if zi < 0: 
            zi += self.MODLUS
        self.zrng[self.stream] = zi
        return (zi >> 7 | 1) / 16777216.0

    def lcgrandst(self, zset, stream):
        self.zrng[stream] = zset

    def lcgrandgt(self, stream):
        return self.zrng[stream]