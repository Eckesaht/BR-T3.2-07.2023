from dino_runner.utils.constants import SWORD, SWORD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Sword(PowerUp):
    def __init__(self):
        super().__init__(SWORD, SWORD_TYPE)
        

