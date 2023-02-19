import yaml
from logging42 import logger
from sigfig import round

class MolarMass:
    def __init__(self, rounding=True):
        self.mass = 0.0
        self.round = rounding

        with open('elements.yml', 'r') as elements:
            self.elements = yaml.load(elements, Loader=yaml.FullLoader)
    
    def add(self, element):
        try:
            add = self.elements[element]
            logger.debug(f'Added Mass of {element}.')
        except:
            logger.critical(f'Failed to find mass of {element}!')
            return False
        if self.round == True:
            add = round(add, sigfigs=3)
            self.mass = round(self.mass, sigfigs=3)
        self.mass += add
        return True
    
    def clear(self):
        self.mass = 0.0