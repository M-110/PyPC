from .logic_gates import and_, or_, not_
from typing import List


def and_16(a: List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool],
           b: List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]) \
        -> List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]:
    """Returns 16-bit bitwise and in the form of a list of 16 bool values."""
    return [and_(a[0], b[0]),
            and_(a[1], b[1]),
            and_(a[2], b[2]),
            and_(a[3], b[3]),
            and_(a[4], b[4]),
            and_(a[5], b[5]),
            and_(a[6], b[6]),
            and_(a[7], b[7]),
            and_(a[8], b[8]),
            and_(a[9], b[9]),
            and_(a[10], b[10]),
            and_(a[11], b[11]),
            and_(a[12], b[12]),
            and_(a[13], b[13]),
            and_(a[14], b[14]),
            and_(a[15], b[15])]


def or_16(a: List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool],
          b: List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]) \
        -> List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]:
    """Returns 16-bit bitwise or in the form of a list of 16 bool values."""
    return [or_(a[0], b[0]),
            or_(a[1], b[1]),
            or_(a[2], b[2]),
            or_(a[3], b[3]),
            or_(a[4], b[4]),
            or_(a[5], b[5]),
            or_(a[6], b[6]),
            or_(a[7], b[7]),
            or_(a[8], b[8]),
            or_(a[9], b[9]),
            or_(a[10], b[10]),
            or_(a[11], b[11]),
            or_(a[12], b[12]),
            or_(a[13], b[13]),
            or_(a[14], b[14]),
            or_(a[15], b[15])]


def not_16(in_: List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool])\
        -> List[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]:
    """Returns 16-bit bitwise not in the form of a list of 16 bool values."""
    return [not_(in_[0]),
            not_(in_[1]),
            not_(in_[2]),
            not_(in_[3]),
            not_(in_[4]),
            not_(in_[5]),
            not_(in_[6]),
            not_(in_[7]),
            not_(in_[8]),
            not_(in_[9]),
            not_(in_[10]),
            not_(in_[11]),
            not_(in_[12]),
            not_(in_[13]),
            not_(in_[14]),
            not_(in_[15])]
