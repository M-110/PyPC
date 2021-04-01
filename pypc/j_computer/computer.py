from pypc.j_computer.cpu import cpu_factory
from pypc.j_computer.memory import memory_factory, fake_memory_factory
from pypc.rom_simulator import ROM


def computer_factory():
    cpu = cpu_factory()
    memory = memory_factory()
    address = (False,) * 16
    m_in = (False,) * 16

    def computer(reset: bool, rom: ROM):
        """The function that encapsulates everything."""
        nonlocal address
        nonlocal m_in
        instructions = rom.read_address(address)
        m_out, write_m, m_address, address = cpu(m_in=m_in,
                                                 instructions=instructions,
                                                 reset=reset)
        m_in = memory(m_out, write_m, m_address)

    return computer


def computer_factory_with_fake_ram(memory=None):
    cpu = cpu_factory()
    if memory is None:
        memory = fake_memory_factory()
    address = (False,) * 16
    m_in = (False,) * 16
    
    def computer(reset: bool, rom: ROM):
        """The function that encapsulates everything."""
        nonlocal address
        nonlocal m_in
        instructions = rom.read_address(address)
        m_out, write_m, m_address, address = cpu(m_in=m_in,
                                                 instructions=instructions,
                                                 reset=reset)
        m_in = memory(m_out, write_m, m_address)
        return memory

    return computer
