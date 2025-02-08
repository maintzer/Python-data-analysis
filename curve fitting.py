# imports
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as scpo
import time

# a constant we'll use later
j = 0

# independent variable & errors
xvalues = np.array([15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
xerrs = np.full((1, 18), 2, dtype=int)

# dependent variable and errors
yvalues = np.array([2.6,3.1,4.5,5.1,6.5,7.1,9.5,8.8,10,13.7,11.9,12.4,13.7,16.5,18,23.6,24.2,24.6])
yerrs = np.full((1, 18), 2, dtype=int)

# another independent variable, defined as arctan(y/x) in degrees
angles = np.array([9.8335639636781,8.81073298551092,10.2039737211827,9.64804531557912,10.5207843133084,10.0651693522184,11.920738539281,9.98182928719618,10.3048464682117,12.8620363664569,10.3746436745613,10.0453303689563,10.3518983647873,11.6538405852074,11.9565842425059,14.6934133697008,14.2913936932336,13.820339526267])
angerrs = np.array([4.5872091630571,3.36637513656478,2.70343494938872,2.23065516711224,1.91877770486896,1.66791480356266,1.50109652788314,1.3281031862156,1.20898471565594,1.1284984709936,1.0213442756097,0.944874510797272,0.883566020181997,0.836565132029845,0.788705229941293,0.75762478762152,0.715871704964732,0.677956662310313])

# linear model
def Line(x, gradient, intercept): 
    return gradient*x + intercept

# quadratic model
def Quadratic(x, A, B, C): 
    return A*x**2 + B*x + C

# a loop to return to if the user is an idiot
while (j != 1) and (j != 2):

    # ask user if we're doing linear or quadratic fitting
    j = int(input("Dataset 1: Enter 1 for a linear fit, or 2 for a quadratic fit. -->  "))

    # linear, dataset 1
    if j == 1 :
        actual_fit_parameters, covariance_matrix = scpo.curve_fit(Line, xvalues,yvalues)
        fit_gradient = actual_fit_parameters[0] 
        fit_intercept = actual_fit_parameters[1]
        ybestfit = Line(xvalues, fit_gradient, fit_intercept)
        plt.figure(figsize=(10, 7))
        plt.errorbar(xvalues,yvalues, xerr = xerrs, yerr = yerrs, fmt = 'o')
        plt.plot(xvalues, ybestfit)
        plt.xlabel("perpendicular distance to object / cm")
        plt.ylabel("max. separation from centre line / cm")
        plt.show()

    # quadratic, dataset 1
    elif j == 2 :
        actual_fit_parameters, covariance_matrix = scpo.curve_fit(Quadratic, xvalues,yvalues)
        fit_C = actual_fit_parameters[2]
        fit_B = actual_fit_parameters[1] 
        fit_A = actual_fit_parameters[0]    
        ybestfit = Quadratic(xvalues, fit_A, fit_B, fit_C)
        plt.figure(figsize=(10, 7))
        plt.errorbar(xvalues,yvalues, xerr = xerrs, yerr = yerrs, fmt = 'o')
        plt.plot(xvalues, ybestfit)
        plt.xlabel("perpendicular distance to object / cm", fontsize = 15)
        plt.ylabel("maximum sensing angle / cm", fontsize = 15)
        plt.show()

    # restart the loop if input is neither 1 or 2
    else:
        print('Error: please choose 1 or 2')
        print('Resetting...')
        time.sleep(1)

#set j back to 0 to do the loop again
j = 0

#do the same for dataset 2
while (j != 1) and (j != 2):

    # ask user if we're doing linear or quadratic fitting
    j = int(input("Dataset 2: Enter 1 for a linear fit, or 2 for a quadratic fit. -->  "))

    # linear, dataset 2
    if j == 1:
        actual_fit_parameters, covariance_matrix = scpo.curve_fit(Line, xvalues,angles)
        fit_gradient = actual_fit_parameters[0] 
        fit_intercept = actual_fit_parameters[1]
        ybestfit = Line(xvalues, fit_gradient, fit_intercept)
        plt.figure(figsize=(10, 7))
        plt.errorbar(xvalues,angles, xerr = xerrs, yerr = angerrs, fmt = 'o')
        plt.plot(xvalues, ybestfit)
        plt.xlabel("perpendicular distance to object / cm", fontsize = 15)
        plt.ylabel("maximum sensing angle / cm", fontsize = 15)
        plt.show()

    # quadratic, dataset 2
    elif j == 2:
        actual_fit_parameters, covariance_matrix = scpo.curve_fit(Quadratic, xvalues,angles)
        fit_C = actual_fit_parameters[2]
        fit_B = actual_fit_parameters[1] 
        fit_A = actual_fit_parameters[0]    
        ybestfit = Quadratic(xvalues, fit_A, fit_B, fit_C)
        plt.figure(figsize=(10, 7))
        plt.errorbar(xvalues,angles, xerr = xerrs, yerr = angerrs, fmt = 'o')
        plt.plot(xvalues, ybestfit)
        plt.xlabel("perpendicular distance to object / cm", fontsize = 15)
        plt.ylabel("maximum sensing angle / cm", fontsize = 15)
        plt.show()
    
    # restart the loop if input is neither 1 or 2
    else:
        print('Error: please choose 1 or 2')
        print('Resetting...')
        time.sleep(1)