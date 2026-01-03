steps_taken = 9000
step_goal = 10000
calories_burned = 350
calorie_goal = 500
morning_exercise = False

all_conditions_met = True

if steps_taken <= step_goal and calories_burned <= calorie_goal and not morning_exercise:
    all_conditions_met = False
  
print("Have all conditions been met?", all_conditions_met)