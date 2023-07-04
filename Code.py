#Completely Randomized Design (CRD):

import pandas as pd
import statsmodels.api as sm
# Read data from CSV
data = pd.read_csv('crd_data.csv')
# Perform analysis
model = sm.formula.ols('Yield ~ Treatment', data=data).fit()
print(model.summary())

#Randomized Complete Block Design (RCBD):

import pandas as pd
import statsmodels.api as sm
# Read data from CSV
data = pd.read_csv('rcbd_data.csv')
# Perform analysis
model = sm.formula.ols('Yield ~ Treatment + Block', data=data).fit()
print(model.summary())

#Split-Plot Design:

import pandas as pd
import statsmodels.api as sm
# Read data from CSV
data = pd.read_csv('split_plot_data.csv')
# Perform analysis
model = sm.formula.ols('Yield ~ Treatment + WholePlot + SubPlot', data=data).fit()
print(model.summary())

#Factorial Design:

import pandas as pd
import statsmodels.api as sm
# Read data from CSV
data = pd.read_csv('factorial_data.csv')
# Perform analysis
model = sm.formula.ols('Yield ~ Factor1 * Factor2', data=data).fit()
print(model.summary())

#Latin Square Design:

import pandas as pd
import statsmodels.api as sm
# Read data from CSV
data = pd.read_csv('latin_square_data.csv')
# Perform analysis
model = sm.formula.ols('Yield ~ Row + Column', data=data).fit()
print(model.summary())


