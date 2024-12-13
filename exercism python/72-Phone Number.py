class PhoneNumber:
    def __init__(self, number):
        self.input = number
        self.number = self.clean()
        self.area_code = number[:3]
        
        
    def clean(self):
        print(self.input)
        number_list = list(self.input)
        result = []
        for num in number_list:
            if num.isdigit():
                result.append(num)
            else:
                if num.isalpha():
                    raise ValueError("letters not permitted")
                elif num in ['@', ':', '!']:
                    raise ValueError("punctuations not permitted")
        if len(result) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(result) == 10:
            if result[0] == "0":
                raise ValueError("area code cannot start with zero")
            elif result[0] == "1":
                raise ValueError("area code cannot start with one")
            elif result[3] == "0":
                raise ValueError("exchange code cannot start with zero")
            elif result[3] == "1":
                raise ValueError("exchange code cannot start with one")
        if len(result) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(result) == 11 and result[0] != "1":
            raise ValueError("11 digits must start with 1")
        if len(result) == 11:
            self.area_code = result[1:4]
            if result[1] == "0":
                raise ValueError("area code cannot start with zero")
            if result[1] == "1":
                raise ValueError("area code cannot start with one")
            if result[4] == "0":
                raise ValueError("exchange code cannot start with zero")
            if result[4] == "1":
                raise ValueError("exchange code cannot start with one")
            return "".join(result[1:])
        return "".join(result)

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:11]}"