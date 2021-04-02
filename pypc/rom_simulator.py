from pypc.tests._converter import bool16_to_int


class ROM:
    def __init__(self, file=None):
        self.file = file
        self.data = None
        if file:
            self.read_file()
        
    def read_file(self):
        with open(self.file, encoding='utf-8-sig') as f:
            self.data = [x[::-1] for x in f.read().split('\n') if x]
        
    def read_address(self, address):
        address_index = bool16_to_int(address)
        try:
            out = tuple(True if c == '1' else False for c in self.data[address_index])
            return out
        except IndexError:
            return (False, ) * 16
