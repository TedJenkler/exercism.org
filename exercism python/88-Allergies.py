class Allergies:

    def __init__(self, score):
        self.score = score
        self.list = { 
            "eggs": 1, 
            "peanuts": 2, 
            "shellfish": 4, 
            "strawberries": 8, 
            "tomatoes": 16, 
            "chocolate": 32, 
            "pollen": 64, 
            "cats": 128
        }

    def allergic_to(self, item):
        return self.score & self.list[item] != 0
        
    @property
    def lst(self):
        x = { 
            1 : "eggs", 
            2 : "peanuts", 
            4 : "shellfish", 
            8 : "strawberries", 
            16 : "tomatoes", 
            32 : "chocolate", 
            64 : "pollen", 
            128 : "cats"
        }
        result = []
        for item in x:
            if self.score & item:
                result.append(x[item])
        return result
        