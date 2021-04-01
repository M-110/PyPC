from pypc.b_basic_logic.core_logic_gates import or_
from pypc.b_basic_logic.selectors import demux_4way
from pypc.e_16_bit_logic.selectors_16 import mux_16_4way
from pypc.g_16_bit_memory.fake_memory import FakeRAM
from pypc.g_16_bit_memory.ram import ram_4k_factory, ram_16k_factory
from pypc.pypc_typing import Bool16, Bool15


def memory_factory():
    ram = ram_16k_factory()
    screen = ram_4k_factory()
    
    def memory(in_: Bool16, load: bool, address: Bool15) -> Bool16:
        load_ram_1, load_ram_2, load_screen, load_keyboard = demux_4way(in_=load,
                                                                        selectors=address[13:15])
        load_ram = or_(load_ram_1, load_ram_2)
        
        ram_out = ram(in_=in_, load=load_ram, address=address[0:14])
        screen_out = screen(in_=in_, load=load_screen, address=address[0:12])
        keyboard_out = (False, ) * 16
        
        return mux_16_4way(address[13:15], ram_out, ram_out, screen_out, keyboard_out)
        # TODO: Keyboard
    return memory


def fake_memory_factory(ram=None, screen=None, keyboard=None):
    if ram is None:
        ram = FakeRAM()
    if screen is None:
        screen = FakeRAM()
    if keyboard is None:
        keyboard = FakeRAM()
    
    def memory(in_: Bool16, load: bool, address: Bool15) -> Bool16:
        load_ram_1, load_ram_2, load_screen, load_keyboard = demux_4way(in_=load,
                                                                        selectors=address[13:15])
        load_ram = or_(load_ram_1, load_ram_2)
        
        ram_out = ram(in_=in_, load=load_ram, address=address[0:14])
        screen_out = screen(in_=in_, load=load_screen, address=address[0:12])
        keyboard_out = keyboard(in_=(False, )*16, load=False, address=(False,))
        
        return mux_16_4way(address[13:15], ram_out, ram_out, screen_out, keyboard_out)
    return memory
