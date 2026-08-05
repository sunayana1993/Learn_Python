class chai:
    temperature="hot"
    strength="strong"

cutting=chai()
print(cutting.temperature)

cutting.temperature="Mild"
print(f"After changing {cutting.temperature}")

del cutting.temperature
print(f"After changing2 {cutting.temperature}")

#If reference is deleted , it falls back to attribute referencing to chai itself

