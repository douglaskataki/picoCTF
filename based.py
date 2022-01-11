import binascii

def main():

    #Example: bin = "01110011 01101111 01100011 01101011 01100101 01110100"
    bin = input("Binary: ")
    # takes out the spaces
    bin = bin.replace(" ","")
    n = int(bin,2)
    # transforms into ascii
    print(binascii.unhexlify("%x"%n))
    octal = input("Octal: ")
    # Example: octal = "163 154 165 144 147 145"
    octal = octal.split()
    for item in octal:
        print(chr(int(item,8)),end='')
    hex = input("Hex: ")
    #Example: hex = "6368616972"
    n = int(hex,16)
    print(binascii.unhexlify("%x"%n))

if __name__ == "__main__":
    main()
