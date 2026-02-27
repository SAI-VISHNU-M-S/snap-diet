def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr, activity_level):
    multipliers = {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725
    }
    return bmr * multipliers.get(activity_level, 1.2)

def get_macros(total_calories, goal):
    # Ratios: Protein/Carbs/Fats
    ratios = {
        "weight_loss": (0.40, 0.35, 0.25),
        "maintenance": (0.30, 0.45, 0.25),
        "muscle_gain": (0.30, 0.50, 0.20)
    }
    p, c, f = ratios.get(goal, (0.30, 0.45, 0.25))
    
    return {
        "protein_g": (total_calories * p) / 4,
        "carbs_g": (total_calories * c) / 4,
        "fats_g": (total_calories * f) / 9
    }
