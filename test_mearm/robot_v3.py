#import required libraries
from visual import *
import numpy as np

#define dimensions for the MeArm
l1 = 8.5 #length of link 1 in cm
l2 = 8.5 #length of link 2 in cm

#Create virtual environment:
scene = display(title='Robot movements', width=600, height=600, center=(8,4,0)) #set up the scene
#To improve clarity, create a set of x, y and z axis
x_axis= arrow(pos=(0,0,0), axis=(15,0,0), shaftwidth=0.1, headwidth=0.3)
y_axis= arrow(pos=(0,0,0), axis=(0,15,0), shaftwidth=0.1, headwidth=0.3)
pos_z_axis= arrow(pos=(0,0,0), axis=(0,0,-15), shaftwidth=0.1, headwidth=0.3)
neg_z_axis= arrow(pos=(0,0,0), axis=(0,0,15), shaftwidth=0.1, headwidth=0.3)

#Indicators for the target, link 1 and link 2 respectively
indicator = arrow(pos=(0,0,0), axis=(10,10,0), shaftwidth=0.2, headwidth=0.3, color=color.yellow)
l1_ind = arrow(pos=(0,0,0), axis=(2.65,7.64,0), shaftwidth=0.2, headwidth=0.3, color=color.red)
l2_ind = arrow(pos=(2.65,7.64,0), axis=(7.3,2.3,0), shaftwidth=0.2, headwidth=0.3, color=color.green)
#Labels to show how to move the robot
label_1=label(pos=(8,18,0), text='Use arrows to move in plane. Use a and d to rotate. Use w and s to open/close the clamp')
label_2=label(pos=(8,-8,0), text='Clamp status = Close')
#Labels to improve the visualization of the position of the arm
in_x_plane=arrow(pos=(0,0,0), axis=(10,0,0), shaftwidth=0.1, headwidth=0.1, color=color.orange, opacity=0.3)
in_y_plane=arrow(pos=(0,0,0), axis=(0,10,0), shaftwidth=0.1, headwidth=0.1, color=color.orange, opacity=0.3)
in_z_plane=arrow(pos=(0,0,0), axis=(0,0,10), shaftwidth=0.1, headwidth=0.1, color=color.orange, opacity=0.3)

#Initial position
x=10
y=10
phi=0 #angle for base rotation
clamp = 'Close' #Clamp is close

#now we made an infinite while loop to keep the program running
while (1==1):
    rate(20) #refresh rate required for VPython
    ev = scene.waitfor('keydown')
    if ev.key == 'up':
        y = y+0.25
    elif ev.key == 'down':
        y = y-0.25
    elif ev.key == 'right':
        x = x+0.25
    elif ev.key == 'left':
        x = x-0.25
    elif ev.key == 'a':
        phi = phi-5
        if phi <= -90:
            print 'Minimum angle reached'
            phi = -90
    elif ev.key == 'd':
        phi = phi+5
        if phi >= 90:
            print 'Maximum angle reached'
            phi = 90
    elif ev.key == 'q':
        print 'Going to initial position...'
        x=10
        y=10
        phi=0
    elif ev.key == 'w':
        print 'Opening clamp...'
        clamp = 'Open'
    elif ev.key == 's':
        print 'Closing clamp...'
        clamp = 'Close'

    #Calculate the distance to the target and the angle to the x axis
    T = np.sqrt(x*x+y*y) #Distance to target
    if l1+l2<T+0.5: #Loop to prevent targets out of range
        print 'Position cannot be reached, reseting...'
        x=10
        y=10
        T = np.sqrt(x*x+y*y)
    theta = np.arctan2(y,x)

    #Calculate the Area of the triangle using Heron's formula
    s=(l1+l2+T)/2 #Calculate the semiperimeter
    A= np.sqrt(s*(s-l1)*(s-l2)*(s-T)) #Area of the triangle 2-link arm
    
    #Now we calculate the angles
    alpha = np.arcsin((2*A)/(l1*T))
    gamma = np.arcsin((2*A)/(T*l2))
    beta = np.arcsin((2*A)/(l1*l2))
    if beta>0.5:
        beta = np.pi-alpha-gamma     
    ang=3.141592+alpha+theta+beta #Correct angle from the l1 indicator

    #Update the indicators
    indicator.axis=(x*np.cos(phi*0.01745),y,x*np.sin(phi*0.01745)) #calculate the new axis of the indicator
    l1_ind.axis=(l1*np.cos(alpha+theta)*np.cos(phi*0.01745),l1*np.sin(alpha+theta),l1*np.cos(alpha+theta)*np.sin(phi*0.01745)) #calculate the new axis of l1
    l2_ind.pos=(l1*np.cos(alpha+theta)*np.cos(phi*0.01745),l1*np.sin(alpha+theta),l1*np.cos(alpha+theta)*np.sin(phi*0.01745)) #calculate new origin for l2
    l2_ind.axis=(l2*np.cos(ang)*np.cos(phi*0.01745),l2*np.sin(ang),l2*np.cos(ang)*np.sin(phi*0.01745)) #Calculate new axis for l2
    in_x_plane.pos=(0,0,x*np.sin(phi*0.01745))
    in_y_plane.pos=(x*np.cos(phi*0.01745),0,x*np.sin(phi*0.01745))
    in_z_plane.pos=(x*np.cos(phi*0.01745),0,0)
    in_x_plane.axis=(x*np.cos(phi*0.01745),0,0)
    in_y_plane.axis=(0,y,0)
    in_z_plane.axis=(0,0,x*np.sin(phi*0.01745))
    label_2.text='Clamp status = '+clamp
