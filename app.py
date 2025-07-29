from flask import Flask, render_template, request
from case_data import Paragon_Cases
from easyship_data import Easyship_Cases
from sim_data import SIM_Cases

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # First get all form inputs
    selected_type = request.form.get("type_selection")
    selected_cycle = request.form.get("cycle")
    selected_stage = request.form.get("stage_of_issue")
    generate_details_clicked = 'generate_details' in request.form

    # Initialize variables
    data_source = {}
    stages_to_display = []
    problems_in_stage = {}
    case_details = None
    selected_problem_name_for_display = None

    # Determine which data source to use
    if selected_type == "Easyship":
        data_source = Easyship_Cases
    elif selected_type == "MLF":
        data_source = Paragon_Cases
    elif selected_type == "SIM":
        data_source = SIM_Cases

    # Logic to populate stages based on cycle selection
    if selected_cycle and selected_cycle in data_source:
        stages_to_display = list(data_source[selected_cycle].keys())
        if selected_stage and selected_stage in data_source[selected_cycle]:
            problems_in_stage = data_source[selected_cycle][selected_stage]

    # Logic for displaying case details
    if generate_details_clicked and selected_cycle and selected_stage:
        if problems_in_stage:
            first_problem_key = next(iter(problems_in_stage))
            if selected_type == "MLF":
                case_details = problems_in_stage[first_problem_key]
            else:  # For Easyship and SIM
                case_details = {"blurb": problems_in_stage[first_problem_key]}
            selected_problem_name_for_display = first_problem_key

    return render_template(
        "index.html",
        types=["MLF", "Easyship", "SIM"],
        selected_type=selected_type,
        cycles=data_source.keys() if data_source else [],
        stages_to_display=stages_to_display,
        selected_cycle=selected_cycle,
        selected_stage=selected_stage,
        case_details=case_details,
        selected_problem_name_for_display=selected_problem_name_for_display
    )

#if __name__ == '__main__':
 #   app.run(debug=True)