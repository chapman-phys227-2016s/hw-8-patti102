#!/usr/python/bin
"""
Author: Taylor Patti
Particle.py

This update on the Particle class conflines the particles to a box
with a hole in it. The particles can leave the box or come back in if
they go through the hole.

"""
import numpy as np
import time
import random
from unittest import TestCase


class Particle:
    """
    Defines particle objects that are seeded at initialization
and move around accordingly
    """
    def __init__(self, seed = -1, x= 0, y = 0):
        if seed == -1:
            seed = random.randint(2, 1000000)
        self.x = x
        self.y = y
        self.RNG = np.random.RandomState(seed)

    def move(self, step_size = 1):
        """
        Moves in a random (seeded) direction with a distance of
        an optional stepsize. The particles are confined to a 2 by 2 box
        but can leave through a hole between x = -2 and x = -1 at the bottom
        of the box for this particle.
        """
        switch = self.RNG.randint(1, 5)
        if(switch == 1):
            if self.y >= 2:
                pass
            else:
                self.y += step_size #Up
        elif(switch == 2):
            if self.x >= 2:
                pass
            else:
                self.x += step_size #Right
        elif(switch == 3):
            if self.y <= - 2:
                if self.x <= -1:
                    self.y -= step_size #Down
                else:
                    pass
            else:
                self.y -= step_size
        else:
            if self.x <= -2:
                pass
            else:
                self.x -= step_size #left

class test_Particle(TestCase):
    """
    Test Class for Particle.
    This class only extends with test functions
    """

    
    def test_confined_movement(self):
        """
        Given n number of steps, the particles
        should not deviate n units from the origin
        n = [10, 100, 1000]
        """
        n = [10, 100, 1000]
        testReturn = True
        for numberOfSteps in n:
            p = Particle()
            for x in xrange(numberOfSteps):
                p.move()
            if(p.x > numberOfSteps or p.x < (-1 * numberOfSteps) or p.y > numberOfSteps or p.y < (-1 * numberOfSteps)):
                testReturn = False
        assert(testReturn)

    def test_same_seed_movement(self, numberOfSteps = 100000):
        """
        2 Particles given the same seed should move identically
        We test that all positions of the two particles are identical
        to the numberOfSteps specified
        """
        p1 = Particle(1024901)
        p2 = Particle(1024901)
        testReturn = True
        for x in xrange(numberOfSteps):
            p1.move()
            p2.move()
            if(p1.x != p2.x or p1.y != p2.y):
                testReturn = False
        assert(testReturn)
        
    def test_Particle(self):
        seed_time = int(time.time()*10 % 10000)
        movement_matrix = np.zeros((3, 6))
        count = 0
        while count <= 2:
            particle = Particle(seed_time)
            other_count = 0
            while other_count <= 2:
                particle.move()
                movement_matrix[count, other_count] = particle.x
                other_count = other_count + 1
                movement_matrix[count, other_count] = particle.y
                other_count = other_count + 1
            count = count + 1
        apt = np.all(movement_matrix[0, :] == movement_matrix[1, :]) and np.all(movement_matrix[0, :] == movement_matrix[2, :])
        msg = 'Particle Function does not work.'
        assert apt, msg
        
    def test_StayBox(self):
        """Ensures that the particles cannot travel outside of the
        typical confines of the box."""
        particle = Particle()
        n = 0
        apt = 1
        while n <= 100:
            n += 1
            particle.move()
            if (particle.y > 2 or particle.x > 2):
                apt = 0
        msg = "Particle box does not hold particles."
        assert apt, msg
        
    def test_ParticleEscape(self):
        """Ensures that the particles can go through the hole in the box
        as it allows 10000 for the particle to reach one of the first spaces
        outside of the boxes limitations but through the hole."""
        particle = Particle()
        n = 0
        apt = 0
        while n <= 10000:
            n += 1
            particle.move()
            if(particle.y == -3 and particle.x == -2):
                apt = 1
        msg = "Particle cannot escape from the hole."
        assert apt, msg