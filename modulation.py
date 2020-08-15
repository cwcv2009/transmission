import numpy

def asciiInput():
    '''
    purpose: prompts user for message

    return: ascii  >> returns a string of ascii characters
    '''
    ascii = str(input("Enter message: "))
    print("Transmitting message: " + ascii)
    return ascii

def ascii_2_package(ascii):
    '''
    purpose: makes message more easily identifiable during transmission
    ex: ascii -> (preamble)(STX)(ascii)(ETX)(endOfTransmission)

    para:   ascii   >> expects a string of ascii characters
    return: package >> returns a string of ascii characters
    '''
    preamble = '----------'
    endOfTransmission = '//////////'
    package = str(preamble + chr(2) + ascii + chr(3) + endOfTransmission)
    return package

def package_2_binary(package):
    '''
    purpose: converts package to a string of 1s and 0s
    ex: (preamble)(STX)(ascii)(ETX)(endOfTransmission) -> 100110

    para:   package >> expects a string of ascii characters
    return: binary  >> returns a string of ascii characters
    '''
    binary = ''
    for char in package:
        dec = ord(char)
        bit_val = 128
        for _ in range(8):
            if dec >= bit_val:
                binary += '1'
                dec = dec - bit_val
            else:
                binary += '0'
            bit_val = bit_val / 2
    return binary

def binary_2_expandedBinary(binary, samp_rate, baud_rate):
    '''
    purpose: processes binary based on samp_rate & buad_rate to expand 1's and 0's
    ex: 100110 -> 111110000000000111111111100000

    param:  binary          >> expects a string of 1's and 0's
    param:  samp_rate       >> expects an integer greater than or equal to 0
    param:  baud_rate       >> expects an integer greater than 0
    return: expandedBinary  >> returns a string of expanded 1's and 0's
    '''
    expandedBinary = ''
    sym_per_sec = int(samp_rate/baud_rate)
    for bit in binary:
       for _ in range(sym_per_sec):
           expandedBinary += bit
    return expandedBinary

def expandedBinary_2_iqData(expandedBinary, samp_rate, freq_shift):
    '''
    purpose: processes expandedBinary based on samp_rate & freq_shift to produce an .fc32 file
    ex: 111110000000000111111111100000 -> [0.999-0.111j 0.999+0.111j 0.999-0.111j ...]

    param:  expandedBinary  >> expects a string of 1's and 0's
    param:  samp_rate       >> expects an integer greater than 0
    param:  freq_shift      >> expects an integer greater than 0
    return: iqData          >> returns an iqData array
    '''
    iqData = []
    count = 1
    for samp in str(expandedBinary):
        time = float(count/samp_rate)
        if int(samp) == 1:
            freq = float(freq_shift)
        else:
            freq = float(-1 * freq_shift)
        wavelength = float(2 * numpy.pi * freq * time)
        iqData.append(numpy.cos(wavelength) + (1j * numpy.sin(wavelength)))
        count += 1
    iqData = numpy.asarray(iqData, "complex64")
    filename = "iqData.fc32"
    iqData.tofile(filename)
    return iqData

a = asciiInput()
b = ascii_2_package(a)
c = package_2_binary(b)
d = 1000000
e = 9600
f = binary_2_expandedBinary(c, d, e)
g = 1000000
h = 100000
expandedBinary_2_iqData(f, g, h)