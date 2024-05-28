from dataclasses import dataclass

@dataclass
class go_retailers():
    Retailer_code: int
    Retailer_name:str
    Type: str
    Country: str


    def __hash__(self):
        return self.Retailer_code

    def __str__(self):
        return f" {self.Retailer_code} - {self.Retailer_name}"