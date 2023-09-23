#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fcfs(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    return waiting_time, turnaround_time

def sjf(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    burst_time_copy = burst_time.copy()
    time = 0

    while True:
        min_burst = float('inf')
        min_idx = -1
        flag = False

        for i in range(n):
            if arrival_time[i] <= time and burst_time_copy[i] < min_burst and burst_time_copy[i] > 0:
                min_burst = burst_time_copy[i]
                min_idx = i
                flag = True

        if not flag:
            break

        burst_time_copy[min_idx] = 0
        waiting_time[min_idx] = time - arrival_time[min_idx]
        turnaround_time[min_idx] = waiting_time[min_idx] + burst_time[min_idx]
        time += burst_time[min_idx]

    return waiting_time, turnaround_time

def ps(processes, arrival_time, burst_time, priority):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    burst_time_copy = burst_time.copy()
    time = 0

    while True:
        highest_priority = -1
        min_idx = -1
        flag = False

        for i in range(n):
            if arrival_time[i] <= time and priority[i] > highest_priority and burst_time_copy[i] > 0:
                highest_priority = priority[i]
                min_idx = i
                flag = True

        if not flag:
            break

        burst_time_copy[min_idx] = 0
        waiting_time[min_idx] = time - arrival_time[min_idx]
        turnaround_time[min_idx] = waiting_time[min_idx] + burst_time[min_idx]
        time += burst_time[min_idx]

    return waiting_time, turnaround_time

def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = burst_time.copy()
    time = 0

    while True:
        done = True

        for i in range(n):
            if arrival_time[i] <= time:
                if remaining_time[i] > 0:
                    done = False
                    if remaining_time[i] > time_quantum:
                        time += time_quantum
                        remaining_time[i] -= time_quantum
                    else:
                        time += remaining_time[i]
                        waiting_time[i] = time - arrival_time[i] - burst_time[i]
                        remaining_time[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    return waiting_time, turnaround_time

# Input data
processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 4, 5, 6]
burst_time = [24, 3, 3, 12]
priority = [3, 1, 4, 2]
time_quantum = 4

# FCFS
fcfs_waiting_time, fcfs_turnaround_time = fcfs(processes, arrival_time, burst_time)

# SJF
sjf_waiting_time, sjf_turnaround_time = sjf(processes, arrival_time, burst_time)

# Priority Scheduling
ps_waiting_time, ps_turnaround_time = ps(processes, arrival_time, burst_time, priority)

# Round Robin
rr_waiting_time, rr_turnaround_time = round_robin(processes, arrival_time, burst_time, time_quantum)

# Calculate average waiting time and average turnaround time for each algorithm
def calculate_average(times):
    return sum(times) / len(times)

fcfs_avg_waiting_time = calculate_average(fcfs_waiting_time)
fcfs_avg_turnaround_time = calculate_average(fcfs_turnaround_time)

sjf_avg_waiting_time = calculate_average(sjf_waiting_time)
sjf_avg_turnaround_time = calculate_average(sjf_turnaround_time)

ps_avg_waiting_time = calculate_average(ps_waiting_time)
ps_avg_turnaround_time = calculate_average(ps_turnaround_time)

rr_avg_waiting_time = calculate_average(rr_waiting_time)
rr_avg_turnaround_time = calculate_average(rr_turnaround_time)

# Print the results

print("FCFS Average Waiting Time:", fcfs_avg_waiting_time)
print("FCFS Average Turnaround Time:", fcfs_avg_turnaround_time)


print("SJF Average Waiting Time:", sjf_avg_waiting_time)
print("SJF Average Turnaround Time:", sjf_avg_turnaround_time)


print("Priority Scheduling Average Waiting Time:", ps_avg_waiting_time)
print("Priority Scheduling Average Turnaround Time:", ps_avg_turnaround_time)


print("Round Robin Average Waiting Time:", rr_avg_waiting_time)
print("Round Robin Average Turnaround Time:", rr_avg_turnaround_time)


# In[ ]:




