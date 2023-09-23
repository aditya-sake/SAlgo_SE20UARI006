#!/usr/bin/env python
# coding: utf-8

# In[4]:


import heapq
from datetime import datetime

def fcfs(patients):
    patients.sort(key=lambda x: x[1])  # Sort by arrival time
    order = [p[0] for p in patients]
    return order

def sjf(patients):
    patients.sort(key=lambda x: (x[2], x[1]))  # Sort by treatment time and arrival time
    order = [p[0] for p in patients]
    return order

def ps(patients):
    patients.sort(key=lambda x: (-x[3], x[1]))  # Sort by urgency level (reverse order) and arrival time
    order = [p[0] for p in patients]
    return order

def round_robin(patients, time_quantum):
    patients.sort(key=lambda x: datetime.strptime(x[1], "%M:%S").minute)  # Sort by arrival time
    queue = patients.copy()
    order = []
    time = 0

    while queue:
        patient = queue.pop(0)
        patient_id, arrival_time, treatment_time, urgency_level = patient

        if treatment_time <= time_quantum:
            order.append(patient_id)
            time += treatment_time
        else:
            order.append(patient_id)
            time += time_quantum
            patient = (patient_id, arrival_time, treatment_time - time_quantum, urgency_level)
            queue.append(patient)

    return order

# Updated patient data (Patient, arrival time, treatment time, urgency level)
patients = [
    ('A', '00:00', 30, 3),
    ('B', '00:10', 20, 5),
    ('C', '00:15', 40, 2),
    ('D', '00:20', 15, 4),
]

# Time quantum for Round Robin
time_quantum = 5

# FCFS
fcfs_order = fcfs(patients)
print("FCFS Order:", fcfs_order)

# SJF
sjf_order = sjf(patients)
print("SJF Order:", sjf_order)

# Priority Scheduling (PS)
ps_order = ps(patients)
print("Priority Scheduling Order:", ps_order)

# Round Robin (RR)
rr_order = round_robin(patients, time_quantum)
print("Round Robin Order:", rr_order)


# In[ ]:




