class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        score_copy = sorted(self.scores)
        return score_copy[-1]

    def personal_top_three(self):
        score_copy = sorted(self.scores)
        rev = reversed(score_copy)
        return list(rev)[:3]