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

        self.box_upper = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_upper_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_upper_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box_upper)
        self.box_upper.append(self.box_upper_left)
        self.box_upper.append(self.box_upper_right)

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
    
    # Actions
    # Add Mass

    # Reset
    def clear_mass(self, button):
        self.mm.clear()
        self.label_mass
        logger.debug('Cleared Molar Mass.')
    
    # Update Mass
    def update_mass(self):
        self.label_mass.setText(f'{mm.mass} g/mol')

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
