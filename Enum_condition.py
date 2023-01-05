from enum import Enum


class Condition_enums(Enum):
    """Enum for the condition of the item"""
    EQUAL = 1
    NOT_EQUAL = 2

class next_step_enums(Enum):
    """Enum for the next_step_enums of the item"""
    AND = 1
    OR = 2
    NOTNEXT = 3