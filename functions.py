import numpy as np
from scipy.constants import g as grav_const


def initial_conditions():
    pos_x, pos_y = input("Enter comma-separated initial position [m]: ").split(",")
    use_angle = input("Use launch angle? (y/n):  ").startswith('y')
    if use_angle==True:
        angle =  float(input("Enter launch angle (deg): ")) * (np.pi/180)
        vel_mag = float(input("Magnitude of initial velocity [m/s]: "))
        vel_x, vel_y = vel_mag*np.cos(angle), vel_mag*np.sin(angle)
    else:
        vel_x, vel_y = input("Enter comma-separated initial velocity [m/s]: ").split(",")

    C_d = float(input("Enter Drag Coefficient: "))
    m = float(input("Enter mass [kg]: "))
    dt = float(input("Enter time-step (s): "))

    pos_vec = {"pos_x":float(pos_x), "pos_y": float(pos_y)}
    vel_vec = {"vel_x":float(vel_x), "vel_y": float(vel_y)}
    
    return vel_vec, pos_vec, C_d, m, dt

def update_force(vel_vec,C_d,m):
    drag_mag = C_d*(vel_vec["vel_x"]**2 + vel_vec["vel_y"]**2)
    grav_mag = m * grav_const

    drag_angle = np.arctan2(vel_vec["vel_y"],vel_vec["vel_x"])
    
    Fd_x = -drag_mag * np.cos(drag_angle)
    Fd_y = -drag_mag * np.sin(drag_angle)
    Fg_y = -grav_mag
    force_vec = {"force_x":float(Fd_x), "force_y":float(Fg_y + Fd_y)}
    
    return force_vec

def update_vel(force_vec,vel_vec,m,dt):
    accel_x,accel_y = force_vec["force_x"]/m, force_vec["force_y"]/m

    vel_vec["vel_x"], vel_vec["vel_y"] = vel_vec["vel_x"] + accel_x * dt, vel_vec["vel_y"] + accel_y * dt

    return vel_vec

def update_pos(pos_vec,vel_vec,dt):
    pos_vec["pos_x"], pos_vec["pos_y"] = pos_vec["pos_x"] + vel_vec["vel_x"] * dt, pos_vec["pos_y"] + vel_vec["vel_y"] * dt

    return pos_vec

def calculate_KE(vel_vec,m):
    v_square = (vel_vec["vel_x"]**2 + vel_vec["vel_y"]**2)
    return (1/2)*m*v_square

def calculate_PE(pos_vec,m):
    return m*grav_const*pos_vec["pos_y"]

def analytic_function(vel_y_init,vel_x_init,t,y_init,x_init):
    y_pos = y_init + vel_y_init * np.array(t) - 1/2 * grav_const * np.array(t) **2
    x_pos = x_init +  vel_x_init * np.array(t)
    y_vel = vel_y_init - grav_const * np.array(t)
    x_vel = vel_x_init - grav_cosst * np.array(t)
    return x_pos,y_pos, x_vel, y_vel
