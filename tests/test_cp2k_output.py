import os
import numpy as np
import unittest
from context import dpdata

class TestCP2KSinglePointEnergy:
    def test_atom_names(self) :
        self.assertEqual(self.system.data['atom_names'], ['C','H','O'])
    def test_atom_numbs(self) :
        self.assertEqual(self.system.data['atom_numbs'], [4,6,3])
    def test_atom_types(self) :
        ref_type = [0,0,0,1,2,0,1,1,2,2,1,1,1]
        ref_type =  np.array(ref_type)
        for ii in range(ref_type.shape[0]) :
            self.assertEqual(self.system.data['atom_types'][ii], ref_type[ii])
    def test_cell(self) :
        fp = open('cp2k/ref_cell')
        cell = []
        for ii in fp :
            cell.append([float(jj) for jj in ii.split()])
        cell = np.array(cell)
        for ii in range(cell.shape[0]) :
            for jj in range(cell.shape[1]) :
                self.assertEqual(self.system.data['cells'][0][ii][jj], cell[ii][jj])


    def test_coord(self) :
        fp = open('cp2k/ref_coord')
        coord = []
        for ii in fp :
            coord.append([float(jj) for jj in ii.split()])
        coord = np.array(coord)
        for ii in range(coord.shape[0]) :
            for jj in range(coord.shape[1]) :
                self.assertEqual(self.system.data['coords'][0][ii][jj], coord[ii][jj])

    def test_force(self) :
        eV = 2.72113838565563E+01
        angstrom = 5.29177208590000E-01
        fp = open('cp2k/ref_force')
        force = []
        for ii in fp :
            force.append([float(jj) for jj in ii.split()])
        force = np.array(force)
        for ii in range(force.shape[0]) :
            for jj in range(force.shape[1]) :
                self.assertEqual(self.system.data['forces'][0][ii][jj], force[ii][jj]*eV/angstrom)

    def test_energy(self) :
        eV = 2.72113838565563E+01
        ref_energy = -74.161831345521179
        self.assertEqual(self.system.data['energies'][0], ref_energy*eV)



class TestCP2KLabeledOutput(unittest.TestCase, TestCP2KSinglePointEnergy):

    def setUp(self):
        self.system = dpdata.LabeledSystem('cp2k/cp2k_output', fmt = 'cp2k/output')

if __name__ == '__main__':
    unittest.main()

