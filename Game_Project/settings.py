class Settings:
    #stores game settings
    
    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (178, 211, 194)

        self.bucket_speed = 1.3
        self.drop_limit = 5

        self.raindrop_speed = .25
        self.drops_per_row = 1
        self.time_between_rows = 1
        self.raindrop_points = 3