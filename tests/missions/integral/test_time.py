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
from gdt.missions.integral.time import *

# Time 1
met1 = 0
tt_str1 = '2000-01-01 00:00:00.000'


# Time 2
met2 = 60307184.184
tt_str2= '2001-11-28 23:59:44.184'

# Time 3
met3 = 731519004.372
tt_str3 = '2023-03-07 15:43:24.372'


class TestTime():
    
    def test_to_tt(self):
        assert Time(met1, format='integral').iso == tt_str1
        assert Time(met2, format='integral').iso == tt_str2
        assert Time(met3, format='integral').iso == tt_str3

    def test_to_integral(self):
        assert Time(tt_str1, format='iso', scale='tt').integral == met1
        assert Time(tt_str2, format='iso', scale='tt').integral == met2
        assert Time(tt_str3, format='iso', scale='tt').integral == met3
    
