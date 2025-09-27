class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergy_list = []

        test_items = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats"}

        mask = 1
        res = 0

        for _ in range(8):
            res = self.score & mask
            if res != 0:
                self.allergy_list.append(test_items.get(res))
            mask = mask << 1

    def allergic_to(self, item):
        return item in self.allergy_list

    @property
    def lst(self):
        return self.allergy_list
