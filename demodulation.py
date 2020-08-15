import numpy
import re

def iqData_input():
    '''
    purpose: retrieves iqData array

    return: ascii  >> returns iqData array
    '''
    iqData = numpy.fromfile(open("iqData.fc32"), dtype=numpy.complex64)
    return iqData

def iqData_2_angleData(iqData):
    '''
    purpose: converts file data to sin() and cos() data
    ex: [0.999-0.111j 0.999+0.111j 0.999-0.111j ...] -> [-0.65287, -0.65287, 0.55239, ...]

    para:   iqData      >> expects an array of iq data
    return: angleData   >> returns sin() and cos() data as a list of integers
    '''
    angleData = []
    for x in range(len(iqData)):
        temp = (numpy.angle([iqData[x - 1], iqData[x]]))
        angleData.append((temp[1] - temp[0]))
    return angleData

def angleData_2_expandedBinary(angleData):
    '''
    purpose: converts sin() and cos() data to a string of expanded 1s and 0s
    ex: [-0.65287, -0.65287, 0.55239, ...] -> 111110000000000111111111100000

    para:   angleData       >> expects a list of integers from sin() and cos() data
    return: expandedBinary  >> returns a string of expanded 1s and 0s
    '''
    expandedBinary = ''
    for samp in angleData:
        if samp > 0:
            expandedBinary += '1'
        else:
            expandedBinary += '0'
    return expandedBinary

def expandedBinary_2_binary(expandedBinary, sps):
    '''
    purpose: processes smooth_data based on sps to compress 1's and 0's. The function takes noise into consideration
    ex_1: 111110000000000111111111100000 -> 100110
    ex_2: 110110000100000111111011100000 -> 100110 (ex_1: with noise)

    para:   expandedBinary  >> expects a string of expanded 1's and 0's
    para:   sps             >> expects an integer greater than 0
    return: binary          >> returns a string of non-expanded 1's and 0's
    '''
    binary = ''
    for _ in range(0, len(expandedBinary), sps):
        sps_data = [int(item) for item in (list(expandedBinary[0:sps]))]
        expandedBinary = expandedBinary[sps:]
        if sum(sps_data) < int(sps/2):
            bit = "0"
        else:
            bit = "1"
        binary += bit
    return binary

def binary_2_package(binary):
    '''
    purpose: converts a string of 1s and 0s to package
    ex: 100110 -> (preamble)(STX)(ascii)(ETX)(endOfTransmission)

    para:   binary  >> expects a string of 1's and 0's
    return: package >> returns a string of ascii characters
    '''
    package = ''
    for _ in range(0, len(binary), 8):
        byte = binary[0:8]
        binary = binary[8:]
        dec = 0
        bit_val = 128
        for bit in byte:
            if bit == '1':
                dec += bit_val
            bit_val = bit_val / 2
        package += chr(int(dec))
    return package

def package_2_ascii(package):
    '''
    purpose: makes package information more readily processed
    ex: (preamble)(STX)(ascii)(ETX)(endOfTransmission) -> (ascii)

    para:   package  >> expects a string of ascii characters
    return: ascii    >> returns a string of ascii characters
    '''
    ascii = re.search('\x02(.+?)\x03', package).group(1)
    return ascii

def asciiOutput(ascii):
    '''
    purpose: outputs message

    para: ascii >> expects a string of ascii characters
    '''
    print(ascii)

a = iqData_input()
b = iqData_2_angleData(a)
c = angleData_2_expandedBinary(b)
d = 104
e = expandedBinary_2_binary(c, d)
f = binary_2_package(e)
g = package_2_ascii(f)
asciiOutput(g)