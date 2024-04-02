# CONTAINS TECHNICAL DATA/COMPUTER SOFTWARE DELIVERED TO THE U.S. GOVERNMENT 
# WITH UNLIMITED RIGHTS
#
# Grant No.: 80NSSC21K0651
# Grantee Name: Universities Space Research Association
# Grantee Address: 425 3rd Street SW, Suite 950, Washington DC 20024
#
# Developed by: Colleen A. Wilson-Hodge
# 			    National Aeronautics and Space Administration (NASA)
#     			Marshall Space Flight Center
#     			Astrophysics Branch (ST-12)
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
#
import unittest
from astropy.io import fits
from gdt.core import data_path
from gdt.missions.integral.spi.spi_acs import Spi_acs

test_file = data_path.joinpath('integral/spiacs_lc_query-3.1.fits')

hdu_list = fits.open(test_file)
data = hdu_list[1].data
data_rates = data['RATE'][1:]
data_lo_edge = data['TIME'][1:]
data_hi_edge = data['TIME'][:-1]
data_exp = data_hi_edge - data_lo_edge

t0 = 731519205.1627802
t_start = 731518935.1876125
t_stop = 731519475.1879478
obsdate = '2023-03-07T15:42:15.188'
obsdateend = '2023-03-07T15:42:15.188'
mjdref = 51544.0


t1 = -268.9501678221859 # 'Time' row 11 of file spiacs_lc_query-3.1.fits
t2 = -19.95001280447468 # 'Time' row 2501 of file spiacs_lc_query-3.1.fits
t3 = 260.050162661355 # 'Time' row 5301 of file spiacs_lc_query-3.1.fits

r1 = 89640.0 # 'Rates' row 11 of file spiacs_lc_query-3.1.fits
r2 = 95100.0 # 'Rates' row 2501 of file spiacs_lc_query-3.1.fits
r3 = 89360.0 # 'Rates' row 5301 of file spiacs_lc_query-3.1.fits


class TestSpi_acs(unittest.TestCase):

    def setUp(self):
        self.spi_acs= Spi_acs.open(test_file)
    
    def test_timezero(self):
        self.assertAlmostEqual(self.spi_acs.timezero, t0, places=7) 

    def test_tstart(self):
        self.assertAlmostEqual(self.spi_acs.tstart, t_start, places=7)

    def test_tstop(self):
        self.assertAlmostEqual(self.spi_acs.tstop, t_stop, places=7)

    def test_obsdate(self):
        assert self.spi_acs.obsdate == obsdate

    def test_obsdateend(self):
        assert self.spi_acs.obsdateend == obsdateend 

    def test_mjdref(self):
        self.assertEqual(self.spi_acs.mjdref, mjdref)

    def test_time(self):
        self.assertAlmostEqual(self.spi_acs.time[10], t1, places=7)
        self.assertAlmostEqual(self.spi_acs.time[2500], t2, places=7)
        self.assertAlmostEqual(self.spi_acs.time[5300], t3, places=7)
        self.assertAlmostEqual(self.spi_acs.time.all(), data['TIME'].all(), places=7)

    def test_rates(self):
        self.assertAlmostEqual(self.spi_acs.rates[10], r1, places=7)
        self.assertAlmostEqual(self.spi_acs.rates[10], data['RATE'][10], places=7)
        self.assertAlmostEqual(self.spi_acs.rates[2500], r2, places=7)
        self.assertAlmostEqual(self.spi_acs.rates[2500], data['RATE'][2500], places=7)
        self.assertAlmostEqual(self.spi_acs.rates[5300], r3, places=7)
        self.assertAlmostEqual(self.spi_acs.rates[5300], data['RATE'][5300], places=7)
        self.assertAlmostEqual(self.spi_acs.rates.all(), data['RATE'].all(), places=7)

    def test_lightcurve(self):
        time_edge1 = self.spi_acs.timezero + self.spi_acs.time[1:]
        time_edge2 = self.spi_acs.timezero + self.spi_acs.time[:-1]
        exp = time_edge1 - time_edge2
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().rates.all(), self.spi_acs.rates[1:].all(), places=7)
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().rates.all(), data_rates.all(), places=7)
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().lo_edges.all(), time_edge1.all(), places=7)
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().lo_edges.all(), data_lo_edge.all(), places=7)
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().hi_edges.all(), time_edge2.all(), places=7)
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().hi_edges.all(), data_hi_edge.all(), places=7)
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().exposure.all(), exp.all(), places=7)
        self.assertAlmostEqual(self.spi_acs.to_lightcurve().exposure.all(), data_exp.all(), places=7)

    
