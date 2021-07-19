DOOR_OPENING_TIME = 3
DOOR_CLOSING_TIME = 3
TIME_PER_FLOOR = 2


class Lift:
    def __init__(self, default_floor, occupied=False, last_used=0):
        self.occupied = occupied
        self.last_used = last_used
        self.default_floor = default_floor
        self.current_floor = default_floor

    def ferry_passenger(self, end_floor, end_time):
        # print(f"Lift currently at {self.current_floor}. Lift ferrying passenger to floor {end_floor} and will finish at {end_time}")
        self.occupied = True
        self.last_used = end_time
        self.current_floor = end_floor


    def update_occupied_state(self, current_time):
        if self.last_used == current_time:
            # print("Lift changing state")
            self.occupied = False


    def return_to_default_floor(self, current_time):
        if (self.current_floor != self.default_floor) and (not self.occupied) and (current_time - self.last_used) > 10:
            # print("Lift returning home")
            self.occupied = True
            self.last_used = current_time + DOOR_CLOSING_TIME + abs(self.current_floor - self.default_floor)*TIME_PER_FLOOR


class LiftRequest:
    def __init__(self, timestamp, start_floor, end_floor):
        self.timestamp = timestamp
        self.start_floor = start_floor
        self.end_floor = end_floor

