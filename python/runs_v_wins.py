from pybaseball import schedule_and_record
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cardinals25 = schedule_and_record(2025, 'STL')
cardinals24 = schedule_and_record(2024, 'STL')
cardinals23 = schedule_and_record(2023, 'STL')
cardinals22 = schedule_and_record(2022, 'STL')
cardinals21 = schedule_and_record(2021, 'STL')   
cardinals19 = schedule_and_record(2019, 'STL')

cardinals25 = cardinals25.drop("Attendance", axis=1)
cardinals24 = cardinals24.drop("Attendance", axis=1)
cardinals23 = cardinals23.drop("Attendance", axis=1)
cardinals22 = cardinals22.drop("Attendance", axis=1)
cardinals21 = cardinals21.drop("Attendance", axis=1)
cardinals19 = cardinals19.drop("Attendance", axis=1)

cardinals25['Year'] = 2025
cardinals24['Year'] = 2024
cardinals23['Year'] = 2023
cardinals22['Year'] = 2022
cardinals21['Year'] = 2021
cardinals19['Year'] = 2019

stacked = pd.concat([cardinals25, cardinals24, cardinals23, cardinals22, cardinals21, cardinals19])

stacked.to_csv("win-loss-record.csv")

cardinals25['win-count'] = np.where(cardinals25['W/L']=='W', 1, 0).cumsum()
cardinals24['win-count'] = np.where(cardinals24['W/L']=='W', 1, 0).cumsum()
cardinals23['win-count'] = np.where(cardinals23['W/L']=='W', 1, 0).cumsum()
cardinals22['win-count'] = np.where(cardinals22['W/L']=='W', 1, 0).cumsum()
cardinals21['win-count'] = np.where(cardinals21['W/L']=='W', 1, 0).cumsum()
cardinals19['win-count'] = np.where(cardinals19['W/L']=='W', 1, 0).cumsum()


plt.plot(cardinals25['win-count'],label=" '25 Cardinals")
plt.plot(cardinals24['win-count'],label=" '24 Cardinals")
plt.plot(cardinals23['win-count'],label=" '23 Cardinals")
plt.plot(cardinals22['win-count'],label=" '22 Cardinals")
plt.plot(cardinals21['win-count'],label=" '21 Cardinals")
plt.plot(cardinals19['win-count'],label=" '19 Cardinals")
plt.legend(loc=4)
plt.ylabel('Win Count')
plt.title('Record Throughout Season')
plt.show()

cardinals25['scorediff'] = (cardinals25['R'] - cardinals25['RA']).cumsum()
cardinals24['scorediff'] = (cardinals24['R'] - cardinals24['RA']).cumsum()
cardinals23['scorediff'] = (cardinals23['R'] - cardinals23['RA']).cumsum()
cardinals22['scorediff'] = (cardinals22['R'] - cardinals22['RA']).cumsum()
cardinals21['scorediff'] = (cardinals21['R'] - cardinals21['RA']).cumsum()
cardinals19['scorediff'] = (cardinals19['R'] - cardinals19['RA']).cumsum()

plt.plot(cardinals25['scorediff'],label=" '25 Cardinals")
plt.plot(cardinals24['scorediff'],label=" '24 Cardinals")
plt.plot(cardinals23['scorediff'],label=" '23 Cardinals")
plt.plot(cardinals22['scorediff'],label=" '22 Cardinals")
plt.plot(cardinals21['scorediff'],label=" '21 Cardinals")
plt.plot(cardinals19['scorediff'],label=" '19 Cardinals")
plt.legend(loc=3)
plt.xlabel('Games into Season')
plt.ylabel('Runs Scored - Runs Against')
plt.title('Cumulative Run Differential')
plt.show()