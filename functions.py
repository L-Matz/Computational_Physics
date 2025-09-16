import numpy as np
from scipy.constants import g as grav_const

def initial_conditions_horizontal():
    #For horizontal spring:
    dis_x = float(input("Enter initial displacement from the equilibrium position [m]: "))
    vel_x = float(input("Enter initial velocity [m/s]: "))
    m = float(input("Enter mass [kg]: "))
    dt = float(input("Enter time-step (s): "))
    k = float(input("Enter spring constant (N/m): "))
    dis_vec = {"dis_x":dis_x, "dis_y":0}
    vel_vec = {"vel_x":vel_x, "vel_y":0}
    
    return vel_vec, dis_vec, k, m, dt
    
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

def update_force(dis_vec,dis_vec,k,m):
    grav_mag = m * grav_const

    Fs_x = -k * dis_vec["dis_x"]
    Fs_y = -k * dis_vec["dis_y"]
    Fg_y = -grav_mag
    force_vec = {"force_x":float(Fs_x), "force_y":float(Fg_y + Fs_y)}
    
    return force_vec

def update_vel_explicit(force_vec,vel_vec,m,dt):
    accel_x,accel_y = force_vec["force_x"]/m, force_vec["force_y"]/m

    vel_vec["vel_x"], vel_vec["vel_y"] = vel_vec["vel_x"] + accel_x * dt, vel_vec["vel_y"] + accel_y * dt

    return vel_vec

def update_pos_explicit(pos_vec,vel_vec,dt):
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
    x_vel = vel_x_init - grav_const * np.array(t)
    return x_pos,y_pos, x_vel, y_vel

def calculate_std(anal_x, anal_y, anal_vx, anal_vy, sim_x, sim_y, sim_vx, sim_vy, m):
    diffx = np.array(anal_x) - np.array(sim_x)
    diffsquarex = np.array(anal_x)**2 - np.array(sim_x)**2
    stdx = np.sqrt(np.absolute(diffsquarex - diffx**2))
    diffy = np.array(anal_y) - np.array(sim_y)
    diffsquarey = np.array(anal_y)**2 - np.array(sim_y)**2
    stdy = np.sqrt(np.absolute(diffsquarey - diffy**2))
    sim_TE = 0.5*m*(np.array(sim_vx)**2 + np.array(sim_vy)**2) + grav_const*m*np.array(sim_y) 
    anal_TE = 0.5*m*(np.array(anal_vx[0])**2 + np.array(anal_vy[0])**2) + grav_const*m*np.array(anal_y[0])
    diffTE = sim_TE - anal_TE
    diffsquareTE = sim_TE**2 - anal_TE**2
    stdTE = np.sqrt(np.absolute(diffsquareTE - diffTE**2))
    
    return stdx, stdy, stdTE
    
