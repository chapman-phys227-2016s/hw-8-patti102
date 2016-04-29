#! /usr/bin/env python

"""
File: Particles.py
Copyright (c) 2016 Taylor Patti
License: MIT

This update on the Particles class confines the particles to a box
with a hole in it. The particles can leave the box or come back in if they
go through the hole in the box.

"""
import matplotlib
matplotlib.use('Agg')
import random as R
import matplotlib.pyplot as plt
from unittest import TestCase
import numpy as np
import time
from Particle import *


class Particles:
    """
    Moves and plots objects of type 'Particle'
    """
    def __init__(self, particles):
        """
        particles is an array of type 'Particle'
        """
        self.particles = particles
        self.np = len(particles)
        self.step = 0
    def move(self, step_size = 1):
        """
        Translates all particles uniformly by step_size
        """
        for p in self.particles:
            p.move(step_size)
        self.step += 1
        
    def plot(self):
        """
        Plots all particles
        """
        xpositions = []
        ypositions = []
        for p in self.particles:
            xpositions.append(p.x)
            ypositions.append(p.y)
            plt.plot(xpositions, ypositions, 'ko',
                     axis = [-100,100,-100,100],
                     title = '%d particles after %d steps' %
                         (self.np, self.step+1),
                     savefig = 'tmp_%03d.pdf' % (self.step+1))
    
    def generate_frame(self):
        """
        Plots the particles and outputs them to a file
        """
        xpositions = []
        ypositions = []
        for p in self.particles:
            xpositions.append(p.x)
            ypositions.append(p.y)
            fig, ax = plt.subplots(nrows = 1, ncols = 1)
            ax.plot(xpositions, ypositions, 'ko')
            ax.set_ylim([-2,2])
            ax.set_xlim([-2,2])
            fig.savefig('tmp_%03d.png' % (self.step))
            plt.close(fig)

    def moves(self, N = 10, step_size = 1):
        """
        Loops over move() and plot() function N times
        """
        self.generate_frame()
        for i in xrange(N):
            self.move(step_size)
            self.generate_frame()

class Test_Particles(TestCase):
    def test_Particle(self):
        """Makes sure that the particles with the same random seed move in the same manner."""
        seed_time = int(time.time()*10 % 10000)
        particle_list = [Particle(seed_time) for _ in xrange(3)]
        particles = Particles(np.array(particle_list))
        particles.move()
        x_array = np.array([particles.particles[n].x for n in xrange(3)])
        y_array = np.array([particles.particles[n].y for n in xrange(3)])
        apt = ((x_array[0] == x_array).all() and (y_array[0] == y_array).all())
        msg = 'Particles did not move in the same way'
        assert apt, msg