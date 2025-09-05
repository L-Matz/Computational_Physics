import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g as grav_const

def initial_conditions():
    pos_x = float(input("Enter the initial x position (m):"))
    pos_y = float(input("Enter the initial y position (m):"))
    vel_x = float(input("Enter the initial x velocity (m/s): "))
    vel_y = float(input("Enter the initial y velocity (m/s): "))

    C_d = float(input("Enter Drag Coefficient: "))
    m = float(input("Enter mass (kg): "))
    dt = float(input("Enter time-step (s): "))

    pos_vec = {"pos_x":pos_x, "pos_y": pos_y}
    vel_vec = {"vel_x":vel_x, "vel_y": vel_y}

    return pos_vec, vel_vec, C_d, m, dt

#pos_vec, vel_vec, C_d, m = initial_conditions() !!!!include this code to query for init conditions
#force_vec = {"force_x":0, "force_y":0}

def force_vector(pos_vec, vel_vec):

    drag_mag = C_d*(vel_vec["vel_x"]**2 + vel_vec["vel_y"]**2)
    grav_mag = m * grav_const

    drag_angle = np.arctan2(vel_vec["vel_y"],vel_vec["vel_x"])
    
    Fd_x = -drag_mag * np.sin(drag_angle)
    Fd_y = -drag_mag * np.cos(drag_angle)
    Fg_y = -grav_mag
    force_vec = { "force_x":(Fd_x), "force_y":(Fg_y + Fd_y)}
    
    return force_vec

def update_vel(vel_vec, force_vec, m, dt):

    accel_x,accel_y = force_vec["force_x"]/m, force_vec["force_y"]/m

    vel_vec["vel_x"], vel_vec["vel_y"] = vel_vec["vel_x"] + accel_x * dt, vel_vec["vel_y"] + accel_y * dt

    return vel_vec

def update_pos(pos_vec, vel_vec, dt):

    pos_vec["pos_x"], pos_vec["pos_y"] = pos_vec["pos_x"] + vel_vec["vel_x"] * dt, pos_vec["pos_y"] + vel_vec["vel_y"] * dt

    return pos_vec
    
#This should be the start of actually using each function and keeping track of the positions and velocities.
vel_x_list = []
vel_y_list = []
pos_x_list = []
pos_y_list = []

#Defining the initial conditons
pos_vec, vel_vec, C_d, m, dt = initial_conditions()
vel_x_list.append(vel_vec["vel_x"])
vel_y_list.append(vel_vec["vel_y"])
pos_x_list.append(pos_vec["pos_x"])
pos_y_list.append(pos_vec["pos_y"])

#Initializing variables for the while loop as to not create infinite loop. Delete it later.
steps = 0
while(pos_vec["pos_y"] >= 0):
    steps += 1
    if steps > 500: break
    #update_pos and update_vel rewrites pos and vel, and we need the old ones for force_vector and update_pos. 
    #Do NOT change the order of these functions. 
    force_vec = force_vector(pos_vec,vel_vec)
    pos_vec = update_pos(pos_vec, vel_vec, dt)
    vel_vec = update_vel(vel_vec, force_vec, m, dt)
    vel_x_list.append(vel_vec["vel_x"])
    vel_y_list.append(vel_vec["vel_y"])
    pos_x_list.append(pos_vec["pos_x"])
    pos_y_list.append(pos_vec["pos_y"])
print("Success! Printing Y values")    
print(vel_y_list)
    


