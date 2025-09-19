#This is a file for running the main loop, so I will need to initial variables, and call in the python functions in functions.py. 
import functions as func
import matplotlib.pyplot as plt
import numpy as np

time_list = []
time_list.append(0)
PE, KE, TE = [], [], []

vel_now_vec, dis_now_vec, k, m, tmax, dt = func.initial_conditions_horizontal()
dis_x_euler, vel_x_euler = [], []
#Recording initial conditions
dis_x_euler.append(dis_now_vec["dis_x"])
vel_x_euler.append(vel_now_vec["vel_x"])
KE.append(func.calculate_KE(vel_now_vec,m))
PE.append(func.calculate_PE(dis_now_vec,m,k))
TE.append(KE[-1] + PE[-1])

countmax = tmax / dt
count = 0
while(count < countmax):
    time_list.append(time_list[-1] + dt)
    force_now = func.update_force_no_gravity(dis_now_vec,k)
    vel_next_vec = func.update_vel_euler(force_now,vel_now_vec,m,dt)
    dis_next_vec = func.update_dis_euler(dis_now_vec,vel_now_vec,dt)
    
    dis_x_euler.append(dis_next_vec["dis_x"])
    vel_x_euler.append(vel_next_vec["vel_x"])
    KE.append(func.calculate_KE(vel_next_vec,m))
    PE.append(func.calculate_PE(dis_next_vec,m,k))
    TE.append(KE[-1] + PE[-1])
    
    dis_now_vec = dis_next_vec
    vel_now_vec = vel_next_vec
        
    count = count + 1
#Making graph
fig, axs = plt.subplots(ncols = 2,layout='constrained')
axs[0].plot(time_list,dis_x_euler,label='displacement')
axs[0].set_xlabel('time [s]')
axs[0].set_ylabel("X-displacement [m]")


axs[1].plot(time_list,TE,label='energy')
axs[1].set_xlabel('time [s]')
axs[1].set_ylabel('Energy [J]')
plt.savefig("graphs_displacement_energy_euler_{tmax}_{dt}.pdf")
plt.close()
