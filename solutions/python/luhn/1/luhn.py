class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) == 1:
            return False

        test_sum = 0
        for i in range(-1, -len(self.card_num) - 1, -1):
            if i % 2 == 0:
                new_digit = int(self.card_num[i]) * 2
                if new_digit > 9:
                    new_digit -= 9
                test_sum += new_digit
            else:
                test_sum += int(self.card_num[i])
        
        return test_sum % 10 == 0
        