# Introduction
  # Jrf (t)    = Rainfall rate
  # E(t)    = Evaporation rate
  # S_d     = Storage cover layer (shallow storage)
  # S_wb    = Storage waste layer
  # S_dr    = Storage drainage layer
  # L_d(t)  = leachate cover layer
  # L_wb(t) = Leachate drainage layer 
  # Q_dr    = Leachate production 

#Initialization of the code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import solve_ivp
import scipy.integrate as spint
%matplotlib inline

# Matching the data set so data for the same dates are used for rainfall and leacheate:

# Calling the database

LeachateData = pd.read_excel ('C:/Users/mazen/Desktop/LeachateData.xlsx', index_col = 0)
MetoData = pd.read_excel ('C:/Users/mazen/Desktop/MetoData.xlsx', index_col = 0)

#Matching the database: Data with the same date for leachate (Qdr), Rainfall ((Jrf), and Evaporation (E)

Qdr = LeachateData.iloc[:, 0]                   # leachate output in [m^3/day]
Jrf = MetoData.iloc[-len(Qdr) + 1 : -1, 1]      # Precipitation [m/day]
pE = MetoData.iloc[-(len(Qdr) +1): -1, 2]        # Evaporation  [m/day]

# Definition of rate equation 
def dydt(t,S):
  """Return the rate of change of storages"""
  Scl = S[0]
  Swb = S[1]
  
  Seff_cl = (Scl - Sclmin)/(Sclmax - Sclmin)
  Lcl = acl * Seff_cl**bcl
  
  Seff_wb = (Swb - Swbmin)/(Swbmax - Swbmin)
  Lwb = awb * Seff_wb**bwb
  
  E = pE * Cf *fred
  Beta = Beta0 * Seff_cl
  
  # Equations
  dScldt = Jrf - Lcl - E
  dSwbdt = (1 - Beta) * Lcl - Lwb

  return np.array([dScldt, dSwbdt,Qdr])

# Definition of parameters

Sclmax = 0.3 * 15   # Maximum storage is reached when all porosity is filled with water [m]
Sclmin = 0          # Minimum storage range between zero and 5 [m], Zero is chosen as the initial value 
bcl = 1             # Assumed
acl = #(10% * max(Qdr)value + max (Qdr value) [in m/day] - here we should make use of the 

Swbmax = 7.5        # how 
Swbmin = 0          #
awb = 0.001         # how
bwb = 30            #

Beta0 = 0.92        #
Cf = 0.92           #
fred = 1            # Assuming no reduction in evaporation 

# Initial case:
