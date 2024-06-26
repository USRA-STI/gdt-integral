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
#

from astropy.time import TimeFromEpoch, Time

__all__ = ['IntegralSecTime', 'Time']

class IntegralSecTime(TimeFromEpoch):

    """Represents the number of seconds elapsed since Jan 1, 2000, 00:00:00 TT
    """
    name = 'integral'
    """(str): Name of the mission"""
    
    unit = 1.0 / 86400 
    """(float): unit in days"""
    
    epoch_val = '2000-01-01 00:00:00.000'
    """(str): The epoch in Terrestrial Time"""
    
    epoch_scale = 'tt'
    """(str): The scale of :attr:`epoch_val`"""

    epoch_val2 = None
    
    epoch_format = 'iso'
    """(str): Format of :attr:`epoch_val2`"""
