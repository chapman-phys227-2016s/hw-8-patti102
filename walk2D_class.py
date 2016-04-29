#! /usr/bin/env python

"""
File: walk2D_class.py
Copyright (c) 2016 Michael Seaman
License: MIT

Description: Draws upon the Particles and Particle class to output ultimately output
pdfs via commandline interface
1st arg: number of particles
2nd arg: number of steps

"""
from Particles import Particles
from Particle import Particle
import sys


partics = Particles([ Particle() for i in xrange(int(sys.argv[1]))])
partics.moves(int(sys.argv[2]))


