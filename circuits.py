# Program Name: AC Circuit Formulas
# Author: Maya Name
# Creation Date:
# Description: Common AC Circuit Formulas

import math, os
import tkinter as tk
from tkinter import messagebox

# Constants
deg_sym = '\xB0'
ang_sym = u'\u2220'
micro_sym = u'\u00B5'
omega_sym = u'\u03A9'
alpha_sym = u'\u03B1'
beta_sym = u'\u03B2'
pi_sym = u'\u03A9'
theta_sym = u'\u03B8'

# Validation functions

def inputFloatValue(m):
    """ 
    Description: reads in numeric input
    :param m:    entered numeric value
    :return:     valid numeric value as type float
    """
    while True:
        try:
            v = float(input(m))
        except ValueError:
            print("Input Error! Please enter valid real number.\n")
            continue
        else:
            return v

def validate_float(new_text): 
    #Validates Entry box entries are float values
    if not new_text: # the field is being cleared
        return True
    try:
        entered_number = float(new_text)
        return True
    except ValueError:
        tk.messagebox.showerror("Invalid entry!", "Please entry real numbers in value fields.")
        return False


# Voltage calculations

def angular_velocity(f):
    """ 
    Description: Calculate angular velocity (radians/second) given frequency 
    :param f:    Frequency as float
    :return:     Angular velocity
    """
    try:
       return 2 * math.pi * abs(float(f))
    except (ValueError):
        print('Error: Invalid arguments for angular_velocity(). Frequency must be numeric!')

def V_inst(v, f, t):
    """ 
    Description: Calculate  instantaneous voltage (Vi) 
    :param v:    Peak voltage as float
    :param f:    Frequency as float
    :param t:    time in seconds as float
    :return:     Instantaneous voltage
    """
    try:
       return float(v) * math.sin(angular_velocity(f) * float(t))
    except (ValueError):
        print('Error: Invalid arguments for v_inst(). Values must be numeric!')


def v_peak(v):
    """ 
    Description: Calculate peak Voltage given RMS Voltage 
    :param v:    RMS Voltage as float
    :return:     Peak Voltage
    """
    try:
       return float(v) * math.sqrt(2)
    except (ValueError):
        print('Error: Invalid arguments for v_peak(). Values must be numeric!')

def v_rms(v):
    """ 
    Description: Calculate rms Voltage given peak Voltage 
    :param v:    Peak Voltage as float
    :return:     RMS Voltage
    """
    try:
       return float(v) / math.sqrt(2)
    except (ValueError):
        print('Error: Invalid arguments for v_rms(). Values must be numeric!')


# Impedance formulas

def z_vs(v, s):
    """ 
    Description: Calculate Impedance given Voltage and Apparent Power 
    :param v:    Voltage as float
    :param s:    Apparent Power as float
    :return:     Impedance
    """
    try:
       return pow(float(v), 2) / float(s)
    except (ValueError):
        print('Error: Invalid arguments for z_vs(). Must be numeric!')
    except (ZeroDivisionError):
        print('Error: Apparent power cannot be zero')


def z_vi(v, i):
    """ 
    Description: Calculate Impedance given Voltage and Current 
    :param v:    Voltage as float
    :param i:    Current as float
    :return:     Impedance
    """
    try:
       return float(v) / float(i)
    except (ValueError):
        print('Error: Invalid arguments for z_vi(). Must be numeric!')
    except (ZeroDivisionError):
        print('Error: Current cannot be zero')


def z_is(i, s):
    """ 
    Description: Calculate Impedance given Voltage and Apparent Power 
    :param i:    Current as float
    :param s:    Apparent Power as float
    :return:     Impedance
    """
    try:
       return float(s) / pow(float(i), 2)
    except (ValueError):
        print('Error: Invalid arguments for z_is(). Must be numeric!')
    except (ZeroDivisionError):
        print('Error: Current cannot be zero')


def z_par_rlc(r, xl, xc):
    """ 
    Description: Calculate impedance for parallel RLC numeric values
    :param r:    resistance 
    :param xl:   inductive reactance
    :param xc:   capacitive reactance
    :return:     impedance
    """
    # Convert values to floats. Raise error if not
    try:
        error = False
        r = float(r)
        xl = float(xl)
        xc = float(xc)
    except ValueError:
        error = True
        print('Error: Invalid arguments for parallel_z(). Requires numeric values') 
   
    if error:
        pass
    else:
        if r > 0:
            if xl == 0 or xc == 0: # avoid divide by zero
                x = xl + xc
                z = (r * x)/(math.sqrt(r**2 + x**2))
                return z           
            else:
                z = 1/(math.sqrt((1/r)**2 + (1/xl - 1/xc)**2))
                return z    
        else:
            print('Positive resistance value required.')



