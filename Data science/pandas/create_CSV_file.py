# square_feet,num_rooms,num_bathrooms,price
# 1500,3,2,300000
# 2000,4,3,400000
# 2500,4,3,500000
# 1800,3,2,350000
# 2200,4,3,450000
# 1600,3,2,320000
# 2100,4,3,430000
# 1700,3,2,340000
# 2300,4,3,470000
# 1900,3,2,360000

import pandas as pd

# Data
data = {
    'square_feet': [1500, 2000, 2500, 1800, 2200, 1600, 2100, 1700, 2300, 1900],
    'num_rooms': [3, 4, 4, 3, 4, 3, 4, 3, 4, 3],
    'num_bathrooms': [2, 3, 3, 2, 3, 2, 3, 2, 3, 2],
    'price': [300000, 400000, 500000, 350000, 450000, 320000, 430000, 340000, 470000, 360000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('house_prices.csv', index=False)

print("house_prices.csv file has been created.")