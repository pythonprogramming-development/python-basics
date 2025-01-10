# simple data analysis using Pandas:

import pandas as pd

# Load data
data = {'Age': [25, 47, 38],
        'Birth Year': [1995, 1973, 1982],
        'Graduation Year': [2016, 2000, 2005]}

df = pd.DataFrame(data)

# Display data
print(df)

# Basic statistics
print(df.describe())

# Data visualization
import matplotlib.pyplot as plt
df['Age'].plot(kind='hist')
plt.show()