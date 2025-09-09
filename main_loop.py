import functions as func
import matplotlib.pyplot as plt
import numpy as np

vel_vec, pos_vec, C_d, m, dt = func.initial_conditions() #pull initial conditions
vel_x_init,vel_y_init = vel_vec["vel_x"], vel_vec["vel_y"]
x_init, y_init = pos_vec["pos_x"], pos_vec["pos_y"]
pos_hist_x, pos_hist_y = [],[] #define lists to store position history
vel_hist_x, vel_hist_y = [], [] #define lists to store velocity history
KE,PE,TE = [],[],[]
time_list = []
time_list.append(0)
#Putting in the initial values for the first time step
pos_hist_x.append(pos_vec["pos_x"])
pos_hist_y.append(pos_vec["pos_y"])
vel_hist_x.append(vel_vec["vel_x"])
vel_hist_y.append(vel_vec["vel_y"])

#For the case of no drag. Find the analytic total energy.
analytic_TE = func.calculate_KE(vel_vec,m) + func.calculate_PE(pos_vec,m)

KE.append(func.calculate_KE(vel_vec,m))
PE.append(func.calculate_PE(pos_vec,m))
TE.append(KE[-1] + PE[-1])

while pos_vec["pos_y"] >= 0:
    time_list.append(time_list[-1] + dt)
    updated_force = func.update_force(vel_vec, C_d, m) #update force vector
    updated_pos = func.update_pos(pos_vec, vel_vec, dt)           #update position vector
    updated_vel = func.update_vel(updated_force, vel_vec, m, dt)      #update velocity vector

    pos_vec = updated_pos
    vel_vec = updated_vel
    
    pos_hist_x.append(pos_vec["pos_x"]) #append updated values to history lists for plotting
    pos_hist_y.append(pos_vec["pos_y"])
    vel_hist_x.append(vel_vec["vel_x"])
    vel_hist_y.append(vel_vec["vel_y"])
    
    KE.append(func.calculate_KE(vel_vec,m))
    PE.append(func.calculate_PE(pos_vec,m))
    TE.append(KE[-1] + PE[-1])
    

#We want to save our time, position_x, position_y
out_dict = {"time":time_list ,"pos_hist_x":pos_hist_x ,"pos_hist_y":pos_hist_y}

analytic_x, analytic_y, analytic_vx, analytic_vy = func.analytic_function(vel_y_init,vel_x_init, time_list, y_init, x_init)

#Here we can start plotting things for the while loop for any of our variables. 
fig, axs = plt.subplots(ncols = 2,layout='constrained')
axs[0].plot(pos_hist_x,pos_hist_y,label='Simulated')
axs[0].plot(analytic_x,analytic_y,label='Analytic')
axs[0].set_xlabel('X-position [m]')
axs[0].set_ylabel("Y-position [m]")
axs[0].legend(loc='upper right')

axs[1].plot(pos_hist_x,KE,label='KE')
axs[1].plot(pos_hist_x,PE,label='PE')
axs[1].plot(pos_hist_x,TE,label='TE')
axs[1].set_xlabel('X-position [m]')
axs[1].set_ylabel('Energy [J]')
axs[1].legend(loc='upper right')

dt_lab = str(dt).split(".")[0] + "d"  + str(dt).split(".")[1]
plt.savefig(f"output_ dt_{dt_lab}.png",dpi=300)

file = open(f"output_file_dt_{dt_lab}.txt","w")
file.write("time pos_x pos_y \n")
for i in range(len(out_dict["time"])):
    file.write(f"{out_dict["time"][i]} {out_dict["pos_hist_x"][i]} {out_dict["pos_hist_y"][i]} \n")
