# ----------------------------------------------------------------------
# Name:        hw10
# Purpose:
#
# Date:        04/25/2019
# ----------------------------------------------------------------------
"""

"""
import pandas as pd
import re


def q1(table):
    return len(table.loc[table['Mfr Name'] == 'Honda'])


def q2(table):
    return len(table.loc[table['Guzzler?'] == 'G'])


def q3(table):
    return table['Comb FE (Guide) - Conventional Fuel'].max()


def q4(table):
    lowest_mpg = table['Comb FE (Guide) - Conventional Fuel'].idxmin()
    # carline = table.iloc[lowest_mpg].loc['Division']
    # manufac = table.iloc[lowest_mpg].loc['Carline']
    return table.loc[lowest_mpg, 'Division'], table.loc[lowest_mpg, 'Carline']


def q5(table):
     awd = table.loc[table['Drive Desc'] == 'All Wheel Drive']
     return  awd['Comb FE (Guide) - Conventional Fuel'].max()


# def q6(table):
#
def q7(table):
    sc = table.loc[table['Air Aspiration Method Desc'] == 'Supercharged']
    return sc['Annual Fuel1 Cost - Conventional Fuel'].mean()

# def q8(table):
#
def q9(table):
    manual = table.loc[table['Transmission'].str.contains('Manual', na=False)]
    return manual.groupby('Mfr Name').count()['Transmission'].idxmax()

# def q10(table):
#
def q11(table):
    pass





def main():
    table = pd.read_csv('2019 FE Guide.csv')
    print(q1(table))
    print(q2(table))
    print(q3(table))
    print(q4(table))
    print(q5(table))

    print(q7(table))

    print(q9(table))

    print(q11(table))


if __name__ == "__main__":
    main()
