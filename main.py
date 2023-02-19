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

        ## Periodic Table of Buttons
        ### Period 1
        self.box_period_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_lower.append(self.box_period_1)
        #### Buttons
        self.button_h = Gtk.Button(label="H")
        self.button_h.connect('clicked', self.add_mass, 'H')
        self.box_period_1.append(self.button_h)
        
        self.box_period_1_space = Gtk.Label(label="                                ")
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
