# lift-optimizer
To demonstrate the optimized default lift settings in my apartment.

## Introduction to Problem
My apartment has 10 floors with 2 lifts. By default, should any lift be left idle for a few minutes, the lifts will automatically position themselves at the 1st and 10th floor respectively. I believe that this is not the optimal setting.

I investigate the optimal default floor settings of the 2 lifts using a Monte Carlo simulation.

## Design of Code
The code has three key components.

A. Queue for Lifts

Every second, there is a given probability p that there will be a passenger requiring a lift to move from floor 1 to floor N, or floor N to floor 1, where 2<N<10 inclusive.

B. Lift Operation

Should the size of the queue be greater than 0, the lift nearest to the passenger will ferry the passenger from the floor. This ferrying process incurs 3 types of time costs: Door Closing, Moving Between Floors, Door Opening.

C. Waiting Times

The Waiting Times determine how efficient the setting is. The Waiting Time is defined as the time interval between joining the Queue, and the lift arriving.

## Results
The lift performs more optimally when placed at floors 5, 6, and 7. This makes intuitive sense, and confirms my hypothesis that the current settings are not optimal. 

Referring to the plot of histograms, we can see that the default settings should be updated to any floor other than 10.

![floor7](/assets/floor7.png)
![floor6](/assets/floor6.png)
![floor5](/assets/floor5.png)

## Further investigation
There is room for further investigation using this code. One could simulate morning peak hours where everyone is leaving for work - this is done by increasing the probability of requiring a lift from floor N to floor 1. You can do so by changing the value of p in the `add_lift_transaction_based_on_probability()` methods called.

The code is flexible and robust enough to do so. Do fork the code and play around with it, and feel free to drop me a message should you need clarifications on how to use it.