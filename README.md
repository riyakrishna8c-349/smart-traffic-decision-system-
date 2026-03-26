# smart-traffic-decision-system-

OVERVIEW OF THE PROJECT:
The Smart Traffic Decision System is a simulation-based project developed using Python to improve traffic management at an intersection. Unlike traditional traffic signals that follow fixed timing, this system dynamically adjusts the green signal duration based on the number of vehicles present on each road.

Problem Statement:
Traditional traffic systems use fixed timing signals, which do not consider real-time traffic conditions. This leads to unnecessary waiting, increased fuel consumption, and traffic congestion. The aim of this project is to design a system that adapts signal timing based on traffic.

Solution :
The system dynamically gives priority to the road with the highest traffic, reducing congestion and improving traffic flow.This system reduces unnecessary waiting time and improves overall traffic efficiency.

FEATURE:
* Dynamic signal timing based on number of vehicles
* Identifies busiest road using a simple algorithm
* Simulates real-time traffic updates after each cycle
* Modular design (separate data, logic, and display)
* Easy to understand and extend for future improvements
  
Technologies  used : Python, Functions,Modular Programming,VS Code

Algorithm used:
this project simulates a smart traffic signal system that adjusts green light timing based on the number of vehicles on each road. Unlike traditional fixed-timer signals, this system dynamically prioritizes roads with higher traffic. The goal is to reduce congestion and improve traffic flow using simple programming logic.A greedy approach is used because it makes the best immediate decision by selecting the road with maximum traffic.

Time Complexity: O(n) per cycle
Space Complexity: O(n)

  Instructions for testing :
 1) Python is installed and working
    
 2) Open terminal/command prompt and navigate to the project folder.
Run the program using: python main.py

3 )The program will automatically execute 5 cycles of traffic simulation.
For each cycle, verify:
* Traffic data for all roads is displayed
* The road with the maximum number of cars is selected
* Appropriate green signal time is assigned:
      More than 20 cars → 55 seconds
      11–20 cars → 35 seconds
      10 or less cars → 20 seconds
  
4) Check traffic updates after each cycle:
      Selected road → cars decrease by 10
      Other roads → cars increase by 3
5) Ensure that:
* Car count never becomes negative
* Simulation runs for all 5 cycles
  
6) Final message “Simulation finished” is displayed

sample output :


<img width="302" height="330" alt="image" src="https://github.com/user-attachments/assets/5988124a-10dc-40e9-a7f4-85906529fa19" />

