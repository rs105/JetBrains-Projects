# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:32:52 2020

@author: Romit
"""
import argparse
from math import ceil, log
from sys import argv


def check_for_negatives(*numbers):
    for number in numbers:
        if number and number < 0:
            print("Incorrect parameters")
            exit()


def calculate_payment(P, n, i):
    A = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    print(f"Your annuity payment = {ceil(A)}")


def calculate_principal(A, n, i):
    P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your credit principal = {P}!")


def calculate_periods(A, P, i):
    count_of_months = log(A / (A - i * P), 1 + i)
    n = ceil(count_of_months)
    overpayment = n * A - P
    print(f"You need {n // 12} years and {n % 12} months to repay this credit!")
    print(f"Overpayment = {overpayment}")
    
def calculate_diff_payment(P, n, i):
    total_payment = 0
    for m in range(1, n + 1):
        D = (P / n) + i * (P - (P * (m - 1)) / n)
        total_payment += ceil(D)
        print(f"Month {m}: paid out {ceil(D)}")
    overpayment = total_payment - P
    print(f"Overpayment = {overpayment}")


if len(argv) < 5:
    print("Incorrect parameters")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if not args.interest:
    print("Incorrect parameters")
    exit()

i = args.interest / (12 * 100)

check_for_negatives(args.payment, args.principal, args.periods, args.interest)

if args.type == "annuity":
    if not args.payment:
        calculate_payment(args.principal, args.periods, i)
    elif not args.principal:
        calculate_principal(args.payment, args.periods, i)
    else:
        calculate_periods(args.payment, args.principal, i)
elif args.type == "diff":
    calculate_diff_payment(args.principal, args.periods, i)
else:
    print("Incorrect parameters")
        


    
    
