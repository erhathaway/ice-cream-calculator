from dataclasses import dataclass, field
from typing import List

@dataclass
class Constraint:
    name: str
    property: str
    ideal_value: float
    tolerance: float
    min_value: float = field(init=False)
    max_value: float = field(init=False)

    def __post_init__(self):
        self.min_value = self.ideal_value - self.tolerance
        self.max_value = self.ideal_value + self.tolerance

@dataclass
class Constraints:
    constraints: List[Constraint] = field(default_factory=list)

    def add_constraint(self, name: str, property: str, ideal_value: float, tolerance: float):
        self.constraints.append(Constraint(name, property, ideal_value, tolerance))
