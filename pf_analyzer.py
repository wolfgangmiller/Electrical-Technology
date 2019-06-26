
"""
Program Name: Power Factor Correction Calculator
Author: Maya Name
Creation Date: 05/02/2019
Description: Calculate the capacitance needed to correct the power factor to a specific amount.

"""
import circuits as cr
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Tk):  # Inheriting from Tk class

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)  # Initializing the inherited class
	    


        tk.Tk.wm_title(self, 'Power Factor Correction Calculator')
        tk.Tk.iconbitmap(self, default='./Templates/wolftrack.ico')
        self.geometry('650x400')

        self.volt_str = tk.StringVar(value='480')
        self.amp_str = tk.StringVar(value='12')
        self.watt_str = tk.StringVar(value='3600')
        self.pf_str = tk.StringVar(value='.95')
        self.hz_str = tk.StringVar(value='60')
        self.status_str = tk.StringVar(value=' Status: Entry values')

        
        self.pf_img = tk.PhotoImage(file='./Electrical/pf_img1.gif')
        
        vcmd_f = self.register(cr.validate_float) # wrapper for the Entry box validation

        def entries_ok():
            # Valid entries 
            if round(float(self.hz_str.get())) <= 0 or round(float(self.volt_str.get())) <= 0 or round(float(self.amp_str.get())) <= 0 or round(float(self.watt_str.get())) <= 0:
                print('Invalid Entry: All values must be greater than zero.')
                self.status_str.set(' Status: Calculation aborted')
                return False
            elif float(self.pf_str.get()) < .90 or round(float(self.pf_str.get())) > 1:
                print('Invalid Entry: Corrected power factor must be between .90 and 1.0')
                self.status_str.set(' Status: Calculation aborted')
                return False
            elif cr.s_ie(self.amp_str.get(), self.volt_str.get()) <= float(self.watt_str.get()):
                print('Invalid Entry: Initial apparent power must be greater than initial true power.')
                self.status_str.set(' Status: Calculation aborted')
                return False
            else:
                print('Good to go!')
                return True


        def calculate():
            print('Method still under construction!')

            if entries_ok():
                old_va = cr.s_ie(self.amp_str.get(), self.volt_str.get())

                print(f'Old_va is {old_va}')

                print(f'pf is {cr.get_pf(self.watt_str.get(), old_va)}')

                old_vars = cr.q_ps(self.watt_str.get(), old_va)

                print(f'Old vars is {old_vars}')

                new_va = cr.s_ppf(self.watt_str.get(), self.pf_str.get())

                print(f'New va is {new_va}')

                new_vars = cr.q_ps(self.watt_str.get(), new_va)

                print(f'New vars is {new_vars}')

                Qc = old_vars - new_vars

                print(f'Qc = {Qc}')

                Xc = cr.z_vs(self.volt_str.get(), Qc)

                print(f'Xc is {Xc}')

                capacitance = cr.capacitance(Xc, self.hz_str.get())

                cap_dis, uom_dis = cr.get_eng_val_tpl(capacitance)

                print(f'Capacitance is {capacitance}')

                v_work = cr.v_peak(self.volt_str.get())

                print(f'Working Voltage is {v_work}')
            
                self.status_str.set(f' Status: The required capacitor is {round(cap_dis, 3)}{uom_dis}F with a working voltage of {round(v_work, 2)}V')

        # Create page frame sections
        self.header_frm = tk.Frame(self)
        self.header_frm.pack(side=tk.TOP)
        self.header_frm.grid_rowconfigure(0, weight=1)

        self.canvas_frm = tk.Frame(self)
        self.canvas_frm.pack()
        self.canvas_frm.grid_rowconfigure(0, weight=1)

        self.body_frm = tk.Frame(self)
        self.body_frm.pack()
        self.body_frm.grid_rowconfigure(0, weight=1)

        self.footer_frm = tk.Frame(self)
        self.footer_frm.pack()
        self.footer_frm.grid_rowconfigure(0, weight=1)

        self.status_frm = ttk.Frame(self)
        self.status_frm.pack(side = tk.BOTTOM, fill=tk.X)

        # Header Section
        label = tk.Label(self.header_frm, text='Calculate the capacitance needed to correct the power factor to a specific amount.')
        label.pack(pady=10,padx=10)

        # Canvas Section
        self.canvas = tk.Canvas(self.canvas_frm, width=516, height=233)
        self.canvas.pack(anchor=tk.CENTER)

        self.canvas.create_image(0,0, anchor=tk.NW, image=self.pf_img)

        # Body Section

        label = tk.Label(self.body_frm, text='Voltage')
        label.grid(row=1, column=0, padx=15,pady=5)

        self.volt_ent = ttk.Entry(self.body_frm, width = 6, textvariable = self.volt_str, validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.volt_ent.grid(row = 1, column = 1, pady = 10)

        label = tk.Label(self.body_frm, text='Ampage')
        label.grid(row=1, column=2, padx=15,pady=5)

        self.amp_ent = ttk.Entry(self.body_frm, width = 6, textvariable = self.amp_str, validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.amp_ent.grid(row = 1, column = 3, pady = 10)

        label = tk.Label(self.body_frm, text='Watts')
        label.grid(row=1, column=4, padx=15,pady=5)

        self.watt_ent = ttk.Entry(self.body_frm, width = 5, textvariable = self.watt_str,  validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.watt_ent.grid(row = 1, column = 5, pady = 10)

        label = tk.Label(self.body_frm, text='Hertz')
        label.grid(row=1, column=6, padx=15,pady=5)

        self.hz_ent = ttk.Entry(self.body_frm, width = 5, textvariable = self.hz_str,validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.hz_ent.grid(row = 1, column = 7, pady = 10)

        label = tk.Label(self.body_frm, text='Corrected pf')
        label.grid(row=1, column=8, padx=15,pady=5)

        self.pf_ent = ttk.Entry(self.body_frm, width = 5, textvariable = self.pf_str,validate="focusout", validatecommand=(vcmd_f, '%P'))
        self.pf_ent.grid(row = 1, column = 9, pady = 10)


    

        # footer Section

        close_btn = ttk.Button(self.footer_frm, text='Close', command=quit)
        close_btn.grid(row=1, column=1, padx=5,pady=5)

        cal_btn = ttk.Button(self.footer_frm, text='Calculate', command=calculate)
        cal_btn.grid(row=1, column=0, padx=5,pady=5)

        status_lbl = tk.Label(self.status_frm, textvariable=self.status_str, borderwidth=1, relief=tk.SUNKEN, anchor=tk.W)
        status_lbl.pack(side = tk.BOTTOM, fill=tk.X)


    # def validate_float(self, new_text): #Validates Entry box values
    #     if not new_text: # the field is being cleared
    #         return True
    #     try:
    #         self.entered_number = float(new_text)
    #         return True
    #     except ValueError:
    #         tk.messagebox.showerror("Invalid entry!", "Please entry real numbers in value fields.")
    #         return False





        


def main():
    prog_app = App()
    prog_app.mainloop()


if __name__ == '__main__': main()

