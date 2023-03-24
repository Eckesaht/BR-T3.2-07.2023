from dino_runner.utils.constants import SPIN, SPIN_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Spin(PowerUp):
    def __init__(self):
        super().__init__(SPIN, SPIN_TYPE)
        

