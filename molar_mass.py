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
        working = self.compound.translate(norm)
        if working == self.compound_start:
            working = element
        elif element in working:
            logger.debug(f'Found {element} in compound {working}')
            parts = working.partition(element)
            if parts[2] == '':
                logger.info(f'There is only one {element} in the compound, making 2 now.')
                working = working.replace(element, f'{element}2')
            elif parts[2][0].isdigit():
                qty_old = ''
                for item in parts[2]:
                    if item.isdigit():
                        qty_old += item
                logger.info(f'There are {qty_old} {element} in compound')
                qty = str(int(qty_old) + 1)
                working = working.replace(f'{element + qty_old}', f'{element + qty}')
            else:
                logger.info(f'There is only one {element} in the compound, making 2 now.')
                working = working.replace(element, f'{element}2')
            
        else:
            working += element
        self.compound = working.translate(sub)
