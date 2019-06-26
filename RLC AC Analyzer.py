"""
Program Name:
Author: Maya Name
Creation Date:
Description:

"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cmath, math
import matplotlib.pyplot as plt
import numpy as np


class App:

    def __init__(self, master):
        #Define window properties
        master.title("RLC Circuit Analyzer")
        master.minsize(400,300)
        master.iconbitmap(self, default='./Templates/wolftrack.ico')

        #Define widget values
        self.resistor_str = tk.StringVar(value = '0.0')
        self.capacitor_str = tk.StringVar(value = '0.0')
        self.inductor_str = tk.StringVar(value = '0.0')
        self.UoM_str = tk.StringVar()

        
        #Display window layout
        self.init_IO(master)

    def init_IO(self, m):
        #Create window layout with m being App master

        #Define constants
        series_type_menu = ('Impedance', 'Power', 'Voltage')
        parallel_type_menu = ('Admittance', 'Current', 'Impedance', 'Power')


        #basic layout frames
        self.header_frm = ttk.Frame(m)
        self.header_frm.pack()
        self.body_frm = ttk.Frame(m)
        self.body_frm.pack()
        self.footer_frm = ttk.Frame(m)
        self.footer_frm.pack()

        #Header section layout
        ttk.Label(self.header_frm, text = 'This program calculates the resultant phasor and phase angle for RC, RL, and RLC series and parallel circuits.', wraplength=300).grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'e')

        #Body section layout
        vcmd_f = m.register(self.validate_float) # wrapper for the Entry box validation
        
        ttk.Label(self.body_frm, text = 'Select circuit and value type. Then enter values.').grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'e')
        
        #Frame content for circuit and value selection
        circuit_type_int = tk.IntVar()  #Int value from rbtns for circuit type

        def get_parallel_Z(r, xl, xc):
   
            if r > 0:
                if xl == 0 or xc == 0:
                    x = xl + xc
                    z = (r * x)/(math.sqrt(r**2 + x**2))
                    print(f'z1 total impedance is: {z}')
                    return z           
                else:
                    z = 1/(math.sqrt((1/r)**2 + (1/xl - 1/xc)**2))
                    print(f'z3 total impedance is: {z}') 
                    return z    
            else:
                print('Positive resistance value required.')

        
        def set_series_menu(): #Sets the Value combo box menu based on circuit type
            if circuit_type_int.get() == 1: 
                r_val_cmb.configure(state = 'normal', value = series_type_menu)
            elif circuit_type_int.get() == 2:
                r_val_cmb.configure(state = 'normal', value = parallel_type_menu)
           

        def clear_vals(): #Resets Entry box values and Results label to defaults
            self.resistor_str.set('0.0')
            self.capacitor_str.set('0.0')
            self.inductor_str.set('0.0')
            self.results_lbl.configure(text = f'Phasor magnituude; {float(self.float_ent1.get()):.3f}  Phase angle: {float(self.float_ent2.get()):.3f}')

        def get_UoM(): #Returns UoM for selected value type
            omega_sym = u'\u03A9'

            if r_val_cmb.get() == 'Admittance':
                return 'S'
            elif r_val_cmb.get() == 'Current':
                return 'A'   
            elif r_val_cmb.get() == 'Impedance':
                return omega_sym
            elif r_val_cmb.get() == 'Power':
                return 'VA'
            elif r_val_cmb.get() == 'Voltage':
                return 'V'
           


        def calculate(): #Calculates phasor and phase angle, then displays results
            deg_sym = '\xB0'

            print(f'Circuit selected is {circuit_type_int.get()}')
            print(f'Value type {r_val_cmb.get()} was selected')

            #Calculations for series circuit
            if circuit_type_int.get() == 1: #Calculation for series circuit

                if r_val_cmb.get() != '': #Value type must be selected
                    res_phasor = complex(float(self.float_ent1.get()), 0)
                    print(res_phasor)

                    reactive_phasor = complex(0, float(self.float_ent2.get()) - float(self.float_ent3.get()))
                    print(reactive_phasor)
            
                    result_phasor = res_phasor + reactive_phasor
                    print(result_phasor)

                    print(f'combo box value: {r_val_cmb.get()}')
            
                    get_UoM()

                    print(f'Phasor magnitude : {abs(result_phasor):.3f}{get_UoM()} and phase angle is {math.degrees(cmath.phase(result_phasor)):.3f}' + deg_sym)
                    self.results_lbl.configure(text = f'Phasor magnitude : {abs(result_phasor):.3f}{get_UoM()} and phase angle is {math.degrees(cmath.phase(result_phasor)):.3f}' + deg_sym)
                else:
                    messagebox.showwarning('Warning', 'You must select a value type.')

            #Calculations for parallel circuits
            elif circuit_type_int.get() == 2:
                print('It is a parallel circuit.')
                if r_val_cmb.get() != '': #Value type must be selected
                    print(f'The selected value is {r_val_cmb.get()}')
                    res_phasor = complex(float(self.float_ent1.get()), 0)
                    print(res_phasor)
                    print(f'The selected value is {r_val_cmb.get()}')
                    if r_val_cmb.get() == 'Admittance':
                        print('Admittance calculation')
                        reactive_phasor = complex(0, float(self.float_ent3.get()) - float(self.float_ent2.get()))
                        print(reactive_phasor)
                    if r_val_cmb.get() == 'Current':
                        print('Current calculation')
                        reactive_phasor = complex(0, float(self.float_ent3.get()) - float(self.float_ent2.get()))
                        print(reactive_phasor)
                    elif r_val_cmb.get() == 'Power':
                        print('Power Calculation')
                        reactive_phasor = complex(0, float(self.float_ent2.get()) - float(self.float_ent3.get()))
                        print(reactive_phasor)
                    elif r_val_cmb.get() == 'Impedance':
                        print('Made it to here')
                        impedanceP = get_parallel_Z(float(self.float_ent1.get()), float(self.float_ent2.get()), float(self.float_ent3.get()))
                        print(f'The impedance for the parallel circuit i: {impedanceP}')
                        if float(self.float_ent2.get()) != 0:
                            pa = math.degrees(math.atan(float(self.float_ent1.get())/float(self.float_ent2.get())))
                            print(pa)
                
                   
                    
                    #Display results for parallel circuit

                    if r_val_cmb.get() == 'Impedance':
                        print(f'Phasor magnitude : {impedanceP}')
                        self.results_lbl.configure(text = f'Phasor magnitude : {impedanceP:.3f}{get_UoM()} and phase angle is {pa:.3f}' + deg_sym)
                    else:
                        result_phasor = res_phasor + reactive_phasor
                        print(result_phasor)
                        print(f'Phasor magnitude : {abs(result_phasor):.3f}{get_UoM()} and phase angle is {math.degrees(cmath.phase(result_phasor)):.3f}' + deg_sym)
                        self.results_lbl.configure(text = f'Phasor magnitude : {abs(result_phasor):.3f}{get_UoM()} and phase angle is {math.degrees(cmath.phase(result_phasor)):.3f}' + deg_sym)
                else:
                    messagebox.showwarning('Warning', 'You must select a value type.')  
            else:
                messagebox.showwarning('Warning', 'You must select Series or Parallel.')
                
        def display_plot():
            x = np.linspace(0, 20, 100)  # Create a list of 100 evenly-spaced numbers over the range 0 to 20.
            plt.plot(x, np.sin(x))       # Plot the sine of each x point
            plt.show()                   # Display the plot 
  
         

       
        #Layout for the Frame containing circuit and value type selectors
        select_frm = ttk.Frame(self.body_frm)
        select_frm.grid(row = 1, column = 0, columnspan = 3)

        sel_series_rbtn = ttk.Radiobutton(select_frm, text="Series", variable=circuit_type_int, value=1, command = set_series_menu)
        sel_series_rbtn.grid(row = 0, column = 0, sticky = 'w')

        ttk.Radiobutton(select_frm, text="Parallel", variable=circuit_type_int, value=2, command = set_series_menu).grid(row = 0, column = 1, sticky = 'w')
        
        
        r_val_cmb = ttk.Combobox(select_frm, width = 10, state = 'disabled')
        r_val_cmb.grid(row = 0, column = 2, padx = 15, columnspan = 2, sticky = 'w')
        r_val_cmb.configure(value = series_type_menu)
        

        #Layout for Frame containing the value Entry boxes
        entry_frm = ttk.Frame(self.body_frm)
        entry_frm.grid(row = 2, column = 0, columnspan = 3)

        ttk.Label(entry_frm, text = 'Resistive Value', width = 15).grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.float_ent1 = ttk.Entry(entry_frm, width = 10, textvariable = self.resistor_str, validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.float_ent1.grid(row = 0, column = 1, pady = 10)

        ttk.Label(entry_frm, text = 'Inductive Value', width = 15).grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.float_ent2 = ttk.Entry(entry_frm, width = 10, textvariable = self.inductor_str, validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.float_ent2.grid(row = 1, column = 1, pady = 10, stick = 'e')

        ttk.Label(entry_frm, text = 'Capacitive Value', width = 15).grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.float_ent3 = ttk.Entry(entry_frm, width = 10, textvariable = self.capacitor_str, validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.float_ent3.grid(row = 2, column = 1, pady = 10, stick = 'e')






        #Footer section layout

        #Layout for Results label
        self.results_lbl = ttk.Label(self.footer_frm, text = f'Phasor magnituude; {float(self.float_ent1.get()):.3f}  Phase angle: {float(self.float_ent2.get()):.3f}')
        self.results_lbl.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 3, sticky = 'e')
        
        #Layout for the program buttons
        self.close_btn = ttk.Button(self.footer_frm, text="Close", command=m.quit)
        self.close_btn.grid(row = 1, column = 3, padx = 5, pady = 10, sticky = 'w')
        self.clear_btn = ttk.Button(self.footer_frm, text="Clear", command = clear_vals)
        self.clear_btn.grid(row = 1, column = 2, padx = 5, pady = 10, sticky = 'w')
        self.calculate_btn = ttk.Button(self.footer_frm, text="Calculate", command = calculate)
        self.calculate_btn.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = 'w')
        self.plot_btn = ttk.Button(self.footer_frm, text="Plot", command = display_plot)
        self.plot_btn.grid(row = 1, column = 0, padx = 5, pady = 10, sticky = 'w')

        # End of window layout





    def validate_float(self, new_text): #Validates Entry box values
        if not new_text: # the field is being cleared
            return True
        try:
            self.entered_number = float(new_text)
            return True
        except ValueError:
            tk.messagebox.showerror("Invalid entry!", "Please entry real number.")
            return False


    
        





def main():
    root = tk.Tk()
    prog_app = App(root)
    root.mainloop()
    

if __name__ == '__main__': main()

