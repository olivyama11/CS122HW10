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
    return len(table[table['Mfr Name'] == 'Honda'])


def q2(table):
    return len(table[table['Guzzler?'] == 'G'])


def q3(table):
    return table['Comb FE (Guide) - Conventional Fuel'].max()


def q4(table):
    lowest_mpg = table['Comb FE (Guide) - Conventional Fuel'].idxmin()
    # carline = table.iloc[lowest_mpg].loc['Division']
    # manufac = table.iloc[lowest_mpg].loc['Carline']
    return table.loc[lowest_mpg, 'Division'], table.loc[lowest_mpg, 'Carline']


def q5(table):
     awd = table[table['Drive Desc'] == 'All Wheel Drive']
     return  awd['Comb FE (Guide) - Conventional Fuel'].max()


# def q6(table):
#
# def q7(table):
#
#
# def q8(table):
#
# def q9(table):
#
# def q10(table):
#
# def q11(table):






def main():
    table = pd.read_csv('2019 FE Guide.csv')
    print(q1(table))
    print(q2(table))
    print(q3(table))
    print(q4(table))
    print(q5(table))




if __name__ == "__main__":
    main()
