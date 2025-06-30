#
# Assigment 13 = Wind Chill Calculations
#
# Author = Estefania Ortiz
#

C = " "
F = " "
t = 0


def temp (t):
    t = (9/5 * temperature_chosen) + 32
    return(t)

temperature_chosen = float (input("What is the temperature? "))
scale = input ("Fahrenheit or Celsius (F/C)? ").upper()

def wind ():
        if scale == C:
            print (t)
        else:
            t = temperature_chosen            
            print(t)
        for i in range (5, 65, 5):
              wind_chill = 35.74 + (0.6215*t) -35.75*(i**0.16) + 0.4275 *((t)* (i**0.16))
              print (f"At temperature {t}F, and wind speed {i} mph, the windchill is: {wind_chill:.2f}F")

temp (t)
wind()
            
