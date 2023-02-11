from simulate import Simulation

m1 = Simulation(23,1000)
m1.simulation()



#AIM : Monte Carlo mathematical simulation of Birthday paradox

# ALGORITHM
# Step 1: choose group size N
# Step 2: randomly assign date(1-365) to all N person
# Step 3: Check whether persons having same date of birth. if yes counted the event in shared bithdays.
# Step 4: from step 1 to 3 repeat for X number of time.
# Step 5: divide the count of trials having peoples with same bithday / total number of trials