# Python Program to Calculate Norton's Theorem
# Electrical Engineering - Network Analysis

print("==============================================")
print("           NORTON'S THEOREM")
print("==============================================")

# Input values
V = float(input("Enter source voltage V (V): "))
R1 = float(input("Enter R1 (ohm): "))
R2 = float(input("Enter R2 (ohm): "))
RL = float(input("Enter load resistance RL (ohm): "))

# ------------------------------------------------
# Step 1: Calculate Norton Current
# ------------------------------------------------
# Short-circuit current at the load terminals

In = V / R1

# ------------------------------------------------
# Step 2: Calculate Norton Resistance
# ------------------------------------------------
# Voltage source is replaced by a short circuit

Rn = (R1 * R2) / (R1 + R2)

# ------------------------------------------------
# Step 3: Calculate Load Current
# ------------------------------------------------
# Norton equivalent: In in parallel with Rn

IL = In * Rn / (Rn + RL)

# ------------------------------------------------
# Step 4: Calculate Load Voltage
# ------------------------------------------------

VL = IL * RL

# Display results
print("\n------------- RESULTS ----------------")
print(f"Norton Current (In)      = {In:.2f} A")
print(f"Norton Resistance (Rn)   = {Rn:.2f} ohm")
print(f"Load Current (IL)        = {IL:.4f} A")
print(f"Load Voltage (VL)        = {VL:.2f} V")
print("--------------------------------------")
print("Norton Equivalent Circuit Calculated")
print("======================================")
