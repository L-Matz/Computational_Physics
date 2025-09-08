import functions as func
import matplotlib.pyplot as plt

vel_vec, pos_vec, C_d, m, dt = func.initial_conditions() #pull initial conditions

pos_hist_x, pos_hist_y = [],[] #define lists to store position history
vel_hist_x, vel_hist_y = [], [] #define lists to store velocity history
time_hist = [] #define list time steps
KE,PE,TE = [],[],[]

#Putting in the initial values for the first time step
pos_hist_x.append(pos_vec["pos_x"])
pos_hist_y.append(pos_vec["pos_y"])
vel_hist_x.append(vel_vec["vel_x"])
vel_hist_y.append(vel_vec["vel_y"])
time_hist.append(0)

KE.append(func.calculate_KE(vel_vec,m))
PE.append(func.calculate_PE(pos_vec,m))
TE.append(KE[-1] + PE[-1])
tcount = 0
while pos_vec["pos_y"] >= 0:
    tcount = tcount + dt
    updated_force = func.update_force(vel_vec, C_d, m) #update force vector
    updated_pos = func.update_pos(pos_vec, vel_vec, dt)           #update position vector
    updated_vel = func.update_vel(updated_force, vel_vec, m, dt)      #update velocity vector

    pos_vec = updated_pos
    vel_vec = updated_vel
    force_vec = updated_force
    
    #Checking if condition has been met before adding it to the data.
    if pos_vec["pos_y"] < 0: break
    
    pos_hist_x.append(pos_vec["pos_x"])
    pos_hist_y.append(pos_vec["pos_y"])
    vel_hist_x.append(vel_vec["vel_x"])
    vel_hist_y.append(vel_vec["vel_y"])
    time_hist.append(tcount)
    
    KE.append(func.calculate_KE(vel_vec,m))
    PE.append(func.calculate_PE(pos_vec,m))
    TE.append(KE[-1] + PE[-1])
    
#Here we can start plotting things for the while loop for any of our variables. 
fig, axs = plt.subplots(ncols = 2,layout='constrained')
axs[0].plot(time_hist,vel_hist_y)
axs[0].set_xlabel('time [s]')
axs[0].set_ylabel("Y-velocity [m/s]")

axs[1].plot(time_hist,vel_hist_x)
axs[1].set_xlabel('time [s]')
axs[1].set_ylabel('X-velocity [m/s]')
#axs[1].legend(loc='upper right')

plt.show()
