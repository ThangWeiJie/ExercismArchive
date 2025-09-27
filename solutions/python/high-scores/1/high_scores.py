class HighScores:
    def __init__(self, scores: list):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        scores_copy = [score for score in self.scores]
        top_three_scores = []

        for _ in range(3):
            if len(scores_copy) == 0:
                break
            
            highest_score = max(scores_copy)
            top_three_scores.append(highest_score)
            scores_copy.remove(highest_score)
        
        return top_three_scores