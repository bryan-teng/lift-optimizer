import numpy as np

from objects import *


def generate_boolean_based_on_probability(number_of_results, probability_of_true):
    s = np.random.choice([0,1],size=number_of_results, replace=True, p=[1-probability_of_true,probability_of_true])
    return s[0]


def add_lift_transaction_based_on_probability(p, timestamp, start_floor, end_floor, q):
    result = generate_boolean_based_on_probability(1,p)

    if result:
        q.put(LiftRequest(timestamp, start_floor, end_floor))


def return_nearest_lift(lift_1, lift_2, current_floor):
    lift_1_difference = abs(lift_1.current_floor - current_floor)
    lift_2_difference = abs(lift_2.current_floor - current_floor)

    if lift_1_difference < lift_2_difference:
        return lift_1
    else:
        return lift_2

def main():
    pass
    # print(generate_boolean_based_on_probability(1,0.5))

if __name__ == "__main__":
    main()