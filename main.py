import queue
import statistics

from utils import *
from objects import *


def simulate(lift_1_default, lift_2_default):
    
    lift_1 = Lift(lift_1_default)
    lift_2 = Lift(lift_2_default)
    q = queue.Queue()

    seconds = 0
    bucket_of_waiting_times = []

    while seconds<6000:
        if seconds % 1000 == 0:
            print(f"{seconds} seconds through the current simulation")
            print(f"current queue size is {q.qsize()}")
        # print(f"time now is {seconds}")
        lift_1.update_occupied_state(seconds)
        lift_2.update_occupied_state(seconds)

        add_lift_transaction_based_on_probability(0.0025,seconds,1,2,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,3,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,4,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,5,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,6,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,7,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,8,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,9,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,1,10,q)

        add_lift_transaction_based_on_probability(0.0025,seconds,10,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,9,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,8,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,7,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,6,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,5,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,4,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,3,1,q)
        add_lift_transaction_based_on_probability(0.0025,seconds,2,1,q)


        
        if q.qsize() != 0:
            if (not lift_1.occupied) and (not lift_2.occupied):
                if q.qsize() == 1:
                    request_1 = q.get()

                    fastest_lift_for_1 = return_nearest_lift(lift_1, lift_2, request_1.start_floor)

                    waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                    total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                    # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                    fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                    bucket_of_waiting_times.append(waiting_time_for_1)

                elif q.qsize() >= 2:
                    request_1 = q.get()
                    request_2 = q.get()

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

                    bucket_of_waiting_times.append(waiting_time_for_1)
                    bucket_of_waiting_times.append(waiting_time_for_2)

            elif (lift_1.occupied) and (not lift_2.occupied):
                request_1 = q.get()

                fastest_lift_for_1 = lift_2

                waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                bucket_of_waiting_times.append(waiting_time_for_1)

            elif (not lift_1.occupied) and (lift_2.occupied):
                request_1 = q.get()

                fastest_lift_for_1 = lift_1

                waiting_time_for_1 = (abs(fastest_lift_for_1.current_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                travel_time_for_1 = (abs(request_1.end_floor - request_1.start_floor)*TIME_PER_FLOOR) + DOOR_OPENING_TIME
                total_time_for_1 = waiting_time_for_1 + travel_time_for_1 + DOOR_CLOSING_TIME

                # print(f"waiting time is {waiting_time_for_1} and travel time is {travel_time_for_1}")

                fastest_lift_for_1.ferry_passenger(request_1.end_floor, (seconds+total_time_for_1))
                bucket_of_waiting_times.append(waiting_time_for_1)


        lift_1.return_to_default_floor(seconds)
        lift_2.return_to_default_floor(seconds)

        seconds += 1

    return bucket_of_waiting_times
    # print(bucket_of_waiting_times)

def main():
    results = {}
    for i in range(1,11):
        print(f"current settings are lift1=1, lift2={i}")
        simulation_outcome = simulate(1,i)
        results[i] = [statistics.mean(simulation_outcome),len(simulation_outcome)]
    print(results)

if __name__ == "__main__":
    main()