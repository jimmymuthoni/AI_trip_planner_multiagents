class Calculator:
    @staticmethod
    def multiply(a:int, b:int)->int:
        """
        returns the product of a and b
        """
        return a * b
    
    @staticmethod
    def calculate_total(*x:float)->float:
        """
        claculate the sum of given list of numbers
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total: float, days:int)->float:
        "calculate daily budget and returns expense for as single day"
        return total / days if days > 0 else 0