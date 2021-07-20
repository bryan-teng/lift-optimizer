import queue

import matplotlib.pyplot as plt

from utils import *
from objects import *


def simulate(lift_1_default, lift_2_default, lift_3_default, verbose=False):
    
    lift_1 = Lift(lift_1_default)
    lift_2 = Lift(lift_2_default)

    lift_1b = Lift(lift_1_default)
    lift_2b = Lift(lift_3_default)
    qa = queue.Queue()
    qb = queue.Queue()

    seconds = 0
    bucket_of_waiting_times_a = []
    bucket_of_waiting_times_b = []

    while seconds<60000:
        if (seconds % 10000 == 0) and verbose:
            print(f"{seconds} seconds through the current simulation")
            print(f"current queue size for A is {qa.qsize()}")
            print(f"current queue size for B is {qb.qsize()}")
        # print(f"time now is {seconds}")
        lift_1.update_occupied_state(seconds)
        lift_2.update_occupied_state(seconds)

        lift_1b.update_occupied_state(seconds)
        lift_2b.update_occupied_state(seconds)

        add_lift_transaction_based_on_probability(0.002,seconds,1,2,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,3,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,4,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,5,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,6,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,7,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,8,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,9,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,1,10,qa, qb)

        add_lift_transaction_based_on_probability(0.002,seconds,10,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,9,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,8,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,7,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,6,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,5,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,4,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,3,1,qa, qb)
        add_lift_transaction_based_on_probability(0.002,seconds,2,1,qa, qb)


        # CASE A
        if qa.qsize() != 0:
            if (not lift_1.occupied) and (not lift_2.occupied):
                if qa.qsize() == 1:
                    request_1 = qa.get()

                    fastest_lift_for_1 = return_nearest_lift(lift_1, lift_2, request_1.start_floor)

                    waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                    # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                    fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                    bucket_of_waiting_times_a.append(waiting_time_for_1 + (seconds-request_1.timestamp))

                elif qa.qsize() >= 2:
                    request_1 = qa.get()
                    request_2 = qa.get()

                    fastest_lift_for_1 = return_nearest_lift(lift_1, lift_2, request_1.start_floor)

                    if fastest_lift_for_1 == lift_1:
                        fastest_lift_for_2 = lift_2
                    else:
                        fastest_lift_for_2 = lift_1

                    waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                    waiting_time_for_2 = (abs(fastest_lift_for_2.current_floor - request_2.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    travel_time_for_2 = (abs(request_2.end_floor - request_2.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    total_time_for_2 = waiting_time_for_2 + travel_time_for_2 + DOOR_CLOSING_TIME


                    fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                    fastest_lift_for_2.ferry_passenger(request_2.end_floor, (seconds+total_time_for_2))

                    # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")
                    # print(f"waiting time is {waiting_time_for_2} and travel time is {travel_time_for_2}")

                    bucket_of_waiting_times_a.append(waiting_time_for_1 + (seconds-request_1.timestamp))
                    bucket_of_waiting_times_a.append(waiting_time_for_2 + (seconds-request_2.timestamp))

            elif (lift_1.occupied) and (not lift_2.occupied):
                request_1 = qa.get()

                fastest_lift_for_1 = lift_2

                waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                bucket_of_waiting_times_a.append(waiting_time_for_1 + (seconds-request_1.timestamp))

            elif (not lift_1.occupied) and (lift_2.occupied):
                request_1 = qa.get()

                fastest_lift_for_1 = lift_1

                waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                bucket_of_waiting_times_a.append(waiting_time_for_1 + (seconds-request_1.timestamp))

        # CASE B
        if qb.qsize() != 0:
            if (not lift_1b.occupied) and (not lift_2b.occupied):
                if qb.qsize() == 1:
                    request_1 = qb.get()

                    fastest_lift_for_1 = return_nearest_lift(lift_1b, lift_2b, request_1.start_floor)

                    waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                    # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                    fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                    bucket_of_waiting_times_b.append(waiting_time_for_1 + (seconds-request_1.timestamp))

                elif qb.qsize() >= 2:
                    request_1 = qb.get()
                    request_2 = qb.get()

                    fastest_lift_for_1 = return_nearest_lift(lift_1b, lift_2b, request_1.start_floor)

                    if fastest_lift_for_1 == lift_1b:
                        fastest_lift_for_2 = lift_2b
                    else:
                        fastest_lift_for_2 = lift_1b

                    waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                    waiting_time_for_2 = (abs(fastest_lift_for_2.current_floor - request_2.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    travel_time_for_2 = (abs(request_2.end_floor - request_2.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    total_time_for_2 = waiting_time_for_2 + travel_time_for_2 + DOOR_CLOSING_TIME


                    fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                    fastest_lift_for_2.ferry_passenger(request_2.end_floor, (seconds+total_time_for_2))

                    # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")
                    # print(f"waiting time is {waiting_time_for_2} and travel time is {travel_time_for_2}")

                    bucket_of_waiting_times_b.append(waiting_time_for_1 + (seconds-request_1.timestamp))
                    bucket_of_waiting_times_b.append(waiting_time_for_2 + (seconds-request_2.timestamp))

            elif (lift_1b.occupied) and (not lift_2b.occupied):
                request_1 = qb.get()

                fastest_lift_for_1 = lift_2b

                waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                bucket_of_waiting_times_b.append(waiting_time_for_1 + (seconds-request_1.timestamp))

            elif (not lift_1b.occupied) and (lift_2b.occupied):
                request_1 = qb.get()

                fastest_lift_for_1 = lift_1b

                waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                bucket_of_waiting_times_b.append(waiting_time_for_1 + (seconds-request_1.timestamp))


        lift_1.return_to_default_floor(seconds)
        lift_2.return_to_default_floor(seconds)

        lift_1b.return_to_default_floor(seconds)
        lift_2b.return_to_default_floor(seconds)

        seconds += 1

    return [bucket_of_waiting_times_a,bucket_of_waiting_times_b]
    # print(bucket_of_waiting_times)

def main():

    results = simulate(1,5,10, verbose=True)

    # print(results)
    # plt.hist([results[1],results[7],results[10]],bins=20,alpha=0.5, label=['1','7','10'])
    plt.hist(results, bins=20, alpha=0.5, label=['5','10'])
    plt.title("Simulation for 1,000 minutes") 
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    main()