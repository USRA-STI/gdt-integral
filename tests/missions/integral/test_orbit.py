# CONTAINS TECHNICAL DATA/COMPUTER SOFTWARE DELIVERED TO THE U.S. GOVERNMENT 
# WITH UNLIMITED RIGHTS
#
# Grant No.: 80NSSC21K0651
# Grantee Name: Universities Space Research Association
# Grantee Address: 425 3rd Street SW, Suite 950, Washington DC 20024
#
# Copyright 2024 by Universities Space Research Association (USRA). All rights 
# reserved.
#
# Developed by: Suman Bala
#               Universities Space Research Association
#               Science and Technology Institute
#               https://sti.usra.edu
#
# This work is a derivative of the Gamma-ray Data Tools (GDT), including the 
# Core and Fermi packages, originally developed by the following:
#
#     William Cleveland and Adam Goldstein
#     Universities Space Research Association
#     Science and Technology Institute
#     https://sti.usra.edu
#     
#     Daniel Kocevski
#     National Aeronautics and Space Administration (NASA)
#     Marshall Space Flight Center
#     Astrophysics Branch (ST-12)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not 
# use this file except in compliance with the License. You may obtain a copy of 
# the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
# License for the specific language governing permissions and limitations under 
# the License.

import unittest
import numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.coordinates.representation as r
from gdt.missions.integral.orbit import IntegralOrbit
from gdt.missions.integral.frame import *

test_file = Path(__file__).parent.joinpath('data', 'sc_orbit_param.fits.gz')

hdu_list = fits.open(test_file)
data = hdu_list[1].data
header = hdu_list[1].header


class TestIntegralOrbit(unittest.TestCase):
    
    def setUp(self):
        self.integral_orbit = IntegralOrbit.open(test_file)

    def test_date(self):
        assert self.integral_orbit.date == header['DATE']

    def test_ertfirst(self):
        assert self.integral_orbit.ertfirst == header['ERTFIRST']

    def test_ertlast(self):
        assert self.integral_orbit.ertlast == header['ERTLAST']

    def test_revol_header(self):
        self.assertEqual(self.integral_orbit.revol_header, str(header['REVOL']))
    
    def test_swid(self):
        assert self.integral_orbit.swid == header['SWID']

    def test_sw_type(self):
        assert self.integral_orbit.sw_type == header['SW_TYPE']

    def test_swbound(self):
        assert self.integral_orbit.swbound == header['SWBOUND']

    def test_bcppid(self):
        assert self.integral_orbit.bcppid == header['BCPPID']

    def test_preswid(self):
        assert self.integral_orbit.preswid == header['PREVSWID']

    def test_obtstart(self):
        assert self.integral_orbit.obtstart == header['OBTSTART']

    def test_obtend(self):
        assert self.integral_orbit.obtend == header['OBTEND']

    def test_obtime(self):
        self.assertAlmostEqual(self.integral_orbit.obtime.all(), data['OB_TIME'].all(), places=7)

    def test_revol(self):
        self.assertAlmostEqual(self.integral_orbit.revol.all(), data['REVOL'].all(), places=7)

    def test_revol_phase(self):
        self.assertAlmostEqual(self.integral_orbit.revol_phase.all(), data['REVOL_PHASE'].all(), places=7)

    def test_revol_frac(self):
        self.assertAlmostEqual(self.integral_orbit.revol_frac.all(), data['REVOL_FRAC'].all(), places=7)

    def test_distance(self):
        self.assertAlmostEqual(self.integral_orbit.distance.all(), data['DISTANCE'].all(), places=7)

    def test_xpos(self):
        self.assertAlmostEqual(self.integral_orbit.xpos.all(), data['XPOS'].all(), places=7)

    def test_ypos(self):
        self.assertAlmostEqual(self.integral_orbit.ypos.all(), data['YPOS'].all(), places=7)

    def test_zpos(self):
        self.assertAlmostEqual(self.integral_orbit.zpos.all(), data['ZPOS'].all(), places=7)

    def test_xvel(self):
        self.assertAlmostEqual(self.integral_orbit.xvel.all(), data['XVEL'].all(), places=7)

    def test_yvel(self):
        self.assertAlmostEqual(self.integral_orbit.yvel.all(), data['YVEL'].all(), places=7)

    def test_zvel(self):
        self.assertAlmostEqual(self.integral_orbit.zvel.all(), data['ZVEL'].all(), places=7)

    def test_ra_scx(self):
        self.assertAlmostEqual(self.integral_orbit.ra_scx.all(), data['RA_SCX'].all(), places=7)

    def test_dec_scx(self):
        self.assertAlmostEqual(self.integral_orbit.dec_scx.all(), data['DEC_SCX'].all(), places=7)

    def test_ra_scz(self):
        self.assertAlmostEqual(self.integral_orbit.ra_scz.all(), data['RA_SCZ'].all(), places=7)

    def test_dec_scz(self):
        self.assertAlmostEqual(self.integral_orbit.dec_scz.all(), data['DEC_SCZ'].all(), places=7)

    def test_posangle(self):
        self.assertAlmostEqual(self.integral_orbit.posangle.all(), data['POSANGLE'].all(), places=7)

    def test_get_spacecraft_frame(self):
        #test_to_integral_frame
        x_pointing = SkyCoord(self.integral_orbit.ra_scx, self.integral_orbit.dec_scx, unit='deg')
        z_pointing = SkyCoord(self.integral_orbit.ra_scz, self.integral_orbit.dec_scz, unit='deg')
        frame = self.integral_orbit.get_spacecraft_frame()
        # z-axis should be at zen=0 (el=90)
        zaxis = z_pointing.transform_to(frame)
        self.assertAlmostEqual(np.sin(np.deg2rad(zaxis.el.value)).all(), 1.0, places=2)
        
        # x-axis should be at az=0, zen=90 (el=0)
        xaxis = x_pointing.transform_to(frame)
        self.assertAlmostEqual(np.cos(xaxis.az.value).all(), 1.0, places=3)
        self.assertAlmostEqual(xaxis.el.value.all(), 0.0, places=3)

        #test_to_icrs_frame
        for i in range(0,len(zaxis)):
            z_coord = SkyCoord(0.0, 90.0, unit='deg', frame=frame[i]).icrs
            self.assertAlmostEqual(z_coord.ra.value[0], z_pointing.ra.value[i], places=2)
            self.assertAlmostEqual(z_coord.dec.value[0], z_pointing.dec.value[i], places=2)
    