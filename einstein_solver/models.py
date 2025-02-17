from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Constraint:
    category: str
    value1: str
    relation: str
    value2: str

class Puzzle:
    def __init__(self, categories: List[str], values: Dict[str, List[str]]):
        self.categories = categories
        self.values = values
        self.constraints: List[Constraint] = []

    def add_constraint(self, constraint: Constraint) -> None:
        self.constraints.append(constraint) 