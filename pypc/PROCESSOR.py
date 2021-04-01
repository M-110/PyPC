from pypc.g_16_bit_memory.fake_memory import FakeRAM
from pypc.j_computer.computer import computer_factory, computer_factory_with_fake_ram
from pypc.j_computer.memory import fake_memory_factory
from pypc.rom_simulator import ROM

computer = computer_factory_with_fake_ram()
rom = ROM()

if __name__ == "__main__":
    file = 'Playground.hack'
    rom.file = file
    rom.read_file()
    print(rom.data)
    
    ram = FakeRAM()
    screen = FakeRAM()
    keyboard = FakeRAM()
    memory = fake_memory_factory(ram, screen, keyboard)
    computer = computer_factory_with_fake_ram(memory)
    for _ in range(100):
        computer(reset=False, rom=rom)
    print(ram.data_dec)
        
    # computer