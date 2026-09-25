# MAIN INFORMATION
# Course: Just for fun
# Name: Test Problem
# Author: Nolan Savage
# Date: 2026-09-24


# Practice Problem: Picnic Blanket Coverage
# Description

# A city park has a grassy area measuring 2500 m².

# People bring rectangular picnic blankets to the park. The user will enter
# the length and width of a blanket in centimeters.

# Your program must:

# Calculate the area of the blanket in cm².
# Convert the blanket area to m².
# Determine how many blankets could fit in the 2500 m² park.
# Display the result rounded to two decimal places.

GRASSY_AREA = 2500


blanket_length = float(input('Please enter the length of the blanket: '))
blanket_width = float(input('Please enter the width of the blanket: '))

# Blanket area math is length times width
blanket_area = float(blanket_length * blanket_width)



# Converting the blanket area into metres squared
blanket_meteres_squared = blanket_area / 10000


blanket_amount = GRASSY_AREA / blanket_meteres_squared
print(f"You can fit {blanket_amount:.2f} amount of blankets in the Grassy Area")
