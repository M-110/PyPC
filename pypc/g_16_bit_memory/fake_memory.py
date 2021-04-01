from collections import defaultdict
from typing import Tuple, Dict

from pypc.pypc_typing import Bool16
from pypc.tests._converter import bool16_to_int


class FakeRAM:
    """Class to bypass the enormous amount of nand gate function calls required
     to simulate memory each cycle.
    
    Stores data in the form of a dictionary.
    """
    def __init__(self):
        self.data: Dict[Tuple[bool, ...], Bool16] = defaultdict(lambda: (False, )*16)
        self.data_dec = {}
        
    def __call__(self, in_: Bool16, load: bool, address: Tuple[bool, ...]) -> Bool16:
        if load:
            print('loading new value: ', bool16_to_int(in_))
            self.data_dec[bool16_to_int(address)] = bool16_to_int(in_)
            self.data[address] = in_
        print('reading from address ', bool16_to_int(address))
        return self.data[address]