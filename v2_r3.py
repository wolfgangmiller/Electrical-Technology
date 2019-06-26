# Program Name: Circuit Analyzer - 2V & 3R
# Author: Maya Name
# Creation Date:
# Description: Calculates the voltage, current, and power for a   combination circuit with
# three resistor and two DC power sources.

import circuits
import math
import os


def circuit_currents(par, r, v):
    """ 
    Description Calculate currents for three resistor in combination circuit
    :param par: Parallel branch resistors - 2 float values in tuple
    :param r:   Series resistor as float
    :return:    Three currents as tuple of floats
    """
    print(f'Re is: {circuits.parallel(par)}')
    i1 = v/(circuits.parallel(par) + r)
    print(f'Series resistor is: {r}')
    print(f'Total Voltage is: {v}')
    print(f'Total current is: {i1}')
    v_par = v - (i1 * r)
    print(f'Parallel voltage is: {v_par}')
    return i1, v_par/par[1], v_par/par[0]




def main():
    os.system('cls')

    sources = 'opposing'
    r1 = 4    # Left resistor
    r2 = 2    # Center resistor
    r3 = 1    # Right resistor
    v1 = 28     # Left power source
    v2 = 7     # Right power source

    # res_tpl = (r1, r2, r3)
    par1_tpl = (r3, r2)  # Circuit 1 parallell branch
    print(par1_tpl)
    par2_tpl = (r1, r2)  # Circuit 2 parallel branch
    print(par2_tpl)

    # Calculate resistor currents assuming right power source removed (Circuit 1)
    currents1_tpl = circuit_currents(par1_tpl, r1, v1)
    for i in range(0, 3):
        print(f'Current on R{i + 1} is: {currents1_tpl[i]}')
    


    # Calculate resistor currents assuming right power source removed (Circuit 2)
    currents2_tpl = circuit_currents(par2_tpl, r3, v2)
    for i in range(0, 3):
        print(f'Current on R{i + 1} is: {currents2_tpl[i]}')

    current_lst = []

    if sources == 'opposing':
        current_lst.append(abs(currents1_tpl[0] - currents2_tpl[2]))
        current_lst.append(abs(currents1_tpl[1] + currents2_tpl[1]))
        current_lst.append(abs(currents1_tpl[2] - currents2_tpl[0]))
    else:
        pass

    for i in range(3):
        print(f'Resistor {i + 1} current is {round(current_lst[i], 3)}A')


if __name__ == "__main__":
    main()
