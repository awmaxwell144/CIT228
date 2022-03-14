class GameStats:

    def __init__(self, cr_game):
        self.settings = cr_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.drops_left = self.settings.drop_limit
        self.score = 0