import numpy as np
from scipy.constants import g as grav_const

def initial_conditions_horizontal():
    #For horizontal spring:
    dis_x = float(input("Enter initial displacement from the equilibrium position [m]: "))
    vel_x = float(input("Enter initial velocity [m/s]: "))
    m = float(input("Enter mass [kg]: "))
    k = float(input("Enter spring constant (N/m): "))
    tmax = float(input("Enter the amount of time for simulation to last [s]: "))
    dt = float(input("Enter time-step (s): "))
    dis_vec = {"dis_x":dis_x, "dis_y":0}
    vel_vec = {"vel_x":vel_x, "vel_y":0}
    
    return vel_vec, dis_vec, k, m, tmax, dt
    
def initial_conditions_vertical():
    #For vertical spring:
    dis_y = float(input("Enter initial displacement from the equilibrium position [m]: "))
    vel_y = float(input("Enter initial velocity [m/s]: "))
    m = float(input("Enter mass [kg]: "))
    dt = float(input("Enter time-step (s): "))
    k = float(input("Enter spring constant (N/m): "))
    dis_vec = {"dis_x":0, "dis_y":dis_y}
    vel_vec = {"vel_x":0, "vel_y":vel_y}
    
    return vel_vec, dis_vec, k, m, dt

def update_force_gravity(dis_vec,vel_vec,k,m):
    grav_mag = m * grav_const

    Fs_x = -k * dis_vec["dis_x"]
    Fs_y = -k * dis_vec["dis_y"]
    Fg_y = -grav_mag
    force_vec = {"force_x":float(Fs_x), "force_y":float(Fg_y + Fs_y)}
    
    return force_vec

def update_force_no_gravity(dis_vec,k):
    Fs_x = -k * dis_vec["dis_x"]
    Fs_y = -k * dis_vec["dis_y"]
    force_vec = {"force_x":float(Fs_x), "force_y":float(Fs_y)}
    
    return force_vec
    
    #These next are euler's method of getting vel and x. 
    #Due to the specifics of this problem, you can get explicit or semi-implicit depending on the input of the velocity in update_pos_euler.
def update_vel_euler(force_vec,vel_vec,m,dt):
    accel_x,accel_y = force_vec["force_x"]/m, force_vec["force_y"]/m

    nvel_vec = {"vel_x":0,"vel_y":0}
    nvel_vec["vel_x"], nvel_vec["vel_y"] = vel_vec["vel_x"] + accel_x * dt, vel_vec["vel_y"] + accel_y * dt

    return nvel_vec
    

def update_dis_euler(dis_vec,vel_vec,dt):
    ndis_vec = {"dis_x":0,"dis_y":0}
    ndis_vec["dis_x"], ndis_vec["dis_y"] = dis_vec["dis_x"] + vel_vec["vel_x"] * dt, dis_vec["dis_y"] + vel_vec["vel_y"] * dt

    return ndis_vec

    #These two will be for the second order method
    #This first one is meant to take in the explicit and implicit results for the velocity: the velocity of the current step and the next step.
def update_vel_secondorder(vel_vec,dis_vec,k,m,dt):
    mid_vec = {"vel_x":0,"vel_y":0}
    mid_vec['vel_x'] = vel_vec['vel_x'] - (k/m) * dis_vec['dis_x'] * dt - (k/m) * dt * dt * 0.5 * vel_vec['vel_x'] + (k/m) * (k/m) * dt * dt * dt * 0.5 * dis_vec['dis_x']
    mid_vec['vel_y'] = vel_vec['vel_y'] - (k/m) * dis_vec['dis_y'] * dt - (k/m) * dt * dt * 0.5 * vel_vec['vel_y'] + (k/m) * (k/m) * dt * dt * dt * 0.5 * dis_vec['dis_y']
    return mid_vec

def calculate_KE(vel_vec,m):
    v_square = (vel_vec["vel_x"]**2 + vel_vec["vel_y"]**2)
    #v_square = vel_vec["vel_x"]**2
    return (1/2)*m*v_square

def calculate_PE(dis_vec,m,k):
    potential_grav = m*grav_const*dis_vec["dis_y"]
    potential_spring = 0.5 * k * (dis_vec["dis_x"]**2 + dis_vec["dis_y"]**2)
    potential = potential_grav + potential_spring
    #potential = 0.5 * k * (dis_vec["dis_x"]**2)
    return potential

