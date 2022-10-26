# How long lasagna needs to bake
EXPECTED_BAKE_TIME = 40

# Calculate the minutes left to bake for lasagna
def bake_time_remaining(EXPECTED_BAKE_TIME, elapsed_minutes):
    return EXPECTED_BAKE_TIME - elapsed_minutes

# Calculate time to prepare
def preparation_time_in_minutes(num_layers):
    return int(num_layers) * 2

# Return elapsed cooking time.

# This function takes two numbers representing the number of layers & the time already spent
# baking and calculates the total elapsed minutes spent cooking the lasagna.
def elapsed_time_in_minutes(elapsed_minutes, preparation_time):
    return elapsed_minutes + preparation_time
