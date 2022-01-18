class Team:

    # how much (in millions) it costs to gain one 1km/h
    money_per_speed = 3

    def __init__(self, name: str, budget: int):
        self.name = name
        self.budget = budget
        self.carspeed: int = budget//self.money_per_speed
        self.points = 0
        
    def get_budget(self) -> int:
        return self.budget
    
    def car_speed(self) -> int:
        return self.carspeed 

    def get_points(self) -> int:
        return self.points
    
    def add_points(self, point: int) -> None:
        self.points = self.points + point
            
    def get_name(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'{self.points}'
    
    def __str__(self) -> str:
        return f'{self.points}'
