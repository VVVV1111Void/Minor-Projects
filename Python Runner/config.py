TITLE: str = "Runner"
HEIGHT: int = 576
WIDTH: int = 960
cell_width: int = 64
cell_height: int = 64
world_height: int = 10 # In cells
world_width: int = 20 # In cells
# Path to game sprites
BG: str = "assets/BG.webp"
# SPRITE_ATLAS: str = "assets/sprite_atlas.png"
# ATLAS_DATA: dict = { # Default rects of atlas subtextures
#     # Topleft-X, Topleft-Y, Width, Height in the atlas
#     "PLAYER_SPRITE": (44, 0, 50, 56),
#     # "OBSTACLE_1": (None),
#     # "OBSTACLE_2": (None)
# }
OBSTACLE_SPRITE = "assets/barrel.png"
NORM_Y = HEIGHT-(cell_height*2)
PLAYER_POS = ((WIDTH/2)-cell_width, NORM_Y)
# Interval between the spawning of objects (milis)
MIN_SPAWN: int = int(1.0 * (1000))
MAX_SPAWN: int = int(3.5 * (1000))