from enum import Enum, unique


# 定义枚举

@unique
class BehaviorType(Enum):
    ADD = 1
    UPDATE = 2
    DELETE = 3
