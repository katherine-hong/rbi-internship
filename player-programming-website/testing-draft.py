# This is the file to write the first draft of the player programming model

# Jason's section
# Note: I just used placeholder variables for the sake of this example, until Mike provides the actual exercises
player_programming = []
# 2: Ankle Eversion and Inversion

ankle_dorsiflexion_exercises = ['a']
ankle_eversion_exercises = ['b']
def ankle_eversion_inversion_comparison(score):
    global player_programming
    if score["Ankle Dorsiflexion"] < 0.5 or score["Ankle Eversion and Inversion"] < 0.5 or score["Tibial Rotation"]< 0.5:
        player_programming += ankle_dorsiflexion_exercises
        if score["Ankle Eversion and Inversion"] <0.5:
            player_programming += ankle_eversion_exercises
ankle_eversion_inversion_comparison(player_score)
print("Ankle Eversion and Inversion exercises:", player_programming)

#3: Tibial Rotation

hip_external_rotation_exercises = ['c']
hip_internal_rotation_exercises = ['d']
def tibial_rotation_comparison(score):
    global player_programming
    if score["Tibial Rotation"] < 0.5:
        player_programming += hip_external_rotation_exercises
    if score.get("Seated Active Hip Rotation", 1.0) < 0.5:
        player_programming += hip_internal_rotation_exercises
tibial_rotation_comparison(player_score)       
#4: Thomas Test
hip_flexion_hamstring_exercises = ['e']
hip_adduction_exercises = ['f']

def thomas_test_comparison(score):
    global player_programming
    if (score.get("Thomas Test", 1.0) < 0.5 or 
        score.get("Single Leg Stability", 1.0) < 0.5 or 
        score.get("Sliders", 1.0) < 0.5):
        player_programming += hip_flexion_hamstring_exercises
    if score.get("Seated Active Hip Rotation", 1.0) < 0.5:
        player_programming += hip_internal_rotation_exercises
thomas_test_comparison(player_score)
#5: Cossack Squat
def cossack_squat_comparsion(score):
    global player_programming
    if (score.get("Thomas Test", 1.0) < 0.5 or 
        score.get("Single Leg Stability", 1.0) < 0.5 or 
        score.get("Sliders", 1.0) < 0.5):
        player_programming += hip_flexion_hamstring_exercises
    if score.get("Seated Active Hip Rotation", 1.0) < 0.5:
        player_programming += hip_internal_rotation_exercises
    if score.get("Hip External Rotation", 1.0) < 0.5:
        player_programming += hip_external_rotation_exercises
    if (score.get("Ankle Dorsiflexion", 1.0) < 0.5 or 
        score.get("Ankle Eversion and Inversion", 1.0) < 0.5 or 
        score.get("Tibial Rotation", 1.0) < 0.5):
        player_programming += ankle_dorsiflexion_exercises
cossack_squat_comparsion(player_score)
#6: sliders
def sliders_comparison(score):
    global player_programming
    if (score.get("Thomas Test", 1.0) < 0.5 or 
        score.get("Single Leg Stability", 1.0) < 0.5 or 
        score.get("Sliders", 1.0) < 0.5):
        player_programming += hip_flexion_hamstring_exercises
    if score.get("Seated Active Hip Rotation", 1.0) < 0.5:
        player_programming += hip_internal_rotation_exercises
    if (score.get("Ankle Dorsiflexion", 1.0) < 0.5 or 
        score.get("Ankle Eversion and Inversion", 1.0) < 0.5 or 
        score.get("Tibial Rotation", 1.0) < 0.5):
        player_programming += ankle_dorsiflexion_exercises
sliders_comparison(player_score)



# Katherine's section

# The following creates lists of exercises for the buckets
# NOTE: The exercises are not in order of precedence

shoulder_ir_exercises = ["Sleeper Stretch PAILs/RAILs", "Prone Lift-offs", "Prone Lift-Offs to Reverse CARs",
        "Medicine Ball Internal Rotation Rebounders", "Banded Lift-Offs", "Standing Lift-Offs",
        "Supraclavicular Fossa Tissue Work"]

# Not sure if "Side Lying Rotation - Shoulder Flexion" or "Back to Wall Shoulder Flexion Test" should be included
shoulder_flexion_exercises = ["Wall Tricep Stretch", "Sliding Active Pec Stretch w/ Roller",
        "Lat Hangs", "Lat Static Stretch", "Back to Wall Shoulder Flexion", "Doorway Stretch", 
        "Quadratus Lumborum (QL) Fascial Stretch"]

shoulder_stability_exercises = ["Medicine Ball Wall Taps", "External Rotation ISOs"]

scapular_control_exercises = ["Scapular CARs", "Overhead Scaption Raise", "Single Arm Serratus Wall Slide",
        "Serratus Wall Slide with Roller"]

tspine_flexion_extension_exercises = ["Segmental Cat-Camel"]

forearm_supination_exercises = ["Supination/Pronation PAILs/RAILs", "Supinator ISOs"]

elbow_extension_exercises = ["Bicep/Tricep Extension ISO", "Biceps Myofascial Stretch", "3-Position Triceps"]

# Does this need to included all possible wrist exercises?
# NOTE: "Wrist CARs" is just for wrist total ROM specifically
wrist_total_ROM_exercises = ["Wrist CARs"]

# Same question as above
# NOTE: "Cervical Rotations" is just for wrist total ROM specifically
total_cervical_ROM_exercises = ["Cervical Rotations"]


# This is the list of test scores from the player (only partial list)
# NOTE: putting in random scores for testing

player_scores = {
    "Liftoffs": 0.25,
    "Scapular Movement": 1,
    "Back to Wall Shoulder Flexion": 1,
    "Forearm Pronation/Supination": 0.25,
    "Single Leg Stability": 1,
    "Field Goal Test": 1,
    "Shoulder Flexion": 0.4,
    "Shoulder Stability": 0.1,
    "Scapular Control": 0.3,
    "T-spine flexion/extension": 0.4,
    "Forearm Supination": 0.3,
    "Elbow Extension": 0.1,
    "Wrist Total ROM": 0.2,
    "Total Cervical ROM": 0.3,
    "Shoulder IR": 0.2
}

# Final message that displays the exercises for the athlete
player_programming = ""


# Following section is the functions for each identifier/test

# Liftoffs identifier
def liftoffs(score_dict):
    global player_programming

    player_programming += "Recommended based on Liftoffs test score: \n" # need to account for case it is above 0.5 later

    if score_dict["Shoulder IR"] < 0.5:
        for i in range(len(shoulder_ir_exercises)):
            player_programming += shoulder_ir_exercises[i] + "\n"

    if score_dict["Shoulder Flexion"] < 0.5:
        for i in range(len(shoulder_flexion_exercises)):
            player_programming += shoulder_flexion_exercises[i] + "\n"

    if score_dict["Shoulder Stability"] < 0.5:
        for i in range(len(shoulder_stability_exercises)):
            player_programming += shoulder_stability_exercises[i] + "\n"

# Scapular movement identifier
def scapular_movement(score_dict):
    global player_programming

    player_programming += "Recommended based on Scapular Movement test score: \n"

    if score_dict["Scapular Control"] < 0.5:
        for i in range(len(scapular_control_exercises)):
            player_programming += scapular_control_exercises[i] + "\n"

    if score_dict["Shoulder Stability"] < 0.5:
        for i in range(len(shoulder_stability_exercises)):
            player_programming += shoulder_stability_exercises[i] + "\n"

# Back to Wall Shoulder Flexion identifier
def back_to_wall_shoulder_flexion(score_dict):
    global player_programming

    player_programming += "Recommended based on Back to Wall Shoulder Flexion test score: \n"

    if score_dict["Shoulder Flexion"] < 0.5:
        for i in range(len(shoulder_flexion_exercises)):
            player_programming += shoulder_flexion_exercises[i] + "\n"

    if score_dict["Scapular Control"] < 0.5:
        for i in range(len(scapular_control_exercises)):
            player_programming += scapular_control_exercises[i] + "\n"

    if score_dict["T-spine flexion/extension"] < 0.5:
        for i in range(len(tspine_flexion_extension_exercises)):
            player_programming += tspine_flexion_extension_exercises[i] + "\n"

# Forearm Pronation/Supination identifier
def forearm_pronation_supination(score_dict):
    global player_programming

    player_programming += "Recommended based on Forearm Pronation/Supination test score: \n"

    if score_dict["Forearm Supination"] < 0.5:
        for i in range(len(forearm_supination_exercises)):
            player_programming += forearm_supination_exercises[i] + "\n"

    if score_dict["Elbow Extension"] < 0.5:
        for i in range(len(elbow_extension_exercises)):
            player_programming += elbow_extension_exercises[i] + "\n"

    if score_dict["Wrist Total ROM"] < 0.5:
        for i in range(len(wrist_total_ROM_exercises)):
            player_programming += wrist_total_ROM_exercises[i] + "\n"

# Field Goal Test identifier
def field_goal_test(score_dict):
    global player_programming

    player_programming += "Recommended based on Back to Wall Field Goal test score: \n"

    if score_dict["Shoulder IR"] < 0.5:
        for i in range(len(shoulder_ir_exercises)):
            player_programming += shoulder_ir_exercises[i] + "\n"

    if score_dict["Shoulder Flexion"] < 0.5:
        for i in range(len(shoulder_flexion_exercises)):
            player_programming += shoulder_flexion_exercises[i] + "\n"

    if score_dict["Shoulder Stability"] < 0.5:
        for i in range(len(shoulder_stability_exercises)):
            player_programming += shoulder_stability_exercises[i] + "\n"

    if score_dict["Total Cervical ROM"] < 0.5:
        for i in range(len(total_cervical_ROM_exercises)):
            player_programming += total_cervical_ROM_exercises[i] + "\n"

# Need to consolidate some code later (right now some of it's duplicated)
# Also need to redo order of the lists according to Mike's exercise precedence
    

# Testing
#print(player_scores)
#liftoffs(player_scores)
#scapular_movement(player_scores)
#back_to_wall_shoulder_flexion(player_scores)
#forearm_pronation_supination(player_scores)
#field_goal_test(player_scores)
print(player_programming)

# Gerardo Code

def overhead_squat_screen(score):
    global player_programming
    # Bucket 1:
    if score.get("Overhead Squat", 1.0) < 0.50:
        player_programming.extend(total_hip_rom_exercises)
    # Bucket 2: 
    if score.get("Shoulder Flexion", 1.0) < 0.50:
        player_programming.extend(shoulder_flexion_exercises)
    # Bucket 3: 
    if score.get("T-spine flexion/extension", 1.0) < 0.50:
        player_programming.extend(t_spine_flexion_extension_exercises)
    # Bucket 4: 
    if (score.get("Ankle Dorsiflexion Test", 1.0) < 0.50 or
        score.get("Ankle Eversion and Inversion", 1.0) < 0.50 or
        score.get("Tibial Rotation", 1.0) < 0.50):
        player_programming.extend(ankle_dorsiflexion_exercises)

def low_back_screen(score):
    global player_programming
    # Bucket 1: 
    if score.get("Low Back Screen", 1.0) < 0.50:
        player_programming.extend(t_spine_flexion_extension_exercises)
    # Bucket 2: 
    if (score.get("Thomas Test", 1.0) < 0.50 or
        score.get("Single Leg Stability", 1.0) < 0.50 or
        score.get("Sliders", 1.0) < 0.50):
        player_programming.extend(hip_flexion_hamstring_exercises)
    # Bucket 3: 
    if score.get("Postural Breathing", 1.0) < 0.50:
        player_programming.extend(postural_breathing_exercises)

def pelvic_dissociation_screen(score):
    global player_programming
    # Bucket 1: 
    if score.get("Pelvic Dissociation", 1.0) < 0.50:
        player_programming.extend(total_hip_rom_exercises)
    # Bucket 2: 
    if score.get("Hip Internal Rotation", 1.0) < 0.50:
        player_programming.extend(hip_internal_rotation_exercises)
    # Bucket 3: 
    if score.get("Hip External Rotation", 1.0) < 0.50:
        player_programming.extend(hip_external_rotation_exercises)
    # Bucket 4:
    if score.get("Thoracic Rotation", 1.0) < 0.50:
        player_programming.extend(thoracic_rotation_exercises)

def locked_t_spine_screen(score):
    global player_programming
    # Bucket 1:
    if score.get("Locked T-Spine", 1.0) < 0.50:
        player_programming.extend(thoracic_rotation_exercises)
    # Bucket 2:
    if score.get("T-spine flexion/extension", 1.0) < 0.50:
        player_programming.extend(t_spine_flexion_extension_exercises)

def cervical_screen(score):
    global player_programming
    # Bucket 1:
    if score.get("Cervical Screen", 1.0) < 0.50:
        player_programming.extend(neck_mobility_exercises)
    # Bucket 2:
    if score.get("Upper Cervical ROM", 1.0) < 0.50:
        player_programming.extend(upper_cervical_rom_exercises)
    # Bucket 3:
    if score.get("Total Cervical ROM", 1.0) < 0.50:
        player_programming.extend(total_cervical_rom_exercises)