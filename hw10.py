# ----------------------------------------------------------------------
# Name:        hw10
# Purpose:     to gain familiarity with using the Pandas package
#
# Date:        04/25/2019
# ----------------------------------------------------------------------
"""
This module uses Pandas to load the data within '2019 FE Guide.csv' into
a Pandas DataFrame, then answers 11 questions about the data by
performing a series of operations on the DataFrame.
"""
import pandas as pd


def q1(table):
    """
    How many cars are made by the manufacturer Honda?
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (int) - number of cars made by Honda
    """
    return len(table.loc[table['Mfr Name'] == 'Honda'])


def q2(table):
    """
    Finds how many 'Guzzlers' there are
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (int) - number of gas guzzlers
    """
    return len(table.loc[table['Guzzler?'] == 'G'])


def q3(table):
    """
    Determines the FE value of the highest combined Fuel Efficiency car
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (float) - the highest Combined Fuel Efficiency
    """
    return table['Comb FE (Guide) - Conventional Fuel'].max()


def q4(table):
    """
    Finds the division and car line with the lowest combined Fuel
    Efficiency using Conventional Fuel
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (string, string) - (<Division>, <Carline>) with the lowest
             combined fuel efficiency
    """
    lowest_mpg = table['Comb FE (Guide) - Conventional Fuel'].idxmin()
    return table.loc[lowest_mpg, 'Division'], table.loc[lowest_mpg, 'Carline']


def q5(table):
    """
    Determines the highest combined FE - Conventional Fuel among all
    wheel drives.
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (float) - the highest combined FE among AWD vehicles
    """
    awd = table.loc[table['Drive Desc'] == 'All Wheel Drive']
    return awd['Comb FE (Guide) - Conventional Fuel'].max()


def q6(table):
    """
    Which car line has the largest difference between Highway and City
    Fuel efficiency - Conventional Fuel?
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (string) the car line with the biggest mileage difference
    """
    city = 'City FE (Guide) - Conventional Fuel'
    hwy = 'Hwy FE (Guide) - Conventional Fuel'
    diffs = abs(table[hwy] - table[city])
    return table.iloc[diffs.idxmax()]['Carline']


def q7(table):
    """
    Calculates the average annual fuel cost of all supercharged cars?
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (float) - the average annual fuel cost of supercharged cars
    """
    sc = table.loc[table['Air Aspiration Method Desc'] == 'Supercharged']
    return sc['Annual Fuel1 Cost - Conventional Fuel'].mean()


def q8(table):
    """
    What SUV has the lowest annual fuel cost? Uses "Carline Class Desc"
    to identify SUVs.
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (string) suv/carline with the lowest annual fuel cost
    """
    suvs = table.loc[table['Carline Class Desc'].str.contains('SUV', na=False)]
    return table.loc[suvs['Annual Fuel1 Cost - Conventional Fuel'].idxmin(),
                     'Carline']


def q9(table):
    """
    Which manufacturer has the most cars with manual transmission?
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (string) - The manufacturer selling the most manual
    transmission cars
    """
    manual = table.loc[table['Transmission'].str.contains('Manual', na=False)]
    return manual.groupby('Mfr Name').count()['Transmission'].idxmax()


def q10(table):
    """
    What is the average annual fuel cost by car division?
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (Pandas Series) a series representing the average annual
    fuel cost by car division
    """
    afc = 'Annual Fuel1 Cost - Conventional Fuel'
    return table.groupby('Division').mean()[afc]
    
    # series = pd.Series()
    # for group, dframe in table.groupby("Division"):
    #     series[group] =
    #             dframe['Annual Fuel1 Cost - Conventional Fuel'].mean()
    # return series


def q11(table):
    """
    A function that returns our perfect car based on our criteria.
    Criteria:
    - Drive System:         All Wheel Drive
    - Engine Displacement:  3.5+ L
    - Transmission:         Selectable Continuously Variable
    - Fuel Economy:         30+
    - Hybrid:               Yes
    - # Batteries:          1+
    :param table: Pandas DataFrame representing '2019 FE Guide.csv'
    :return: (string) - the perfect carline for us.
    """
    result = table.loc[
        (table["Drive Desc"] == 'All Wheel Drive') &
        (table["Eng Displ"] >= 3.5) &
        (table['Comb FE (Guide) - Conventional Fuel'] >= 30) &
        (table['Trans Desc'] ==
         'Selectable Continuously Variable (e.g. CVT with paddles)') &
        (table['Guzzler?'] != 'G') &
        (table['# Batteries'] >= 1),
        ['Division', "Carline"]]
    return result.iloc[0]['Carline']


def main():
    table = pd.read_csv('2019 FE Guide.csv')

    print('-----------Q1:-----------')
    print(q1(table))
    print('-----------Q2:-----------')
    print(q2(table))
    print('-----------Q3:-----------')
    print(q3(table))
    print('-----------Q4:-----------')
    print(q4(table))
    print('-----------Q5:-----------')
    print(q5(table))
    print('-----------Q6:-----------')
    print(q6(table))
    print('-----------Q7:-----------')
    print(q7(table))
    print('-----------Q8:-----------')
    print(q8(table))
    print('-----------Q9:-----------')
    print(q9(table))
    print('-----------Q10:----------')
    print(q10(table))
    print('-----------Q11:----------')
    print(q11(table))


if __name__ == "__main__":
    main()