# 2
player_score = {
    "Ankle Dorsiflexion": 0.0,
    "Ankle Eversion and Inversion": 0.0,
    "Tibial Rotation": 0.0
}
player_programming = []
# Ankle Eversion and Inversion
ankle_dorsiflexion_exercises = ['x']
ankle_eversion_exercises = ['y']
def ankle_eversion_inversion_comparison(score):
    global player_programming
    if score["Ankle Dorsiflexion"] < 0.5 or score["Ankle Eversion and Inversion"] < 0.5 or score["Tibial Rotation"]< 0.5:
        player_programming += ankle_dorsiflexion_exercises
        if score["Ankle Eversion and Inversion"] <0.5:
            player_programming += ankle_eversion_exercises
ankle_eversion_inversion_comparison(player_score)
print("Ankle Eversion and Inversion exercises:", player_programming)
