class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergy_list = []

        test_items = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

        self.allergy_list = [test_items[i] for i in range(len(test_items)) if self.score & (1 << i)]

    def allergic_to(self, item):
        return item in self.allergy_list

    @property
    def lst(self):
        return self.allergy_list
