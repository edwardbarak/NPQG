import numpy as np
from fractions import Fraction
from vectors import Point, Vector
from math import pi

# TODO
class simulator:
    """Simulator object. Used to simulate n planckSphere interactions over t time.

    Args:
        n (int): Number of planckSpheres to generate
        t (int): Duration of simulation in planck time
        
        minDist (int): Minimum distance between generated planckSpheres. Default is planckSphere.radius * 2
        maxDist (int): Maximum distance between generated planckSpheres. Default is planckSphere.electricFieldMaxRadius * 2 + minDist
        
        minXVector (int): Minimum velocity for generated planckSpheres on X axis. Default is 0.
        maxXVector (int): Maximum velocity for generated planckSpheres on X axis. Default is planckSphere.electricFieldMaxRadius.
        minYVector (int): Minimum velocity for generated planckSpheres on Y axis. Default is 0.
        maxYVector (int): Maximum velocity for generated planckSpheres on Y axis. Default is planckSphere.electricFieldMaxRadius.
        minZVector (int): Minimum velocity for generated planckSpheres on Z axis. Default is 0.
        maxZVector (int): Maximum velocity for generated planckSpheres on Z axis. Default is planckSphere.electricFieldMaxRadius.

        boundingBox (tuple(int, int, int)): Defines dimensions of box where planckSpheres can be generated using a tuple of (xLength, yLength, zLength). Default is n * planckSphere.electricFieldMaxRadius * 2 for x, y, & z.

    """

    # TODO
    def __init__(
        self, 
        planckSphere,
        n, 
        t, 
        minDist=planckSphere.radius*2,
        maxDist=planckSphere.electricFieldMaxRadius*2+planckSphere.radius*2,
        minXVector=0,
        maxXVector=planckSphere.electricFieldMaxRadius,
        minYVector=0,
        maxYVector=planckSphere.electricFieldMaxRadius,
        minZVector=0,
        maxZVector=planckSphere.electricFieldMaxRadius,
        boundingBox=None,
        ):

        if boundingBox == None:
            __defaultLength = n * planckSphere.electricFieldMaxRadius * 2
            boundingBox = (__defaultLength, __defaultLength, __defaultLength)
                        
        # self.currentDB = self.__generateSpheres(n, boundingBox)
        pass

    # TODO
    def __generateSpheres(self, n, boundingBox):
        # 
        # return np.array of planckSphere
        pass        

