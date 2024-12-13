class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if len(self.card_num.strip()) <= 1:
            return False
        arr = list(self.card_num)
        total = 0
        even = False
        for i in range(len(arr) - 1, -1, -1):
            if arr[i].isdigit():
                if even:
                    if int(arr[i]) * 2 > 9: 
                        total += int(arr[i]) * 2 - 9
                    else:
                        total += int(arr[i]) * 2
                    even = False
                else:
                    even = True
                    total += int(arr[i])
            elif arr[i] != " ":
                return False
            
        return total % 10 == 0