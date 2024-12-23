import pandas as pd 

data = {'Age': [25,47,38],
        'Birth Year': [1995,1973,1982],
        'Graduation Year': [2016,2000,2005]
        }

df = pd.DataFrame(data, columns = ['Age','Birth Year','Graduation Year'])

print(df)
print(type(df))