class planckSphere:
    """Planck sphere object.
    
    Args:
        planckType (str): 'electrino' OR 'positrino'
        planckRadius (float): radius of planck Sphere in planck lengths. This is always 1. Planck particles can touch, but not overlap.
        point (Point): Point object from vectors library in planck lengths
        vector (Vector): Vector object from vectors library in planck lengths
        chargeMagnitude (Fraction): Fraction object from fractions library 
    """

    # Class Variables
    radius = 1.0 # radius of the planck sphere is the planck length. 
    diameter = 2 * radius
    circumference = 2 * pi * radius
    surfaceArea = 4 * pi * radius**2
    volume = (4/3) * pi * (radius**2)

    electricFieldMaxRadius = 100

    def __init__(self, planckType, planckRadius, point=Point(0,0,0), vector=Vector(0,0,0), chargeMagnitude=Fraction(1,6)):
        # process args
        if planckType == 'electrino':
            self.planckType = planckType
            self.charge = chargeMagnitude * -1
        elif planckType == 'positrino':
            self.planckType = planckType
            self.charge = chargeMagnitude
        else:
            raise TypeError('planckType must be electrino OR positrino')                     

        if isinstance(point, Point):
            self.point = point
        if isinstance(vector, Vector):
            self.vector = vector

        self.electricFieldTime = 0
        self.electricFieldRadius = 0
        self.magneticFieldTime = 0
        self.magneticFieldRadius = 0

    # TODO
    def nextPoint(self):
        pass
    
    def calculateCurrentElectricField(self, electricFieldMaxRadius):
        if self.electricFieldTime <= electricFieldMaxRadius:
            self.electricFieldRadius = self.charge/(6 * (self.electricFieldTime ** 2))
            self.electricFieldTime += 1
        else:
            self.electricFieldTime = 0
            self.electricFieldRadius = 0

        # NOTE: Each and every Planck sphere is always emitting an electric field.
        # NOTE: The electric field emitted by a Planck sphere propogates at local c in Map 1 (Euclidean space and time).
        # NOTE: The radial distance from the center of the sphere is used to calculate field strength.         
        # NOTE: We should measure distance such that everything is measured in planck lengths as the unit vector. 

        # NOTE: Spheres are immutable so no other Planck sphere can overlap within their radius.         
        # NOTE: At a radial distance of 1 Planck length, i.e., the surface of the Planck sphere, electric field is (e/6)/ (1 squared) which is e/6. 
        # NOTE: At a radial distance of 1.5 Planck lengths the field is e/(6*1.5*1.5). 
        # NOTE: Charge is measured in e, so likewise e can be considered as 1 unit charge.
        # NOTE: Assumption: Electric fields are not impeded by other Planck spheres. (i.e., passes through them)
        # NOTE: Electric field spreads out spherically at 1/(radial distance squared)
        # NOTE: At each point in space the electric field has a vector direction, which is radial from the location of the Planck sphere at the time when it was emitted.
        # NOTE: At each point in absolute time and absolute space (Map 1) the total vector electric field is the vector sum of all arriving electric fields.
        pass
    
    # TODO
    def calculateCurrentMagneticField(self):
        # TODO: Calculate radius of current magnetic field

        # TODO: look at shape of spreading magnetic field from a moving charge.
        # NOTE: If a particle is moving it creates a magnetic field.  
        # NOTE: Magnetic fields exert forces on charged particles. 
        # NOTE: The magnetic field emitted by a Planck sphere propogates at local c in Map 1 (Euclidean space and time). 
        # NOTE: The Planck sphere charge plays into the configuration of the magnetic field (like is it curling clockwise or anticlockwise).
        # NOTE: Assumption: Magnetic fields are not impeded by other Planck spheres. (i.e., passes through them)        
        # NOTE: At each point in space the magnetic field has a vector direction, which is related (TBD) to the location of the Planck sphere at the time when it was emitted.
        # NOTE: At each point in absolute time and absolute space (Map 1) the total vector magnetic field is the vector sum of all arriving magnetic fields.
        pass
    
    # TODO
    def calculateElectricFieldInteraction(self):
        # TODO: Calculate distance from self and target planck sphere, compare distance between both spheres with self.electricFieldRadius and target.electricFieldRadius
        # if dist(self, target) <= (self.electricFieldRadius + target.electricFieldRadius): interact()
        
        # NOTE: Electric fields exert forces on other Planck spheres.
        # NOTE: electrino repulses electrino
        # NOTE: positrino repulses positrino
        # NOTE: electrino attracts positrino and vice versa.
        pass

    # TODO
    def calculateMagneticFieldInteraction(self):
        # TODO: Calculate distance from self and target planck sphere, compare distance between both spheres with self.magneticFieldRadius and target.magneticFieldRadius
        # if dist(self, target) <= (self.magneticFieldRadius + target.magneticFieldRadius): interact()
        pass

    # TODO
    def calculateKineticInteraction(self):
        # TODO: Calculate distance from self and target planck sphere, compare distance between both spheres with self.radius and target.radius
        # if dist(self, target) <= (self.radius + target.radius): interact()
        pass

    # TODO
    """
    FUNCTION: planckSphereAtAbsolutePointTime
    Planck Sphere at absolute point and time in Map 1 (Euclidean space and time) 
    
    Args:
        This is a Planck sphere in Map 1 absolute location (x,y,z) at absolute time t.
        We will need to define some granularities for simulations, like 1/Nth a Planck length. and 1/Mth a Planck time.
        We will need to learn how sensitive the simulation is to granularities N and M.
        The larger the N, the smaller the spatial granularity and this may correspond to greater computation.
        The larger the M, the smaller the time granularity and this will correspond to greater computation.
        We don't need to calculate the full x * y * z * t for the range of simulation volume and time span.
        We only need to calculate at points in space that correspond to the centers of all Planck spheres at each absolute time t.
        Here are the characteristics of a PointTime:
        1) Is a Planck sphere center at that x,y,z,t? We will focus on when this is true. 
        There is no action caused by electric or magnetic field at a PointTime that is not the center of a Planck sphere.
        2) Vector sum of all arriving electric fields.
        3) Vector sum of all arriving magnetic fields.
        4) Vector velocity of the Planck sphere. This is used in the kinetic energy calculation, etc.
        Now we can calculate the force on each Planck sphere and its characteristics at t plus delta t.        
    """
