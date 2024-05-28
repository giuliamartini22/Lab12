from dataclasses import dataclass

from model.go_retailers import go_retailers


@dataclass
class Connessione():

    R1: go_retailers
    R2: go_retailers
    N: int