# Series and Parallel circuit formulas
def series(lst):
    """ 
    Description: Calculates equivalent resistance for series resistors
    :param lst:  list of positive non-zero numeric values
    :return:     x - equivalent resistance
    """
    x = 0
    for r in lst:
        try:
            x += float(r)
            error = False
        except ValueError:
            print('Error: Invalid list item argument for series(). Must be numeric')
            error = True
            break
        
    if error:
        return None
    else:
        return x

    
def parallel(lst):
    """ 
    Description: Calculates equivalent resistance for parallel resistors
    :param lst:  list of positive non-zero numeric values
    :return:     x - equivalent resistance
    """
    x = 0
    for r in lst:
        try:
            x += 1/float(r)
            error = False
        except (ValueError, ZeroDivisionError):
            print('Error: Invalid list item argument for parallel(). Must be nom zero numeric')
            error = True
            break
    if error:
        return None
    else:
        return 1/x





def input__flt_lst(m):
    """ 
    Description: Create list from entered float values: 0 ends input
    :param m:    Input message
    :return:     value list
    """
    lst = []    # Value list

    while True:
        print(m + str(len(lst) + 1) + " value or Enter 0 to stop")
        v = float(inputFloatValue(''))
        if v == 0.0:
            break
        lst.append(v)
    return lst


def ind_react(l, f):
    """ 
    Description: Calculate inductive reactance
    :param l:    inductance
    :param f:    frequency
    :return:     inductive reactance
    """
    try:
        return 2*math.pi*float(f)*float(l)
    except ValueError:
        print('Error: Invalid arguments for ind_react(). Must be numeric!')
        

def cap_react(c, f):
    """ 
    Description: Calculate capacitive reactance (Xc)
    :param c:    capacitance
    :param f:    frequency
    :return:     capacitive reactance
    """
    try:
        return 1/(2*math.pi*float(f)*float(c))
    except (ValueError):
        print('Error: Invalid arguments for cap_react(). Must be numeric plus c and f not zero')
    except (ZeroDivisionError):
        print('Error: Capacitance and frequency cannot be zero')


def capacitance(x, f):
    """ 
    Description: Calculate capacitance (C)
    :param x:    capacitive reactance
    :param f:    frequency
    :return:     capacitance
    """
    try:
        return 1/(2*math.pi*float(f)*float(x))
    except (ValueError, ZeroDivisionError):
        print('Error: Invalid arguments for cap_react(). Must be numeric plus c and f not zero')



def get_polar(r, i):
    """ 
    Description: Calculate magnitude and phase angle 
    :param r:    real (x axis) value
    :param i:    imaginary (y axis) value
    :return:     phasor tuple
    """
    # Convert values to floats. Raise error if not
    try:
        error = False
        r = float(r)
        i = float(i)
    except ValueError:
        error = True
        print('Error: Invalid arguments for get_polar(). Requires numeric values') 

    if error:
        pass
    else:
        # Calculate magnitude
        m = math.sqrt(r**2 + i**2)

        # Calculate phase angle for zero an non zero values
        if r != 0 and i != 0:
            pa = math.degrees(math.atan(i/r))                       
        elif r == 0:
            pa = 90.0
        elif i == 0:
            pa = 0.0  
    
    # Return tuple values
    if error:
        return None
    else: # Correct for proper quadrant
        if r < 0 and i > 0:
            return m, 180 + pa
        elif r > 0 and i < 0:
            return m, 360 + pa
        elif r < 0 and i < 0:
            return m, 180 + pa
        else: # Quadrant 1
            return m, pa
    
# Power formulas: Use for Apparent, True, and Reactive Power
def s_ie(i, e):
    """ 
    Description: Calculate Apparent Power given Current and Voltage 
    :param i:    Current as float
    :param e:    Voltage as float
    :return:     Apparent Power
    """
    try:
       return float(i) * float(e)
    except ValueError:
        print('Error: Invalid arguments for s_ie(). Must be numeric!')


