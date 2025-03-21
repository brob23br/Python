weight = 41.5
premium_ground = 125

#ground shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight >= 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Standard Ground Shipping:$", cost_ground)
print("Ground Shipping Premium:$", premium_ground)

#drone shipping
if weight <= 2:
  cost_ground = weight * 4.50
elif weight >= 2 and weight <= 6:
  cost_ground = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 12.00
else:
  cost_ground = weight * 14.25
print("Drone Shipping Cost:$", cost_ground)