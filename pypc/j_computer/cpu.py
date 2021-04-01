from typing import Tuple

from pypc.b_basic_logic.core_logic_gates import or_, and_, not_
from pypc.e_16_bit_logic.selectors_16 import mux_16
from pypc.g_16_bit_memory.program_counter import pc_factory
from pypc.g_16_bit_memory.register import register_16_bit_factory
from pypc.i_arithmetic_logic_unit.alu import alu
from pypc.pypc_typing import Bool16, Bool15

"""
### A Instruction format: VVVVVVVVVVVVVVV 0
    
    0-14: 15 bit value describing an address. (V)
    15: A instruction digit. (0)
        Always 0
    
### C Instruction format: 111 ACCCCCC DDD JJJ
C instructions begin with 1:
    0-2: jump instructions (J)
        j1 = ng
        j2 = zr
        j3 = greater than zero
    
    3-5: destination instructions (D)
        d1 = A
        d2 = D
        d3 = M
        
    6-12: computational instructions (C)
        A = M
        c1 = zx
        c2 = nx
        c3 = zy
        c4 = ny
        c5 = f
        c6 = no
        
    13-15: C instruction digits (1)
        Always just 111
    
"""


# nand gates used: 1206
def cpu_factory():
    alu_out: Bool16 = (False,) * 16
    a_register = register_16_bit_factory()
    d_register = register_16_bit_factory()
    pc = pc_factory()

    def cpu(m_in: Bool16, instructions: Bool16, reset: bool) \
            -> Tuple[Bool16, bool, Bool15, Bool15]:
        """Simulation of the CPU unit.
        
        Args:
            m_in: Value of the M RAM input.
            instructions: 16 bit instructions for the CPU to follow.
            reset: If True, program will be restarted.
            
        Returns:
            (a, b, c, d) where
            a: M output value.
            b: Write to M instruction.
            c: Address of M
            d: address of the next instruction
        """
        nonlocal alu_out

        # If first instruction digit is 1, then it is a C instruction.
        a_instruction = not_(instructions[15])
        c_instruction = not_(a_instruction)

        # # # # # # # # # # # # # # Register A
        # instructions[5] represents whether A is the destination
        alu_to_a = and_(a=c_instruction, b=instructions[5])

        # If it's a C instruction and the destination is A then send the ALU output
        # to the A register. Otherwise send the instruction to Register A.
        register_a_input = mux_16(alu_to_a, instructions, alu_out)

        # load_a is True if it is an A instruction or the C instruction has A as
        # the destination.
        load_a = or_(a_instruction, alu_to_a)
        a_to_pc = a_register(register_a_input, load_a)
        register_a_out = a_to_pc
        m_address = a_to_pc[0:15]  # Returned as output ->

        # if instructions[12] is True M should be used instead of the A register
        am_mux_out = mux_16(instructions[12], register_a_out, m_in)

        # # # # # # # # # # # # # # Register D
        # If instructions[4] is True the D register is the destination (if it is a
        # c instruction).
        load_d = and_(a=c_instruction, b=instructions[4])
        register_d_out = d_register(alu_out, load_d)

        # # # # # # # # # # # # # # ALU
        # Send the register_d_out into the ALU
        alu_out, zero_out, neg_out = alu(x=register_d_out,
                                         y=am_mux_out,
                                         zero_x=instructions[11],
                                         negate_x=instructions[10],
                                         zero_y=instructions[9],
                                         negate_y=instructions[8],
                                         add_x_y=instructions[7],
                                         negate_output=instructions[6])

        m_out = alu_out  # Returned as output ->

        # If it is a C instruction and the destination is M, write to M
        write_m = and_(c_instruction, instructions[3])  # Returned as output ->

        # # # # # # # # # # # # # # PC / JUMP conditionals
        # Jump if equal to zero
        jeq = and_(zero_out, instructions[1])
        # Jump if less than zero
        jlt = and_(neg_out, instructions[2])

        # Zero or negative
        zero_or_neg = or_(zero_out, neg_out)
        # Positive
        positive = not_(zero_or_neg)

        # Jump if greater than zero
        jgt = and_(positive, instructions[0])
        # Jump if less than or equal to zero
        jle = or_(jeq, jlt)

        # If any conditions are met, ready the jump to A
        # (less than or equal to and greater than cover all possible conditions
        # so if either is True, there must be a jump).
        jump_to_a = or_(jle, jgt)

        # Only jump if it a C instruction though!
        load_pc = and_(c_instruction, jump_to_a)
        # If not loading an address, increase the PC
        inc_pc = not_(load_pc)

        # If any conditions were met then the PC will load the address,
        # otherwise the PC will just increase the address to the program's next line.
        pc_out = pc(a_to_pc, load_pc, inc_pc, reset)[:15]  # returned as output

        return m_out, write_m, m_address, pc_out

    return cpu
