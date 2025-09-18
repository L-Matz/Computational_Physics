#This is a file for running the main loop, so I will need to initial variables, and call in the python functions in functions.py. 
import functions as func
import matplotlib.pyplot as plt
import numpy as np

#choice = input("Did you want to simulate a vertical spring with Gravity? A No will use the default Horizontal spring simulation. (y/n): ").startswith('y')
choice = False
PE_euler, PE_symplectic, PE_secondorder, KE_euler, KE_symplectic, KE_secondorder, TE_euler, TE_symplectic, TE_secondorder = [], [], [], [], [], [], [], [], []
time_list = []
time_list.append(0)

if (choice == True):
    print("Vertical Spring simulation")
    vel_vec, dis_vec, k, m, dt = func.initial_conditions_vertical()
    #store data points for y, vy, etc...
else:
    print("Horizontal Spring simulation")
    #Initial conditions
    vel_vec, dis_vec, k, m, tmax, dt = func.initial_conditions_horizontal()
    
    #Store data points for x position and velocity:
    dis_x_euler, vel_x_euler, dis_x_symplectic, vel_x_symplectic, dis_x_secondorder, vel_x_secondorder = [], [], [], [], [], []
    
    #Initialize the first values
    dis_x_euler.append(dis_vec["dis_x"])
    vel_x_euler.append(vel_vec["vel_x"])
    vel_x_symplectic.append(vel_vec["vel_x"])
    dis_x_symplectic.append(dis_vec["dis_x"])
    vel_x_secondorder.append(vel_vec["vel_x"])
    dis_x_secondorder.append(dis_vec["dis_x"])
    
    #Gets initial energy values for each method:
    KE_euler.append(func.calculate_KE(vel_vec,m))
    KE_symplectic.append(func.calculate_KE(vel_vec,m))
    KE_secondorder.append(func.calculate_KE(vel_vec,m))
    PE_euler.append(func.calculate_PE(dis_vec,m,k))
    PE_symplectic.append(func.calculate_PE(dis_vec,m,k))
    PE_secondorder.append(func.calculate_PE(dis_vec,m,k))
    TE_euler.append(KE_euler[-1] + PE_euler[-1])
    TE_symplectic.append(KE_symplectic[-1] + PE_symplectic[-1])
    TE_secondorder.append(KE_secondorder[-1] + PE_secondorder[-1])
    
    #Making the previous step variables for each method before the loop, so it works as intended.
    euler_past_displacement = dis_vec
    euler_past_velocity =  vel_vec
    symplectic_past_displacement = dis_vec
    symplectic_past_velocity = vel_vec
    secondorder_past_displacement = dis_vec
    secondorder_past_velocity = vel_vec
    countmax = tmax / dt
    count = 0
    while(count < countmax):
        time_list.append(time_list[-1] + dt)
        #Euler method:
        euler_update_force = func.update_force_no_gravity(euler_past_displacement,euler_past_velocity,k,m)
        euler_update_velocity = func.update_vel_euler(euler_update_force,euler_past_velocity,m,dt)
        euler_update_displacement = func.update_dis_euler(euler_past_displacement,euler_past_velocity,dt)
        
        dis_x_euler.append(euler_update_displacement["dis_x"])
        vel_x_euler.append(euler_update_velocity["vel_x"])
        KE_euler.append(func.calculate_KE(euler_update_velocity,m))
        PE_euler.append(func.calculate_PE(euler_update_displacement,m,k))
        TE_euler.append(KE_euler[-1] + PE_euler[-1])
        
        euler_past_velocity = euler_update_velocity
        euler_past_displacement = euler_update_displacement
        
        #Symplectic method:
        symplectic_update_force = func.update_force_no_gravity(symplectic_past_displacement,symplectic_past_velocity,k,m)
        symplectic_update_velocity = func.update_vel_euler(symplectic_update_force,symplectic_past_velocity,m,dt)
        symplectic_update_displacement = func.update_dis_euler(symplectic_past_displacement,symplectic_update_velocity,dt)
        
        dis_x_symplectic.append(symplectic_update_displacement["dis_x"])
        vel_x_symplectic.append(symplectic_update_velocity["vel_x"])
        KE_symplectic.append(func.calculate_KE(symplectic_update_velocity,m))
        PE_symplectic.append(func.calculate_PE(symplectic_update_displacement,m,k))
        TE_symplectic.append(KE_symplectic[-1] + PE_symplectic[-1])
        
        symplectic_past_velocity = symplectic_update_velocity
        symplectic_past_displacement = symplectic_update_displacement
        
        #Put second order method here
        secondorder_update_force = func.update_force_no_gravity(secondorder_past_displacement,secondorder_past_velocity,k,m)
        secondorder_update_velocity = func.update_vel_euler(secondorder_update_force,secondorder_past_velocity,m,dt)
        secondorder_update_velocity = func.update_vel_trapezoid(secondorder_past_velocity,secondorder_update_velocity)
        secondorder_update_displacement = func.update_dis_euler(secondorder_past_displacement,secondorder_update_velocity,dt)
        
        dis_x_secondorder.append(secondorder_update_displacement["dis_x"])
        vel_x_secondorder.append(secondorder_update_velocity["vel_x"])
        KE_secondorder.append(func.calculate_KE(secondorder_update_velocity,m))
        PE_secondorder.append(func.calculate_PE(secondorder_update_displacement,m,k))
        TE_secondorder.append(KE_secondorder[-1] + PE_secondorder[-1])
        
        secondorder_past_velocity = secondorder_update_velocity
        secondorder_past_displacement = secondorder_update_displacement
        
        
        #Adjust counter
        count = count + 1
#Make plots

fig, axs = plt.subplots(ncols = 2,layout='constrained')
axs[0].plot(time_list,dis_x_euler,label='displacement')
axs[0].set_xlabel('time [s]')
axs[0].set_ylabel("X-displacement [m]")


axs[1].plot(time_list,TE_euler,label='energy')
axs[1].set_xlabel('time [s]')
axs[1].set_ylabel('Energy [J]')
plt.savefig("graphs_displacement_energy_euler.pdf")
plt.close()

fig, axs = plt.subplots(ncols = 2,layout='constrained')
axs[0].plot(time_list,dis_x_symplectic,label='displacement')
axs[0].set_xlabel('time [s]')
axs[0].set_ylabel("X-displacement [m]")

axs[1].plot(time_list,TE_symplectic,label='energy')
axs[1].set_xlabel('time [s]')
axs[1].set_ylabel('Energy [J]')
plt.savefig("graphs_displacement_energy_symplectic.pdf")
plt.close()

fig, axs = plt.subplots(ncols = 2,layout='constrained')
axs[0].plot(time_list,dis_x_secondorder,label='displacement')
axs[0].set_xlabel('time [s]')
axs[0].set_ylabel("X-displacement [m]")

axs[1].plot(time_list,TE_secondorder,label='energy')
axs[1].set_xlabel('time [s]')
axs[1].set_ylabel('Energy [J]')
plt.savefig("graphs_displacement_energy_secondorder.pdf")
plt.close()

    
    


