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
        self.box_whole.set_spacing(10)

        ## Upper Box
        self.box_upper = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_upper_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_upper_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.box_whole.append(self.box_upper)
        self.box_upper.append(self.box_upper_left)
        self.box_upper.append(self.box_upper_right)
        self.box_upper.set_spacing(5)

        self.box_upper.set_spacing(10)
        self.box_upper_left.set_spacing(5)
        self.box_upper_right.set_spacing(5)

        ## Lower Box
        self.box_lower = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_whole.append(self.box_lower)

        ### Scrollability
        self.scrolled_window = Gtk.ScrolledWindow.new()
        self.viewport_periodic = Gtk.Viewport.new()
        self.scrolled_window.set_child(self.viewport_periodic)
        self.viewport_adjustment = Gtk.Adjustment(lower=50, upper=5000, step_increment=10)
        self.box_lower.append(self.scrolled_window) 
        self.viewport_periodic.set_hadjustment(self.viewport_adjustment)

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
        self.peridoic_grid = Gtk.Grid()
        self.viewport_periodic.set_child(self.peridoic_grid)

        ### Labels
        self.label_groups = []
        for i in range(18):
            self.label_groups.append(Gtk.Label(label=f'{str(i+1)}'))
            self.peridoic_grid.attach(self.label_groups[i], column=(i+1), row = 0, width=1, height=1)
        
        self.label_periods = []
        for i in range(7):
            self.label_periods.append(Gtk.Label(label=f'{str(i+1)}'))
            self.peridoic_grid.attach(self.label_periods[i], column=0, row=(i+1), width=1, height=1)

        ### Period 1
        self.element_h = Gtk.Button(label='H')
        self.element_h.connect('clicked', self.add_mass, 'H')
        self.peridoic_grid.attach(self.element_h, column=1, row=1, width=1, height=1)

        self.element_he = Gtk.Button(label='He')
        self.element_he.connect('clicked', self.add_mass, 'He')
        self.peridoic_grid.attach(self.element_he, column=18, row=1, width=1, height=1)

        ### Period 2
        self.element_li = Gtk.Button(label='Li')
        self.element_li.connect('clicked', self.add_mass, 'Li')
        self.peridoic_grid.attach(self.element_li, column=1, row=2, width=1, height=1)

        self.element_be = Gtk.Button(label='Be')
        self.element_be.connect('clicked', self.add_mass, 'Be')
        self.peridoic_grid.attach(self.element_be, column=2, row=2, width=1, height=1)

        self.element_b = Gtk.Button(label='B')
        self.element_b.connect('clicked', self.add_mass, 'B')
        self.peridoic_grid.attach(self.element_b, column=13, row=2, width=1, height=1)

        self.element_c = Gtk.Button(label='C')
        self.element_c.connect('clicked', self.add_mass, 'C')
        self.peridoic_grid.attach(self.element_c, column=14, row=2, width=1, height=1)

        self.element_n = Gtk.Button(label='N')
        self.element_n.connect('clicked', self.add_mass, 'N')
        self.peridoic_grid.attach(self.element_n, column=15, row=2, width=1, height=1)

        self.element_o = Gtk.Button(label='O')
        self.element_o.connect('clicked', self.add_mass, 'O')
        self.peridoic_grid.attach(self.element_o, column=16, row=2, width=1, height=1)

        self.element_f = Gtk.Button(label='F')
        self.element_f.connect('clicked', self.add_mass, 'F')
        self.peridoic_grid.attach(self.element_f, column=17, row=2, width=1, height=1)

        self.element_ne = Gtk.Button(label='Ne')
        self.element_ne.connect('clicked', self.add_mass, 'Ne')
        self.peridoic_grid.attach(self.element_ne, column=18, row=2, width=1, height=1)

        ### Period 3
        self.element_na = Gtk.Button(label='Na')
        self.element_na.connect('clicked', self.add_mass, 'Na')
        self.peridoic_grid.attach(self.element_na, column=1, row=3, width=1, height=1)

        self.element_mg = Gtk.Button(label='Mg')
        self.element_mg.connect('clicked', self.add_mass, 'Mg')
        self.peridoic_grid.attach(self.element_mg, column=2, row=3, width=1, height=1)

        self.element_al = Gtk.Button(label='Al')
        self.element_al.connect('clicked', self.add_mass, 'Al')
        self.peridoic_grid.attach(self.element_al, column=13, row=3, width=1, height=1)

        self.element_si = Gtk.Button(label='Si')
        self.element_si.connect('clicked', self.add_mass, 'Si')
        self.peridoic_grid.attach(self.element_si, column=14, row=3, width=1, height=1)

        self.element_p = Gtk.Button(label='P')
        self.element_p.connect('clicked', self.add_mass, 'P')
        self.peridoic_grid.attach(self.element_p, column=15, row=3, width=1, height=1)

        self.element_s = Gtk.Button(label='S')
        self.element_s.connect('clicked', self.add_mass, 'S')
        self.peridoic_grid.attach(self.element_s, column=16, row=3, width=1, height=1)

        self.element_cl = Gtk.Button(label='Cl')
        self.element_cl.connect('clicked', self.add_mass, 'Cl')
        self.peridoic_grid.attach(self.element_cl, column=17, row=3, width=1, height=1)

        self.element_ar = Gtk.Button(label='Ar')
        self.element_ar.connect('clicked', self.add_mass, 'Ar')
        self.peridoic_grid.attach(self.element_ar, column=18, row=3, width=1, height=1)

        ### Period 4
        elements = ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']
        it = 0
        self.elements_period_4 = []
        for element in elements:
            self.elements_period_4.append(Gtk.Button(label=element))
            self.elements_period_4[it].connect('clicked', self.add_mass, element)
            self.peridoic_grid.attach(self.elements_period_4[it], column=(it+1), row=4, width=1, height=1)
            it += 1
        
        ### Period 5
        elements = ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe']
        it = 0
        self.elements_period_5 = []
        for element in elements:
            self.elements_period_5.append(Gtk.Button(label=element))
            self.elements_period_5[it].connect('clicked', self.add_mass, element)
            self.peridoic_grid.attach(self.elements_period_5[it], column=(it+1), row=5, width=1, height=1)
            it += 1

        ### Period 6
        elements = ['Cs', 'Ba', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']
        it = 0
        self.elements_period_6 = []
        for element in elements:
            self.elements_period_6.append(Gtk.Button(label=element))
            self.elements_period_6[it].connect('clicked', self.add_mass, element)
            self.peridoic_grid.attach(self.elements_period_6[it], column=(it+1), row=6, width=1, height=1)
            it += 1

        ### Period 7
        elements = ['Fr', 'Ra', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
        it = 0
        self.elements_period_7 = []
        for element in elements:
            self.elements_period_7.append(Gtk.Button(label=element))
            self.elements_period_7[it].connect('clicked', self.add_mass, element)
            self.peridoic_grid.attach(self.elements_period_7[it], column=(it+1), row=7, width=1, height=1)
            it += 1
        
        ### F-Block
        #### Spacer
        self.spacer_fblock = Gtk.Label(label='   ')
        self.peridoic_grid.attach(self.spacer_fblock, column=0, row=8, width=19, height=1)
        #### Part 1
        elements = ['La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Fr', 'Tm', 'Yb']
        it = 0
        self.elements_fblock_1 = []
        for element in elements:
            self.elements_fblock_1.append(Gtk.Button(label=element))
            self.elements_fblock_1[it].connect('clicked', self.add_mass, element)
            self.peridoic_grid.attach(self.elements_fblock_1[it], column=(it+3), row=9, width=1, height=1)
            it += 1

        #### Part 2
        elements = ['Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No']
        it = 0
        self.elements_fblock_2 = []
        for element in elements:
            self.elements_fblock_2.append(Gtk.Button(label=element))
            self.elements_fblock_2[it].connect('clicked', self.add_mass, element)
            self.peridoic_grid.attach(self.elements_fblock_2[it], column=(it+3), row=10, width=1, height=1)
            it += 1
        # Pre-Run Actions
        self.update_mass()
        

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
        self.label_mass.set_markup(f'<b>{self.mm.mass} g/mol</b>')
    
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
