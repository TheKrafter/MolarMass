import yaml
from logging42 import logger
from sigfig import round

class MolarMass:
    def __init__(self, rounding=True):
        self.mass = 0.0
        self.round = rounding
        self.compound_start = 'Tap an Element!'
        self.compound = self.compound_start

        with open('elements.yml', 'r') as elements:
            self.elements = yaml.load(elements, Loader=yaml.FullLoader)
    
    def add(self, element):
        try:
            add = self.elements[element]
            logger.debug(f'Added Mass of {element}.')
        except:
            logger.critical(f'Failed to find mass of {element}!')
            return False
        self.mass += add
        if self.round:
            self.mass = round(self.mass, sigfigs = 3)
        self.compound_add(element)
        return True
    
    def clear(self):
        self.mass = 0.0
        self.compound = self.compound_start
    
    def compound_add(self, element):
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        norm = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
        working = self.compound.translate(sub)
        if working == self.compound_start:
            working = element
        elif element in working:
            logger.debug(f'Found {element} in compound {working}')
            comp = working.partition(element)
            after = comp[2]
            try:
                qty = int(after[0])
                qty += 1
                after[0] = str(qty)
                working = comp[0] + comp[1] + comp[2]
                errors = False
            except IndexError:
                qty = 2
                errors = True
            except ValueError:
                qty = 2
                errors = True
            if errors:
                working.replace(element, f'{element}{str(qty)}')
            
        else:
            working += element
        self.compound = working.translate(norm)
