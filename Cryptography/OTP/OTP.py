import binascii
from random import getrandbits
import sys

class OTP:

    def __init__(self):
        self.flag = ''
        self.plaintext = ''
        self.key = ''
        self.ciphertext = ''
        self.toSave = ''

    def openFile(self):
        with open('flag.txt', 'r') as raw_flag:
            self.flag = raw_flag.read()
        with open('plaintext.txt', 'r') as raw_plaintext:
            self.plaintext = raw_plaintext.read()

    def convertToBits(self, plaintext):
        return "".join(format(ord(charX), 'b') for charX in plaintext)

    def createKey(self, plaintext):
        return bin(getrandbits(len(plaintext)))[2:].zfill(len(plaintext))

    def XOR(self, plaintext):
        ciphertext = []
        ciphertext.clear()
        for char1, char2 in zip(plaintext, self.key):
            ciphertext.append(str(int(int(char1) ^ int(char2))))
        return ''.join(ciphertext)

    def defineAndRun(self):
        self.openFile()
        if len(self.flag) != len(self.plaintext):
            print('[!] Flag and Plaintext are not of the same length.')
            print('[!] Padding Plaintext to achieve equal length.')
            value = len(self.flag) - len(self.plaintext)
            for counter in range(value):
                self.plaintext += '.'
            if len(self.flag) == len(self.plaintext):
                print('[+] Padding successful')
            else:
                sys.exit(0)
        else:
            print('[+] Flag and the Plaintext are of the same length.')
        self.plaintext = self.convertToBits(self.plaintext)
        self.flag = self.convertToBits(self.flag)
        self.key = self.createKey(self.flag)
        self.ciphertext = self.XOR(self.plaintext)
        temp = self.ciphertext.strip().encode('utf-8')
        temp = int(temp, 2)
        self.toSave = binascii.unhexlify('%x' % temp)
        self.saveTheCode('Plaintext.cryp')
        self.ciphertext = self.XOR(self.flag)
        self.toSave = binascii.unhexlify('%x' % int(self.ciphertext))
        self.saveTheCode('Flag.cryp')
        self.toSave()
        self.saveTheCode('Key.txt')


    def saveTheCode(self, name):
        with open(name, 'w') as writer:
            writer.write(str(self.toSave))


if __name__ == '__main__':
    x = OTP()
    x.defineAndRun()
