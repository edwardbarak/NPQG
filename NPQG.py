from fractions import Fraction
from vectors import Point, Vector

class planckSphere:
    """Planck sphere object.
    
    Args:
        planckType (str): 'electrino' OR 'positrino'
        planckRadius (float): radius of planck in planck lengths
        point (Point): Point object from vectors library in planck lengths
        vector (Vector): Vector object from vectors library in planck lengths
        chargeMagnitude (Fraction): Fraction object from fractions library 
    """

    def __init__(self, planckType, planckRadius, point=Point(0,0,0), vector=Vector(0,0,0), chargeMagnitude=Fraction(1,6)):
        if planckType == 'electrino':
            self.planckType = planckType
            self.charge = chargeMagnitude * -1
        elif planckType == 'positrino':
            self.planckType = planckType
            self.charge = chargeMagnitude
        else:
            raise TypeError('planckType must be electrino OR positrino')            
        
        self.radius = float(planckRadius)

        if isinstance(point, Point):
            self.point = point
        if isinstance(vector, Vector):
            self.vector = vector    

    def nextPoint(self):
        # TODO
        pass
    
    def calculateElectricField(self):
        # TODO
        # NOTE: The radial distance from the center of the sphere. The radius of the planck sphere is the planck length. Spheres are immutable so nothing can get inside that radius. We should measure distance such that everything is measured in planck lengths as the unit vector. So 1 is at the radius of the sphere and the electric field is (e/6)/ (1 squared) which is e/6. At 1.5 radius the field is e/(6*1.5*1.5). Charge is measured in e, so likewise e can be considered as 1.
        pass
    
    def calculateMagneticField(self):
        # TODO
        # NOTE: If a particle is moving it creates a magnetic field.  And magnetic fields exert forces on charged particles. And like above, the field takes a while to propagate.  The charge plays into the configuration of the magnetic field (like is it curling clockwise or anticlockwise).
        pass