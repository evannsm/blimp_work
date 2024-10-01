import numpy as np
import matplotlib.pyplot as plt
import csv

class Trajectories:
    def get_circle_horz(x0, y0, z0, psi0, dT, TRACKING_TIME=30, SETTLE_TIME=30):
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))
        R = .8
        tScale = 0.5

        x0 = 1.5
        y0 = 1.0
        z0 = -1.5

        #do it without settle time
        traj_x = np.array([x0 + R * np.cos(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_y = np.array([y0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_z = np.array([(z0)* np.ones(len(tracking_time))]).reshape(-1)
        traj_psi = np.array([0. * np.ones(len(tracking_time))]).reshape(-1)
        traj_x_dot = np.zeros(len(tracking_time))
        traj_y_dot = np.zeros(len(tracking_time))
        traj_z_dot = np.zeros(len(tracking_time))
        traj_psi_dot = np.zeros(len(tracking_time))
        traj_x_ddot = np.zeros(len(tracking_time))
        traj_y_ddot = np.zeros(len(tracking_time))
        traj_z_ddot = np.zeros(len(tracking_time))
        traj_psi_ddot = np.zeros(len(tracking_time))

        # do it with settling too
        traj_x = np.concatenate((traj_x, traj_x[-1] * np.ones(len(settle_time))))
        traj_y = np.concatenate((traj_y, traj_y[-1] * np.ones(len(settle_time))))
        traj_z = np.concatenate((traj_z, traj_z[-1] * np.ones(len(settle_time))))
        traj_psi = np.concatenate((traj_psi, traj_psi[-1] * np.ones(len(settle_time))))
        traj_x_dot = np.concatenate((traj_x_dot, traj_x_dot[-1] * np.ones(len(settle_time))))
        traj_y_dot = np.concatenate((traj_y_dot, traj_y_dot[-1] * np.ones(len(settle_time))))
        traj_z_dot = np.concatenate((traj_z_dot, traj_z_dot[-1] * np.ones(len(settle_time))))
        traj_psi_dot = np.concatenate((traj_psi_dot, traj_psi_dot[-1] * np.ones(len(settle_time))))
        traj_x_ddot = np.concatenate((traj_x_ddot, traj_x_ddot[-1] * np.ones(len(settle_time))))
        traj_y_ddot = np.concatenate((traj_y_ddot, traj_y_ddot[-1] * np.ones(len(settle_time))))
        traj_z_ddot = np.concatenate((traj_z_ddot, traj_z_ddot[-1] * np.ones(len(settle_time))))
        traj_psi_ddot = np.concatenate((traj_psi_ddot, traj_psi_ddot[-1] * np.ones(len(settle_time))))
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)
     

    def get_circle_vert(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))

        R = .8
        tScale = 0.5

        x0 = 1.5
        y0 = 1.0
        z0 = -1.5
        #do it without settle time
        traj_x = np.array([x0 + R * np.cos(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_y = np.array([y0 * np.ones(len(tracking_time))]).reshape(-1)
        traj_z = np.array([z0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_psi = np.array([0. * np.ones(len(tracking_time))]).reshape(-1)
        traj_x_dot = np.zeros(len(tracking_time))
        traj_y_dot = np.zeros(len(tracking_time))
        traj_z_dot = np.zeros(len(tracking_time))
        traj_psi_dot = np.zeros(len(tracking_time))
        traj_x_ddot = np.zeros(len(tracking_time))
        traj_y_ddot = np.zeros(len(tracking_time))
        traj_z_ddot = np.zeros(len(tracking_time))
        traj_psi_ddot = np.zeros(len(tracking_time))

        # do it with settling too
        traj_x = np.concatenate((traj_x, traj_x[-1] * np.ones(len(settle_time))))
        traj_y = np.concatenate((traj_y, traj_y[-1] * np.ones(len(settle_time))))
        traj_z = np.concatenate((traj_z, traj_z[-1] * np.ones(len(settle_time))))
        traj_psi = np.concatenate((traj_psi, traj_psi[-1] * np.ones(len(settle_time))))
        traj_x_dot = np.concatenate((traj_x_dot, traj_x_dot[-1] * np.ones(len(settle_time))))
        traj_y_dot = np.concatenate((traj_y_dot, traj_y_dot[-1] * np.ones(len(settle_time))))
        traj_z_dot = np.concatenate((traj_z_dot, traj_z_dot[-1] * np.ones(len(settle_time))))
        traj_psi_dot = np.concatenate((traj_psi_dot, traj_psi_dot[-1] * np.ones(len(settle_time))))
        traj_x_ddot = np.concatenate((traj_x_ddot, traj_x_ddot[-1] * np.ones(len(settle_time))))
        traj_y_ddot = np.concatenate((traj_y_ddot, traj_y_ddot[-1] * np.ones(len(settle_time))))
        traj_z_ddot = np.concatenate((traj_z_ddot, traj_z_ddot[-1] * np.ones(len(settle_time))))
        traj_psi_ddot = np.concatenate((traj_psi_ddot, traj_psi_ddot[-1] * np.ones(len(settle_time))))
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)
     

    def get_fig8_horz(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))

        R = 0.35
        tScale = 0.5
        x0 = 1.5
        y0 = 1.0
        z0 = -1.5

        #do it without settle time
        traj_x = np.concatenate([x0 + R * np.sin(2*2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_y = np.concatenate([y0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_z = np.array([(z0)* np.ones(len(tracking_time))]).reshape(-1)
        traj_psi = np.array([0. * np.ones(len(tracking_time))]).reshape(-1)
        traj_x_dot = np.zeros(len(tracking_time))
        traj_y_dot = np.zeros(len(tracking_time))
        traj_z_dot = np.zeros(len(tracking_time))
        traj_psi_dot = np.zeros(len(tracking_time))
        traj_x_ddot = np.zeros(len(tracking_time))
        traj_y_ddot = np.zeros(len(tracking_time))
        traj_z_ddot = np.zeros(len(tracking_time))
        traj_psi_ddot = np.zeros(len(tracking_time))

        # do it with settling too
        traj_x = np.concatenate((traj_x, traj_x[-1] * np.ones(len(settle_time))))
        traj_y = np.concatenate((traj_y, traj_y[-1] * np.ones(len(settle_time))))
        traj_z = np.concatenate((traj_z, traj_z[-1] * np.ones(len(settle_time))))
        traj_psi = np.concatenate((traj_psi, traj_psi[-1] * np.ones(len(settle_time))))
        traj_x_dot = np.concatenate((traj_x_dot, traj_x_dot[-1] * np.ones(len(settle_time))))
        traj_y_dot = np.concatenate((traj_y_dot, traj_y_dot[-1] * np.ones(len(settle_time))))
        traj_z_dot = np.concatenate((traj_z_dot, traj_z_dot[-1] * np.ones(len(settle_time))))
        traj_psi_dot = np.concatenate((traj_psi_dot, traj_psi_dot[-1] * np.ones(len(settle_time))))
        traj_x_ddot = np.concatenate((traj_x_ddot, traj_x_ddot[-1] * np.ones(len(settle_time))))
        traj_y_ddot = np.concatenate((traj_y_ddot, traj_y_ddot[-1] * np.ones(len(settle_time))))
        traj_z_ddot = np.concatenate((traj_z_ddot, traj_z_ddot[-1] * np.ones(len(settle_time))))
        traj_psi_ddot = np.concatenate((traj_psi_ddot, traj_psi_ddot[-1] * np.ones(len(settle_time))))
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)

    def get_fig8_vert_short(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))

        R = 0.35
        tScale = 0.5
        x0 = 1.5
        y0 = 1.0
        z0 = -1.5

        #do it without settle time
        traj_x = np.concatenate([x0 * np.ones(len(tracking_time))]).reshape(-1)
        traj_y = np.concatenate([y0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_z = np.concatenate([z0 + R * np.sin(2*2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_psi = np.array([0. * np.ones(len(tracking_time))]).reshape(-1)
        traj_x_dot = np.zeros(len(tracking_time))
        traj_y_dot = np.zeros(len(tracking_time))
        traj_z_dot = np.zeros(len(tracking_time))
        traj_psi_dot = np.zeros(len(tracking_time))
        traj_x_ddot = np.zeros(len(tracking_time))
        traj_y_ddot = np.zeros(len(tracking_time))
        traj_z_ddot = np.zeros(len(tracking_time))
        traj_psi_ddot = np.zeros(len(tracking_time))

        # do it with settling too
        traj_x = np.concatenate((traj_x, traj_x[-1] * np.ones(len(settle_time))))
        traj_y = np.concatenate((traj_y, traj_y[-1] * np.ones(len(settle_time))))
        traj_z = np.concatenate((traj_z, traj_z[-1] * np.ones(len(settle_time))))
        traj_psi = np.concatenate((traj_psi, traj_psi[-1] * np.ones(len(settle_time))))
        traj_x_dot = np.concatenate((traj_x_dot, traj_x_dot[-1] * np.ones(len(settle_time))))
        traj_y_dot = np.concatenate((traj_y_dot, traj_y_dot[-1] * np.ones(len(settle_time))))
        traj_z_dot = np.concatenate((traj_z_dot, traj_z_dot[-1] * np.ones(len(settle_time))))
        traj_psi_dot = np.concatenate((traj_psi_dot, traj_psi_dot[-1] * np.ones(len(settle_time))))
        traj_x_ddot = np.concatenate((traj_x_ddot, traj_x_ddot[-1] * np.ones(len(settle_time))))
        traj_y_ddot = np.concatenate((traj_y_ddot, traj_y_ddot[-1] * np.ones(len(settle_time))))
        traj_z_ddot = np.concatenate((traj_z_ddot, traj_z_ddot[-1] * np.ones(len(settle_time))))
        traj_psi_ddot = np.concatenate((traj_psi_ddot, traj_psi_ddot[-1] * np.ones(len(settle_time))))
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)

    def get_fig8_vert_tall(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))

        R = 0.35
        tScale = 0.5
        x0 = 1.5
        y0 = 1.0
        z0 = -1.5

        traj_x = np.concatenate([x0 * np.ones(len(tracking_time))]).reshape(-1)
        traj_y = np.concatenate([y0 + R * np.sin(2*2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_z = np.concatenate([z0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
        traj_psi = np.array([0. * np.ones(len(tracking_time))]).reshape(-1)
        traj_x_dot = np.zeros(len(tracking_time))
        traj_y_dot = np.zeros(len(tracking_time))
        traj_z_dot = np.zeros(len(tracking_time))
        traj_psi_dot = np.zeros(len(tracking_time))
        traj_x_ddot = np.zeros(len(tracking_time))
        traj_y_ddot = np.zeros(len(tracking_time))
        traj_z_ddot = np.zeros(len(tracking_time))
        traj_psi_ddot = np.zeros(len(tracking_time))

        # do it with settling too
        traj_x = np.concatenate((traj_x, traj_x[-1] * np.ones(len(settle_time))))
        traj_y = np.concatenate((traj_y, traj_y[-1] * np.ones(len(settle_time))))
        traj_z = np.concatenate((traj_z, traj_z[-1] * np.ones(len(settle_time))))
        traj_psi = np.concatenate((traj_psi, traj_psi[-1] * np.ones(len(settle_time))))
        traj_x_dot = np.concatenate((traj_x_dot, traj_x_dot[-1] * np.ones(len(settle_time))))
        traj_y_dot = np.concatenate((traj_y_dot, traj_y_dot[-1] * np.ones(len(settle_time))))
        traj_z_dot = np.concatenate((traj_z_dot, traj_z_dot[-1] * np.ones(len(settle_time))))
        traj_psi_dot = np.concatenate((traj_psi_dot, traj_psi_dot[-1] * np.ones(len(settle_time))))
        traj_x_ddot = np.concatenate((traj_x_ddot, traj_x_ddot[-1] * np.ones(len(settle_time))))
        traj_y_ddot = np.concatenate((traj_y_ddot, traj_y_ddot[-1] * np.ones(len(settle_time))))
        traj_z_ddot = np.concatenate((traj_z_ddot, traj_z_ddot[-1] * np.ones(len(settle_time))))
        traj_psi_ddot = np.concatenate((traj_psi_ddot, traj_psi_ddot[-1] * np.ones(len(settle_time))))
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)





    def get_spiral_stairs(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20, which_one=1):
        # Trajectory definition
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))

        R = 0.35
        tScale = 0.5
        x0 = 1.5
        y0 = 1.0
        z0 = -1.5


        which_one = 4
        if which_one == 1:
            # go up and down in z periodically while staying still in x,y
            traj_x = np.concatenate([x0 * np.ones(len(tracking_time))]).reshape(-1)
            traj_y = np.concatenate([y0 * np.ones(len(tracking_time))]).reshape(-1)
            traj_z = np.concatenate([z0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_psi = np.array([0. * np.ones(len(tracking_time))]).reshape(-1)
                
        elif which_one == 2:
            # go in a vertical spiral
            traj_x = np.concatenate([x0 + R * np.cos(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_y = np.concatenate([y0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_z = np.concatenate([z0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_psi = np.array([0. * np.ones(len(tracking_time))]).reshape(-1)

        elif which_one == 3:
            # go in a circle while spinning
            traj_x = np.concatenate([x0 + R * np.cos(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_y = np.concatenate([y0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_z = np.concatenate([z0 * np.ones(len(tracking_time))]).reshape(-1)
            traj_psi = np.concatenate([2*np.pi*tracking_time/(tScale*TRACKING_TIME)]).reshape(-1)

            
        elif which_one == 4:
            # go in a vertical spiral while spinning
            traj_x = np.concatenate([x0 + R * np.cos(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_y = np.concatenate([y0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_z = np.concatenate([z0 + R * np.sin(2*np.pi*tracking_time/(tScale*TRACKING_TIME))]).reshape(-1)
            traj_psi = np.concatenate([2*np.pi*tracking_time/(tScale*TRACKING_TIME)]).reshape(-1)

        traj_x_dot = np.zeros(len(tracking_time))
        traj_y_dot = np.zeros(len(tracking_time))
        traj_z_dot = np.zeros(len(tracking_time))
        traj_psi_dot = np.zeros(len(tracking_time))
        traj_x_ddot = np.zeros(len(tracking_time))
        traj_y_ddot = np.zeros(len(tracking_time))
        traj_z_ddot = np.zeros(len(tracking_time))
        traj_psi_ddot = np.zeros(len(tracking_time))

        # do it with settling too
        traj_x = np.concatenate((traj_x, traj_x[-1] * np.ones(len(settle_time))))
        traj_y = np.concatenate((traj_y, traj_y[-1] * np.ones(len(settle_time))))
        traj_z = np.concatenate((traj_z, traj_z[-1] * np.ones(len(settle_time))))
        traj_psi = np.concatenate((traj_psi, traj_psi[-1] * np.ones(len(settle_time))))
        traj_x_dot = np.concatenate((traj_x_dot, traj_x_dot[-1] * np.ones(len(settle_time))))
        traj_y_dot = np.concatenate((traj_y_dot, traj_y_dot[-1] * np.ones(len(settle_time))))
        traj_z_dot = np.concatenate((traj_z_dot, traj_z_dot[-1] * np.ones(len(settle_time))))
        traj_psi_dot = np.concatenate((traj_psi_dot, traj_psi_dot[-1] * np.ones(len(settle_time))))
        traj_x_ddot = np.concatenate((traj_x_ddot, traj_x_ddot[-1] * np.ones(len(settle_time))))
        traj_y_ddot = np.concatenate((traj_y_ddot, traj_y_ddot[-1] * np.ones(len(settle_time))))
        traj_z_ddot = np.concatenate((traj_z_ddot, traj_z_ddot[-1] * np.ones(len(settle_time))))
        traj_psi_ddot = np.concatenate((traj_psi_ddot, traj_psi_ddot[-1] * np.ones(len(settle_time))))
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)


    # def get_spiral_stairs(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
    #     # Trajectory definition
    #     tracking_time = np.arange(0, TRACKING_TIME, dT)
    #     settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
    #     time_vec = np.concatenate((tracking_time, settle_time))




    #     traj_x_dot = np.zeros(len(time_vec))
    #     traj_y_dot = np.zeros(len(time_vec))
    #     traj_z_dot = np.zeros(len(time_vec))
    #     traj_psi_dot = np.zeros(len(time_vec))
    #     traj_x_ddot = np.zeros(len(time_vec))
    #     traj_y_ddot = np.zeros(len(time_vec))
    #     traj_z_ddot = np.zeros(len(time_vec))
    #     traj_psi_ddot = np.zeros(len(time_vec))
    #     return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)

    def get_helix(x0, y0, z0, psi0, dT):
        # Time
        TRACKING_TIME = 40
        SETTLE_TIME = 20

        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)

        time_vec = np.concatenate((tracking_time, settle_time))

        At = 0.75
        z_max = -0.5

        # Trajectory definition
        f = 1/TRACKING_TIME
        
        z_slope = z_max / TRACKING_TIME
        
        traj_x = np.concatenate((x0 + (At - At * np.cos(2*np.pi*f*tracking_time)), x0 * np.ones(len(settle_time))))
        traj_y = np.concatenate((y0 + At * np.sin(2*np.pi*f*tracking_time), y0 * np.ones(len(settle_time))))
        traj_z = np.concatenate((z0 + tracking_time * z_slope, (z0 + TRACKING_TIME * z_slope) * np.ones(len(settle_time))))
        traj_psi = np.concatenate((psi0 * np.ones(len(tracking_time)), psi0 * np.ones(len(settle_time))))
        
        traj_x_dot = np.concatenate((2*np.pi*f*At*np.sin(2*np.pi*f*tracking_time), np.zeros(len(settle_time))))
        traj_y_dot = np.concatenate((2*np.pi*f*At*np.cos(2*np.pi*f*tracking_time), np.zeros(len(settle_time))))
        traj_z_dot = np.concatenate((z_slope * np.ones(len(tracking_time)), np.zeros(len(settle_time))))
        traj_psi_dot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))

        traj_x_ddot = np.concatenate((-(2*np.pi*f)**2*At*np.cos(2*np.pi*f*tracking_time), np.zeros(len(settle_time))))
        traj_y_ddot = np.concatenate((-(2*np.pi*f)**2*At*np.sin(2*np.pi*f*tracking_time), np.zeros(len(settle_time))))
        traj_z_ddot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        traj_psi_ddot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)
        
    def get_circle(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))

        R = 0.5
        # w = 0.5
        traj_x = np.concatenate((x0 + R * np.cos(2*np.pi*tracking_time/(0.9*TRACKING_TIME)), (x0 + R * np.cos(2*np.pi*tracking_time[-1])/(0.9*TRACKING_TIME)) * np.ones(len(settle_time))))
        traj_y = np.concatenate((y0 + R * np.sin(2*np.pi*tracking_time/(0.9*TRACKING_TIME)), (y0 + R * np.sin(2*np.pi*tracking_time[-1]/(0.9*TRACKING_TIME)) ) * np.ones(len(settle_time))))
        traj_z = np.concatenate((z0 * np.ones(len(tracking_time)), z0 * np.ones(len(settle_time))))
        traj_psi = np.concatenate((psi0 * np.ones(len(tracking_time)), psi0 * np.ones(len(settle_time))))


        traj_x_dot = np.zeros(len(time_vec))
        traj_y_dot = np.zeros(len(time_vec))
        traj_z_dot = np.zeros(len(time_vec))
        traj_psi_dot = np.zeros(len(time_vec))

        traj_x_ddot = np.zeros(len(time_vec))
        traj_y_ddot = np.zeros(len(time_vec))
        traj_z_ddot = np.zeros(len(time_vec))
        traj_psi_ddot = np.zeros(len(time_vec))
        
        
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)

    def get_circle_yaw(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
        # Trajectory definition
        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)
        time_vec = np.concatenate((tracking_time, settle_time))

        R = 0.5
        # w = 0.5
        traj_x = np.concatenate((x0 + R * np.cos(2*np.pi*tracking_time/(0.9*TRACKING_TIME)), (x0 + np.cos(2*np.pi)) * np.ones(len(settle_time))))
        traj_y = np.concatenate((y0 + R * np.sin(2*np.pi*tracking_time/(0.9*TRACKING_TIME)), (y0 + np.sin(2*np.pi) ) * np.ones(len(settle_time))))
        traj_z = np.concatenate((z0 * np.ones(len(tracking_time)), z0 * np.ones(len(settle_time))))
        traj_psi = np.concatenate((psi0 + R * np.sin(2*np.pi*tracking_time/(0.8*TRACKING_TIME)), (psi0 + np.sin(2*np.pi) ) * np.ones(len(settle_time))))

        traj_x_dot = np.zeros(len(time_vec))
        traj_y_dot = np.zeros(len(time_vec))
        traj_z_dot = np.zeros(len(time_vec))
        traj_psi_dot = np.zeros(len(time_vec))

        traj_x_ddot = np.zeros(len(time_vec))
        traj_y_ddot = np.zeros(len(time_vec))
        traj_z_ddot = np.zeros(len(time_vec))
        traj_psi_ddot = np.zeros(len(time_vec))
        
        
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)
     
    def get_line(x0, y0, z0, psi0, dT, TRACKING_TIME=40, SETTLE_TIME=20):
        # Trajectory definition
        
        m = 0.05

        tracking_time = np.arange(0, TRACKING_TIME, dT)
        settle_time = np.arange(TRACKING_TIME, TRACKING_TIME + SETTLE_TIME + 1, dT)

        time_vec = np.concatenate((tracking_time, settle_time))
        
        traj_x = np.concatenate((x0 + m*tracking_time, (x0 + m*TRACKING_TIME) * np.ones(len(settle_time))))
        traj_y = np.concatenate((y0 * np.ones(len(tracking_time)), y0 * np.ones(len(settle_time))))
        traj_z = np.concatenate((z0 * np.ones(len(tracking_time)), z0 * np.ones(len(settle_time))))
        traj_psi = np.concatenate((psi0 * np.ones(len(tracking_time)), psi0 * np.ones(len(settle_time))))
        
        traj_x_dot = np.concatenate((m * np.ones(len(tracking_time)), np.zeros(len(settle_time))))
        traj_y_dot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        traj_z_dot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        traj_psi_dot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        
        traj_x_ddot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        traj_y_ddot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        traj_z_ddot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        traj_psi_ddot = np.concatenate((np.zeros(len(tracking_time)), np.zeros(len(settle_time))))
        
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)
        
    def get_origin(dT, TRACKING_TIME=40):

        time_vec = np.arange(0, TRACKING_TIME, dT)
        traj_x = 0 * np.ones(len(time_vec))
        traj_y = 0 * np.ones(len(time_vec))
        traj_z = -1.2 * np.ones(len(time_vec))
        traj_psi = 0 * np.ones(len(time_vec))

        traj_x_dot = 0 * np.ones(len(time_vec))
        traj_y_dot = 0 * np.ones(len(time_vec))
        traj_z_dot = 0 * np.ones(len(time_vec))
        traj_psi_dot = 0 * np.ones(len(time_vec))

        traj_x_ddot = 0 * np.ones(len(time_vec))
        traj_y_ddot = 0 * np.ones(len(time_vec))
        traj_z_ddot = 0 * np.ones(len(time_vec))
        traj_psi_ddot = 0 * np.ones(len(time_vec))
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)
     
    def get_triangle(x0, y0, z0, psi0, dT):
        # Trajectory definition
        TRACKING_TIME = 180

        x_distance = 0.5
        y_distance = 0.5
        z_distance = -0.5

        time_vec = np.arange(0, TRACKING_TIME, dT)

        traj_x = np.empty(len(time_vec))
        traj_y = np.empty(len(time_vec))
        traj_z = np.empty(len(time_vec))
        
        traj_x_dot = np.empty(len(time_vec))
        traj_y_dot = np.empty(len(time_vec))
        traj_z_dot = np.empty(len(time_vec))
        
        traj_psi = psi0 * np.ones(len(time_vec))
        traj_psi_dot = np.zeros(len(time_vec))
        
        for i in range(0, int(len(time_vec)/4)):
            traj_x[i] = x0 + (x_distance) / (TRACKING_TIME/4) * time_vec[i]
            traj_y[i] = y0
            
            traj_x_dot[i] = (x_distance) / (TRACKING_TIME/4)
            traj_y_dot[i] = 0
            
            if i < len(time_vec)/8:
                traj_z[i] = z0 + (z_distance) / (TRACKING_TIME/8) * time_vec[i]
                traj_z_dot[i] = (z_distance) / (TRACKING_TIME/8)
            else:
                traj_z[i] = z0 + z_distance - (z_distance) / (TRACKING_TIME/8) * (time_vec[i] - time_vec[int(len(time_vec)/8)])
                traj_z_dot[i] = -(z_distance) / (TRACKING_TIME/8)
            
            
        for i in range(int(len(time_vec)/4) , int(len(time_vec)/2)):
            traj_x[i] = x0 + x_distance
            traj_y[i] = y0 + (y_distance) / (TRACKING_TIME/4) * (time_vec[i] - time_vec[int(len(time_vec)/4)])
            
            traj_x_dot[i] = 0
            traj_y_dot[i] = (y_distance) / (TRACKING_TIME/4)
            
            if i < len(time_vec)*3/8:
                traj_z[i] = z0 + (z_distance) / (TRACKING_TIME/8) * (time_vec[i] - time_vec[int(len(time_vec)/4)])
                traj_z_dot[i] = (z_distance) / (TRACKING_TIME/8)
            else:
                traj_z[i] = z0 + z_distance - (z_distance) / (TRACKING_TIME/8) * (time_vec[i] - time_vec[int(len(time_vec)*3/8)])
                traj_z_dot[i] = -(z_distance) / (TRACKING_TIME/8)
            
        for i in range(int(len(time_vec)/2), int(len(time_vec)*3/4)):
            traj_x[i] = x0 + x_distance - (x_distance) / (TRACKING_TIME/4) * (time_vec[i] - time_vec[int(len(time_vec)/2)])
            traj_y[i] = y0 + y_distance
            
            traj_x_dot[i] = - (x_distance) / (TRACKING_TIME/4)
            traj_y_dot[i] = 0
            
            if i < len(time_vec)*5/8:
                traj_z[i] = z0 + (z_distance) / (TRACKING_TIME/8) * (time_vec[i] - time_vec[int(len(time_vec)/2)])
                traj_z_dot[i] = (z_distance) / (TRACKING_TIME/8)
            else:
                traj_z[i] = z0 + z_distance - (z_distance) / (TRACKING_TIME/8) * (time_vec[i] - time_vec[int(len(time_vec)*5/8)])
                traj_z_dot[i] = -(z_distance) / (TRACKING_TIME/8)
                
        for i in range(int(len(time_vec)*3/4), int(len(time_vec))):
            traj_x[i] = x0
            traj_y[i] = y0 + y_distance - (y_distance) / (TRACKING_TIME/4) * (time_vec[i] - time_vec[int(len(time_vec)*3/4)])
            
            traj_x_dot[i] = 0
            traj_y_dot[i] = -(y_distance) / (TRACKING_TIME/4)
            
            if i < len(time_vec)*7/8:
                traj_z[i] = z0 + (z_distance) / (TRACKING_TIME/8) * (time_vec[i] - time_vec[int(len(time_vec)*3/4)])
                traj_z_dot[i] = (z_distance) / (TRACKING_TIME/8)
            else:
                traj_z[i] = z0 + z_distance - (z_distance) / (TRACKING_TIME/8) * (time_vec[i] - time_vec[int(len(time_vec)*7/8)])
                traj_z_dot[i] = -(z_distance) / (TRACKING_TIME/8)
        
        traj_x_ddot = np.zeros(len(time_vec))
        traj_y_ddot = np.zeros(len(time_vec))
        traj_z_ddot = np.zeros(len(time_vec))
        traj_psi_ddot = np.zeros(len(time_vec))
        
        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_x_ddot, traj_y_ddot, traj_z_ddot, traj_psi_ddot)
        
    def get_generated(x0, y0, z0, psi0, dT=0.05):
        # Load the generated trajectory
        file = np.load('optimal_trajectory.npy')
        states = file['x']
        inputs = file['u']

        traj_x = states[6,:] + x0
        traj_y = states[7,:] + y0
        traj_z = states[8,:] + z0
        traj_psi = states[11,:] + psi0

        traj_x_dot = states[0,:]
        traj_y_dot = states[1,:]
        traj_z_dot = states[2,:]
        traj_psi_dot = states[3,:]

        # Append the inputs at the end.

        traj_u_x = inputs[0,:]
        traj_u_y = inputs[1,:]
        traj_u_z = inputs[2,:]
        traj_u_psi = inputs[3,:]

        return (traj_x, traj_y, traj_z, traj_psi, traj_x_dot, traj_y_dot, traj_z_dot, traj_psi_dot, traj_u_x, traj_u_y, traj_u_z, traj_u_psi)
        