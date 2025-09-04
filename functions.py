import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g as grav_const

def initial_conditions():

    pos_x, pos_y = input("Enter comma-separated initial position: ")
    vel_x, vel_y = input("Enter comma-separated initial velocity: ")

    C_d = input("Enter Drag Coefficient: ")
    m = input("Enter mass: ")
    dt = input("Enter time-step (s): ")

    pos_vec = {"pos_x":pos_x, "pos_y": pos_y}
    vel_vec = {"vel_x":vel_x, "vel_y": vel_y}

    return pos_vec, vel_vec, C_d, m

#pos_vec, vel_vec, C_d, m = initial_conditions() !!!!include this code to query for init conditions
#force_vec = {"force_x":0, "force_y":0}

def force_vector(pos_vec, vel_vec, force_vec):

    drag_mag = C_d*(vel_vec["vel_x"]**2 + vel_vec["vel_y"]**2)
    grav_mag = m * grav_const

    drag_angle = np.arctan2(vel_vec["vel_y"],vel_vec["vel_y"])
    
    Fd_x = -drag_mag * np.sin(drag_angle)
    Fd_y = -drag_mag * np.cos(drag_angle)
    Fg_y = -grav_mag

    force_vec["force_x"], force_vec["force_y"] = Fd_x, Fg_y + Fd_y
    
    return force_vec

def update_vel(vel_vec, force_vec, m, dt):

    accel_x,accel_y = force_vec["force_x"]/m, force_vec["force_y"]/m

    vel_vec["vel_x"], vel_vec["vel_y"] = vel_vec["vel_x"] + accel_x * dt, vel_vec["vec_y"] + accel_y * dt

    return vel_vec

def update_pos(pos_vec, vel_vec, dt):

    pos_vec["pos_x"], pos_vec["pos_y"] = pos_vec["pos_x"] + vel_vec["vel_x"] * dt, pos_vec["pos_y"] + vel_vec["vel_y"] * dt

    return pos_vec
