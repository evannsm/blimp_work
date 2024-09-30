import gurobipy as gp
from gurobipy import GRB
import numpy as np
import control
from . utilities import *
from . CtrlWardi import CtrlWardi
from . Trajectories import Trajectories
import math
import sys

class HardwareWardiFig8VertTall(CtrlWardi):

    def __init__(self, dT, skip_derivatives=True):
        super().__init__(dT)
        
    def init_sim(self, sim):
        x0 = sim.get_var('x')
        y0 = sim.get_var('y')
        z0 = sim.get_var('z')
        psi0 = sim.get_var('psi')
        
        trajectory = Trajectories.get_fig8_vert_tall(x0, y0, z0, psi0, self.dT)
        self.init_trajectory(trajectory)
        
        self.is_initialized = True

