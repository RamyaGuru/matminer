#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:31:31 2018

@author: guru

script to play aorund with pymatgen phonon tools and matminer
"""

from __future__ import division, unicode_literals, print_function

import numpy as np

#from pymatgen.matproj.rest import MPRester
#mpr = MPRester('pfSJBa1OwitR5uNL')

from matminer.featurizers.base import BaseFeaturizer
from pymatgen.phonon.bandstructure import PhononBandStructure, PhononBandStructureSymmLine
from pymatgen.phonon.dos import PhononDos, CompletePhononDos
from pymatgen.phonon.plotter import PhononDosPlotter, PhononBSPlotter
from pymatgen import MPRester
from pymatgen.ext.matproj import MPRestError


from matminer.data_retrieval.retrieve_MP import MPDataRetrieval 
#import pandas as pd

mpd = MPDataRetrieval('pfSJBa1OwitR5uNL')


#this fetches the phonon bandstructure along a specific path in k-space
bstruct = mpd.get_dataframe("mp-149", ["phonon_bandstructure", "phonon_dos"])

bs_symm = bstruct["phonon_bandstructure"][0]

bs_dos = bstruct["phonon_dos"][0]

#bstructGamma_X = PhononBandStructureSymmLine(bstruct)

branch = bs_symm.get_branch(148)
print(branch)
print(len(bs_symm.qpoints))


bsplt = PhononBSPlotter(bs_symm)
dosplt = PhononDosPlotter()
dosplt.add_dos("Total", bs_dos)
dosplt.get_plot().show()
bsplt.get_plot().show()
bsplt.plot_brillouin()








