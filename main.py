import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib
from molar_mass import MolarMass
from logging42 import logger

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Molar Mass
        self.mm = MolarMass()

        # Layout
        self.set_title("Molar Mass")

        self.box_whole = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box_whole)

        ## Upper Box
        self.box_upper = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_upper_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_upper_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.box_whole.append(self.box_upper)
        self.box_upper.append(self.box_upper_left)
        self.box_upper.append(self.box_upper_right)

        self.box_upper.set_spacing(10)
        self.box_upper_left.set_spacing(5)
        self.box_upper_right.set_spacing(5)

        ## Lower Box
        self.box_lower = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_whole.append(self.box_lower)

        ## Left Side Display
        ### Molecule Name
        self.label_molecule = Gtk.Label(label="Tap an Element!")
        self.box_upper_left.append(self.label_molecule)

        ### Mass Display
        self.label_mass = Gtk.Label(label="0.0 g/mol")
        self.box_upper_left.append(self.label_mass)

        ## Right Side Controls
        ### Clear Button
        self.button_clear = Gtk.Button(label="Clear")
        self.button_clear.connect('clicked', self.clear_mass)
        self.box_upper_right.append(self.button_clear)
        ### Rounding Checkbox
        self.check_rounding = Gtk.CheckButton(label="Round 3 SigFigs")
        self.box_upper_right.append(self.check_rounding)
        self.check_rounding.set_active(True)

        ## Periodic Table of Buttons
        ### Period 1
        self.box_period_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_lower.append(self.box_period_1)
        #### Buttons
        self.button_h = Gtk.Button(label="H")
        self.button_h.connect('clicked', self.add_mass, 'H')
        self.box_period_1.append(self.button_h)
        
        self.box_period_1_space = Gtk.Label(label=(" " * 260))
        self.box_period_1.append(self.box_period_1_space)

        self.button_he = Gtk.Button(label="He")
        self.button_he.connect('clicked', self.add_mass, 'He')
        self.box_period_1.append(self.button_he)

        ### Period 2
        self.box_period_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_lower.append(self.box_period_2)
        #### Buttons
        self.button_li = Gtk.Button(label="Li")
        self.button_li.connect('clicked', self.add_mass, 'Li')
        self.box_period_2.append(self.button_li)

        self.button_be = Gtk.Button(label="Be")
        self.button_be.connect('clicked', self.add_mass, 'Be')
        self.box_period_2.append(self.button_be)

        self.box_period_2_space = Gtk.Label(label=("                " * 10))
        self.box_period_2.append(self.box_period_2_space)

        self.button_b = Gtk.Button(label="B")
        self.button_b.connect('clicked', self.add_mass, 'B')
        self.box_period_2.append(self.button_b)

        self.button_c = Gtk.Button(label="C")
        self.button_c.connect('clicked', self.add_mass, 'C')
        self.box_period_2.append(self.button_c)

        self.button_n = Gtk.Button(label="N")
        self.button_n.connect('clicked', self.add_mass, 'N')
        self.box_period_2.append(self.button_n)

        self.button_o = Gtk.Button(label="O")
        self.button_o.connect('clicked', self.add_mass, 'O')
        self.box_period_2.append(self.button_o)

        self.button_f = Gtk.Button(label="F")
        self.button_f.connect('clicked', self.add_mass, 'F')
        self.box_period_2.append(self.button_f)

        self.button_ne = Gtk.Button(label="Ne")
        self.button_ne.connect('clicked', self.add_mass, 'Ne')
        self.box_period_2.append(self.button_ne)

        ## Period 3
        self.box_period_3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_lower.append(self.box_period_3)
        ### Buttons
        self.button_na = Gtk.Button(label="Na")
        self.button_na.connect('clicked', self.add_mass, 'Na')
        self.box_period_3.append(self.button_na)

        self.button_mg = Gtk.Button(label="Mg")
        self.button_mg.connect('clicked', self.add_mass, 'Mg')
        self.box_period_3.append(self.button_mg)

        self.box_period_3_space = Gtk.Label(label=("                " * 10))
        self.box_period_3.append(self.box_period_3_space)

        self.button_al = Gtk.Button(label="Al")
        self.button_al.connect('clicked', self.add_mass, 'Al')
        self.box_period_3.append(self.button_al)

        self.button_si = Gtk.Button(label="Si")
        self.button_si.connect('clicked', self.add_mass, 'Si')
        self.box_period_3.append(self.button_si)

        self.button_p = Gtk.Button(label="P")
        self.button_p.connect('clicked', self.add_mass, 'P')
        self.box_period_3.append(self.button_p)

        self.button_s = Gtk.Button(label="S")
        self.button_s.connect('clicked', self.add_mass, 'S')
        self.box_period_3.append(self.button_s)

        self.button_cl = Gtk.Button(label="Cl")
        self.button_cl.connect('clicked', self.add_mass, 'Cl')
        self.box_period_3.append(self.button_cl)

        self.button_ar = Gtk.Button(label="Ar")
        self.button_ar.connect('clicked', self.add_mass, 'Ar')
        self.box_period_3.append(self.button_ar)

        ## Period 4
        self.box_period_4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_lower.append(self.box_period_4)
        ## Buttons
        elements = ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']
        it = 0
        self.buttons_period_4 = []
        for element in elements:
            self.buttons_period_4.append(Gtk.Button(label=element))
            self.buttons_period_4[it].connect('clicked', self.add_mass, element)
            self.box_period_4.append(self.buttons_period_4[it])
            it = it + 1
        
        ## Period 5
        self.box_period_5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_lower.append(self.box_period_5)
        ## Buttons
        elements = ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe']
        it = 0
        self.buttons_period_5 = []
        for element in elements:
            self.buttons_period_5.append(Gtk.Button(label=element))
            self.buttons_period_5[it].connect('clicked', self.add_mass, element)
            self.box_period_5.append(self.buttons_period_5[it])
            it = it + 1
        
        

    # Actions
    # Add Mass
    def add_mass(self, button, element):
        if self.check_rounding.get_active():
            self.mm.round = True
        else:
            self.mm.round = False
        self.mm.add(element)
        self.update_mass()

    # Reset
    def clear_mass(self, button):
        self.mm.clear()
        self.update_mass()
        logger.debug('Cleared Molar Mass.')
    
    # Update Mass
    def update_mass(self):
        if self.check_rounding.get_active():
            self.mm.round = True
        else:
            self.mm.round = False
        self.label_mass.set_text(f'{self.mm.mass} g/mol')
        self.update_compound()
    
    # Update Compound
    def update_compound(self):
        self.label_molecule.set_text(f'{self.mm.compound}')

class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

# Run App
app = App(application_id="com.github.thekrafter.MolarMass")
app.run(sys.argv)
