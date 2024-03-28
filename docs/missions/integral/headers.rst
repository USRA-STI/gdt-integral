.. _integral-headers:

*****************************************************************
INTEGRAL FITS Headers (:mod:`gdt.missions.integral.headers`)
*****************************************************************
This module defines all of the FITS headers for the public data files. While
these classes are not usually directly called by the user, we may load one up
and see the contents and default values.  For example, here is the set of 
header definitions for Integral Orbit Parameter:

    >>> from gdt.missions.integral.headers import SPIOrbitHeader
    >>> hdrs = SPIOrbitHeader()
    >>> hdrs
    <SPIOrbitHeader: 2 headers>
    
And here is the ``INTL-ORBI-SCP`` header and default values:

    >>> hdrs['INTL-ORBI-SCP']
    EXTNAME = 'INTL-ORBI-SCP'      / name of this binary table extension            
    EXTREL  = '' / ISDC release number                                              
    TELESCOP= 'INTEGRAL'           / Name of mission/satellite                      
    INSTRUME= 'SPI     '           / Specific instrument used for observation       
    DATE    = '2024-03-28T16:08:25.374' / file creation or modification date (YYYY-M
    ERTFIRST= '' / Earth received time of the first packet                          
    ERTLAST = '' / Earth received time of the last packet                           
    REVOL   = '' / Revolution number                                                
    SWID    = '' / Science Window identifier                                        
    SW_TYPE = '' /  Type of the Science Window                                      
    SWBOUND = '' / Reason for Science Window ending                                 
    BCPPID  = '' / Broadcast packet pointing ID at ScW start                        
    PREVSWID= '' / Identifier of the previous Science Window                        
    OBTSTART= '' / OBT of the start of the Science Window                           
    OBTEND  = '' / OBT of the end of the Science Window                             

See :external:ref:`Data File Headers<core-headers>` for more information about 
creating and using FITS headers.
    
Reference/API
=============

.. automodapi:: gdt.missions.integral.headers
   :inherited-members:


