from flask import Flask, render_template, request

app = Flask(__name__)

# ========= EXERCISE LISTS =========
# These lists contain exercises recommended for specific mobility issues.

ankle_dorsiflexion_exercises = [
    "Banded Ankle Mobilizations", "Wall Dorsiflexion Reach", "Weighted Knee-to-Wall Dorsiflexion",
    "Slant Board Calf Stretch", "Foam Roll Calf + Active Pump"
]
ankle_eversion_inversion_exercises = [
    "Tibialis Anterior Raises",
    "Lateral Ankle Resisted Eversion with Band",
    "Heel Walks",
    "Ankle Alphabet (controlled foot circles)",
    "Banded Inversion/Eversion Isometrics"
]
tibial_rotation_exercises = [
    "Seated Tibial Rotations", "Standing Tibial Rotations with Band", "Foot Arch Lifts"
]
thomas_test_exercises = [
    "Kneeling Hip Flexor Stretch", "Couch Stretch", "Psoas Release with Ball"
]
cossack_squat_exercises = [
    "Cossack Squat Progressions", "Adductor Mobilizations", "Deep Squat Holds"
]
seated_active_hip_rotation_exercises = [
    "90/90 Internal/External Rotations", "Hip CARs (Controlled Articular Rotations)"
]
single_leg_stability_exercises = [
    "Single Leg Balance", "Pistol Squat Progressions", "Single Leg RDL"
]
sliders_exercises = [
    "Slider Lunges", "Slider Hamstring Curls", "Slider Adductions"
]
overhead_squat_exercises = [
    "Overhead Squat Progressions", "Thoracic Spine Extensions", "Shoulder Mobility Drills"
]
low_back_screen_exercises = [
    "Cat-Cow", "Bird-Dog", "Pelvic Tilts"
]
pelvic_dissociation_exercises = [
    "Pelvic Tilts in Quadruped", "Hip Hinge Drills", "Segmental Rolling"
]
locked_t_spine_exercises = [
    "Thoracic Spine Rotations", "Foam Roll Thoracic Extension", "Thread the Needle"
]
cervical_screen_exercises = [
    "Cervical CARs", "Neck Rotations", "Chin Tucks"
]
liftoffs_exercises = [
    "Sleeper Stretch PAILs/RAILs", "Prone Lift-offs", "Banded Lift-Offs",
    "Wall Tricep Stretch", "External Rotation ISOs"
]
scapular_movement_exercises = [
    "Scapular CARs", "Overhead Scaption Raise", "Single Arm Serratus Wall Slide",
    "Medicine Ball Wall Taps"
]
back_to_wall_shoulder_flexion_exercises = [
    "Back to Wall Shoulder Flexion Progressions", "Lat Hangs", "Doorway Stretch"
]
forearm_pronation_supination_exercises = [
    "Supination/Pronation PAILs/RAILs", "Supinator ISOs", "Wrist CARs"
]
field_goal_test_exercises = [
    "Shoulder External Rotation Drills", "T-Spine Rotations", "Cervical Rotations"
]
pec_exercises = [
    "Pec Stretch (Doorway)", "Foam Roll Pec Release", "Banded Pec Stretch"
]
lat_exercises = [
    "Lat Stretch (Overhead)", "Foam Roll Lat Release", "Lat Pulldown Stretch"
]
trap_exercises = [
    "Upper Trap Stretch", "Levator Scapulae Stretch", "Scapular Retractions"
]


# ========= SCREENING FUNCTIONS =========
# Each function checks a specific test score and adds relevant exercises to the 'programming' list.

def generate_recommendations(score):
    programming = {
        "Lower Body Mobility": [],
        "Thoracic Spine Mobility": [],
        "Upper Body Mobility": [],
        "Tissue Mobility": []
    }

    # Lower Body
    if score.get("Ankle Dorsiflexion", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(ankle_dorsiflexion_exercises)
    if score.get("Ankle Eversion & Inversion", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(ankle_eversion_inversion_exercises)
    if score.get("Tibial Rotation", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(tibial_rotation_exercises)
    if score.get("Thomas Test", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(thomas_test_exercises)
    if score.get("Cossack Squat", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(cossack_squat_exercises)
    if score.get("Seated Active Hip Rotation", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(seated_active_hip_rotation_exercises)
    if score.get("Single Leg Stability", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(single_leg_stability_exercises)
    if score.get("Sliders", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(sliders_exercises)
    if score.get("Overhead Squat", 1.0) < 0.5:
        programming["Lower Body Mobility"].extend(overhead_squat_exercises)

    # Thoracic Spine
    if score.get("Low Back Screen", 1.0) < 0.5:
        programming["Thoracic Spine Mobility"].extend(low_back_screen_exercises)
    if score.get("Pelvic Dissociation", 1.0) < 0.5:
        programming["Thoracic Spine Mobility"].extend(pelvic_dissociation_exercises)
    if score.get("Locked T-Spine", 1.0) < 0.5:
        programming["Thoracic Spine Mobility"].extend(locked_t_spine_exercises)
    if score.get("Cervical Screen", 1.0) < 0.5:
        programming["Thoracic Spine Mobility"].extend(cervical_screen_exercises)

    # Upper Body
    if score.get("Liftoffs", 1.0) < 0.5:
        programming["Upper Body Mobility"].extend(liftoffs_exercises)
    if score.get("Scapular Movement", 1.0) < 0.5:
        programming["Upper Body Mobility"].extend(scapular_movement_exercises)
    if score.get("Back to Wall Shoulder Flexion", 1.0) < 0.5:
        programming["Upper Body Mobility"].extend(back_to_wall_shoulder_flexion_exercises)
    if score.get("Forearm Pronation/Supination", 1.0) < 0.5:
        programming["Upper Body Mobility"].extend(forearm_pronation_supination_exercises)
    if score.get("Field Goal Test", 1.0) < 0.5:
        programming["Upper Body Mobility"].extend(field_goal_test_exercises)

    # Tissue
    if score.get("Pec", 1.0) < 0.5:
        programming["Tissue Mobility"].extend(pec_exercises)
    if score.get("Lat", 1.0) < 0.5:
        programming["Tissue Mobility"].extend(lat_exercises)
    if score.get("Trap", 1.0) < 0.5:
        programming["Tissue Mobility"].extend(trap_exercises)

    # Remove duplicates per category
    for key in programming:
        programming[key] = list(set(programming[key]))

    return programming


# ========= ROUTES =========
# Defines the web pages for the application.

@app.route('/')
def index():
    # Renders the main input form page.
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handles the form submission from index.html.
    form_data = request.form
    score_dict = {}

    # Iterates through the form data to convert scores to floats.
    # Defaults to 1.0 if input is blank or invalid (ValueError).
    for key in form_data:
        try:
            score_dict[key] = float(form_data[key])
        except ValueError:
            score_dict[key] = 1.0  # Default to 1.0 (no issue) if input is blank or invalid

    # Generates exercise recommendations based on the submitted scores.
    recommendations = generate_recommendations(score_dict)

    # Renders the results page, passing the list of recommended exercises.
    return render_template('results.html', grouped_exercises=recommendations)

if __name__ == '__main__':
    # Runs the Flask application in debug mode.
    # For local network access, you can use host='0.0.0.0'
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
