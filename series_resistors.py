# Program Name: Series Total Resistance
# Author: Maya Name
# Creation Date: 12/28/2018
# Description: Calculates total resistance in a series circut.

import os

def inputFloatValue(m):
    while True:
        try:
            v = float(input(m))
        except ValueError:
            print("Input Error! Please enter valid real number.\n")
            continue
        else:
            return v
            

def inputIntValue(m):
    while True:
        try:
            v = int(input(m))
        except ValueError:
            print("Input Error! Please enter valid whole number.\n")
            continue
        else:
            return v
            



def inputStrValue(m):
    v = input(m)
    return v.strip()





def main(): 
    os.system('cls')
    seriesRt = []           # Resistor values
    # voltDropR = []          # Resistor voltage drop values
    # powerR = []             # Resistor power values
    totalResistance = 0
    voltage = 12

    print('Series Circuit Calculator\n')

    while True:
        print("Enter value for resistor " + str(len(seriesRt) + 1) + " or ENTER 0 stop")
        resistor = inputFloatValue("")
        if resistor == 0:
            break
        seriesRt.append(resistor)  # Concatenate list
    
    print(f"\nBased on a {voltage}V source, circuit values are: ")
    for resistor in seriesRt:
     #   print(resistor)
        totalResistance = totalResistance + resistor
    current = voltage/totalResistance
    power = voltage * current
    print("\nTotal resistance is: " + str(round(totalResistance, 3)) + " ohms.")
    print("Total current is: " + str(round(current, 3)) + " amps.")
    print("Total power is: " + str(round(power, 3)) + " watts.\n")
    print("Values per resistor: \n")


    for resistor in seriesRt:
        vDrop = (resistor/totalResistance)*voltage
        pDis = current * vDrop
        print("Voltage drop on " + str(resistor) + " ohm resistor " + str(seriesRt.index(resistor) + 1) + " is: "  + \
        str(round(vDrop, 3)) + " volts")
        print("Power dissipated on " + str(resistor) + " ohm resistor " + str(seriesRt.index(resistor) + 1) + " is: "  + \
        str(round(pDis, 3)) + " watts\n")
    #     voltDropR.append(vDrop)
    #     powerR.append(current * vDrop)
    # for vDrop in voltDropR:
    #     print(vDrop)
    # for pdis in powerR:
    #     print(pdis)
        


if __name__ == "__main__":
    main()