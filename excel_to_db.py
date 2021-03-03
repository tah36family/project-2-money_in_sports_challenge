import pandas as pd
import sqlite3

#Change the path, where you want the database
conn = sqlite3.connect('C:/Users/Owner/Desktop/BASEKETBAL/MONEY_IN_SPORTS.db')

#Change the path , where your csv files are stored
df=pd.read_csv(r'C:/Users/Owner/Downloads/TAS_V1.csv')
df2 = pd.read_csv(r'C:/Users/Owner/Downloads/TAS_V2.csv')

df.to_sql("TAS_V1",conn)

df2.to_sql("TAS_V2",conn)

df.columns =['Athlete', 'Athlete_top_20', 'Sport', '2014_Pay_millions','Endorsements_Millions' , 'Salary_Winnings_millions']
df2.columns =['League', 'Sport_Top_teams_Payroll_List', 'Team', 'Percent_Change_From_Last_Year_Survey','Percent_Change_Over_Last_5_Years' , 'Average_Annual_pay_per_player', 'Average_player_5_year_earnings', 'Last_Year_Rank', 'Rank' ,'Rank_of_Total_Payroll', 'Total_Payroll']

df.to_sql("TAS1_V1",conn,if_exists='replace')
df2.to_sql("TAS2_V1",conn,if_exists='replace')
