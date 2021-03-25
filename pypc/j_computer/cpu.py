from pypc.b_basic_logic.core_logic_gates import or_, and_, not_
from pypc.e_16_bit_logic.selectors_16 import mux_16
from pypc.i_arithmetic_logic_unit import alu

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