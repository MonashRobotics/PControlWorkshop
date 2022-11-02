import numpy as np
from matplotlib import pyplot as plt
from IPython import display

class SimpleRobot:

    def __init__(self,dt=0.1):

        self.x = 0
        self.dt = dt

    def drive(self,v):

        self.x = self.x + v*self.dt

    def plot(self,ax,color='C0'):

        ax.cla()

        ax.add_patch(plt.Rectangle((self.x,9.5),2,1,color=color))
        ax.plot(self.x,10.5,'ko',markersize=20)
        ax.plot(self.x,9.5,'ko',markersize=20)
        ax.plot(self.x+1.75,10,'ko',markersize=10)
        ax.set_xlim(0,10)
        ax.set_ylim(8,12)
        ax.set_xlabel('Distance')
        ax.grid('True')

        display.clear_output(wait=True)
        display.display(plt.gcf())
