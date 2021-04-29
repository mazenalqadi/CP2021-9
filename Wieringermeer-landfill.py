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
import pandas as dp
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

Qdr = LeachateData.iloc[:, 1]                   # leachate output in [m^3/day]
Jrf = MetoData.iloc[-len(Qdr) + 1 : -1, 1]      # Precipitation [m/day]
E = MetoData.iloc[-(len(Qdr) +1): -1, 2]        # Evaporation  [m/day]

# Definition of rate equation 
def dydt(t,S):
  Scl = S[0]
  Swb = S[1]
  Seff_cl = (Scl - Sclmin)/(Sclmax - Sclmin)
  Lcl = acl * Seff_cl**bcl
  
  #Equations
  dScldt = Jrf - Lcl - E

  return np.array([dScldt, dSwbdt,Qdr])
