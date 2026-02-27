from flask import Flask, request, jsonify
from nutrition_logic import calculate_bmr, calculate_tdee, get_macros

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    bmr = calculate_bmr(data['weight'], data['height'], data['age'], data['gender'])
    tdee = calculate_tdee(bmr, data['activity'])
    
    # Adjust calories based on goal
    target_calories = tdee - 500 if data['goal'] == 'weight_loss' else tdee + 500
    macros = get_macros(target_calories, data['goal'])
    
    return jsonify({
        "target_calories": round(target_calories),
        "macros": macros
    })

if __name__ == '__main__':
    app.run(debug=True)