def s_ir(i, r):
    """ 
    Description: Calculate Apparent Power given Current and Resistance 
    :param i:    Current as float
    :param r:    Resistance as float
    :return:     Apparent Power
    """
    try:
       return pow(float(i), 2) * float(r)
    except ValueError:
        print('Error: Invalid arguments for s_ir(). Must be numeric!')    
    

def s_er(e, r):
    """ 
    Description: Calculate Apparent Power given Voltage and Resistance 
    :param e:    Voltage as float
    :param r:    Resistance as float
    :return:     Apparent Power
    """
    try:
        return pow(float(e), 2) / float(r)
    except (ValueError, ZeroDivisionError):
        print('Error: Invalid arguments for s_er(). Must be numeric and r not zero')
 

def s_tprp(tp, rp):
    """ 
    Description:  Calculate Apparent Power given True Power and Reactive Power
    :param tp:    True Power as float
    :param rp:    Reactive Power as float
    :return:      Apparent Power
    """
    try:
        return math.sqrt(pow(float(tp),2) + pow(float(rp), 2))
    except ValueError:
        print('Error: Invalid arguments for s_ir(). Must be numeric!') 


def s_ppf(p, pf):
    """ 
    Description: Calculate Apparent Power given True Power and pf 
    :param p:    True Power as float
    :param pf:   Power Factor as float
    :return:     Reactive Power
    """
    try:
       return float(p) / float(pf)
    except (ValueError, ZeroDivisionError):
        print('Error: Invalid arguments for q_ps(). Must be numeric!')


def q_ps(p, s):
    """ 
    Description: Calculate Reactive Power given True and Apparent Power 
    :param i:    True Power as float
    :param e:    Apparent Power as float
    :return:     Reactive Power
    """
    try:
       return math.sqrt(pow(float(s), 2) - pow(float(p), 2))
    except ValueError:
        print('Error: Invalid arguments for q_ps(). Must be numeric!')




def get_pf(p, s):
    """ 
    Description:  Calculates power factor
    :param p:     True power (watts) as float
    :param s:     Apparent power as float
    :return:      Power factor as float
    """
    try:
        return float(p) / float(s)
    except ValueError:
        print('Error: Invalid arguments for get_pf(). Must be numeric!') 



def str_polar(t, r):
    """ 
    Description:  Creates polar formatted string from polar tuple
    :param t:     polar tuple value 
    :param r:     number of decimal places to round
    :return:      Formatted string
    """
    return f'{round(t[0], r)} ' + ang_sym + f' {round(t[1], r)}' + deg_sym       
        

def get_eng_val_tpl(v, d = 4):
    """
    Convert a float to engineering notation, with specified
    significant digits and units
    :param v: float point number
    :param d: number of significant digits - default is 4

    :return: tuple of scaled value and suffix  
    
    """

    # Practical component suffixes
    _SUFFIX = ["p", "n", "u", "m", "", "k", "M", "G"]
    # Offset to unit multiplier (no suffix)

    _UNIT_OFFSET = 4 # Use if no suffix is needed



    if v == 0:     # Returns zero and no suffix if zero, Zero would cause error in log10()
        return 0, ''

    # Get scaled value and exponent
    mant, exp = get_exp10(abs(v))

    # Normalize and round to significant digits
    r = round(mant, d)

    # Convert back
    x1 = r * math.pow(10.0, exp)

    # Get int for ENG exp to use for suffix index
    p = int(math.floor(math.log10(abs(x1))))
    p3 = p // 3

    # Create suffix index
    si = p3 + _UNIT_OFFSET

    # Create return ENG root value
    r_val = x1 / math.pow(10.0, 3*p3)

    # display ENG values
    if v < 0:
        r_val = -r_val
        return r_val, _SUFFIX[si]
    else:
        return r_val, _SUFFIX[si]

         
def get_exp10(v):
    """
    Returns mantissa and exponent (base 10)
    :param v: floating point number
    :return: tuple (mantissa, exponent)
    """
    exp = math.floor(math.log10(v))
    return v/10**exp, exp
 




def main(): 
    os.system('cls')
    
    print(z_vs(120, 0))
    # v, u = get_eng_val_tpl(.00456783)
    # print(f'Voltage = {v} {u}V')
    
    

if __name__ == "__main__": main()