.. _integral-headers:

**************************************************************
INTEGRAL FITS Headers (:mod:`gdt.missions.integral.headers`)
**************************************************************
This module defines all of the FITS headers for the public data files. While
these classes are not usually directly called by the user, we may load one up
and see the contents and default values.  For example, here is the set of 
header definitions for Integral Orbit Parameter:

    >>> from gdt.missions.integral.headers import SPIOrbitHeader
    >>> hdrs = SPIOrbitHeader()
    >>> hdrs
    <PhaiiTriggerHeaders: 2 headers>
    
Here is the ``PRIMARY`` header and default values (retrieved by index):
    >>> hdrs[0]
	SIMPLE  =                    T / file does conform to FITS standard             
	BITPIX  =                    8 / number of bits per data pixel                  
	NAXIS   =                    0 / number of data axes                            
	EXTEND  =                    T / FITS dataset may contain extensions            
	COMMENT   FITS (Flexible Image Transport System) format is defined in 'Astronomy
	COMMENT   and Astrophysics', volume 376, page 359; bibcode: 2001A&A...376..359H 
	COMMENT                                                                         
           


And here is the ``SPECTRUM`` header and default values:

    >>> hdrs['SPECTRUM']
	XTENSION= 'BINTABLE'           / Binary table extension                         
	BITPIX  =                    8 / 8-bit bytes                                    
	NAXIS   =                    2 / 2-dimensional binary table                     
	NAXIS1  =                  122 / width of table in bytes                        
	NAXIS2  =                  244 / number of rows in table                        
	PCOUNT  =                    0 / size of special data area                      
	GCOUNT  =                    1 / one data group (required keyword)              
	TFIELDS =                   16 / number of fields in each row                   
	TTYPE1  = 'OB_TIME '           / Central on-board time                          
	TFORM1  = '4I      '           / Format of column OB_TIME                       
	TZERO1  =                32768 / offset for unsigned integers                   
	TSCAL1  =                    1 / data are not scaled                            
	TTYPE2  = 'REVOL   '           / Revolution number                              
	TFORM2  = '1I      '           / Format of column REVOL                         
	TZERO2  =                32768 / offset for unsigned integers                   
	TSCAL2  =                    1 / data are not scaled                            
	TTYPE3  = 'REVOL_PHASE'        / Phase of the revolution                        
	TFORM3  = '1D      '           / Format of column REVOL_PHASE                   
	TTYPE4  = 'REVOL_FRAC'         / Fractional revolution number                   
	TFORM4  = '1D      '           / Format of column REVOL_FRAC                    
	TTYPE5  = 'DISTANCE'           / Spacecraft distance from the Earth centre      
	TFORM5  = '1D      '           / Format of column DISTANCE                      
	TTYPE6  = 'XPOS    '           / X component of the s/c position vector         
	TFORM6  = '1D      '           / Format of column XPOS                          
	TTYPE7  = 'YPOS    '           / Y component of the s/c position vector         
	TFORM7  = '1D      '           / Format of column YPOS                          
	TTYPE8  = 'ZPOS    '           / Z component of the s/c position vector         
	TFORM8  = '1D      '           / Format of column ZPOS                          
	TTYPE9  = 'XVEL    '           / X component of the s/c velocity vector         
	TFORM9  = '1D      '           / Format of column XVEL                          
	TTYPE10 = 'YVEL    '           / Y component of the s/c velocity vector         
	TFORM10 = '1D      '           / Format of column YVEL                          
	TTYPE11 = 'ZVEL    '           / Z component of the s/c velocity vector         
	TFORM11 = '1D      '           / Format of column ZVEL                          
	TTYPE12 = 'RA_SCX  '           / Right ascension of s/c viewing direction       
	TFORM12 = '1D      '           / Format of column RA_SCX                        
	TTYPE13 = 'DEC_SCX '           / Declination of s/c viewing direction           
	TFORM13 = '1D      '           / Format of column DEC_SCX                       
	TTYPE14 = 'RA_SCZ  '           / Right ascension of the s/c Z-axis              
	TFORM14 = '1D      '           / Format of column RA_SCZ                        
	TTYPE15 = 'DEC_SCZ '           / Declination of the s/c Z-axis                  
	TFORM15 = '1D      '           / Format of column DEC_SCZ                       
	TTYPE16 = 'POSANGLE'           / Position angle in degrees                      
	TFORM16 = '1D      '           / Format of column POSANGLE                      
	EXTNAME = 'INTL-ORBI-SCP'      / Extension name                                 
	EXTREL  = '5.4     '           / ISDC release number                            
	BASETYPE= 'DAL_TABLE'          / Data Access Layer base type                    
	TELESCOP= 'INTEGRAL'           / Telescope or mission name                      
	ORIGIN  = 'ISDC    '           / Origin of FITS file                            
	INSTRUME= 'INTEGRAL'           / Instrument name                                
	ISDCLEVL= 'PRP     '           / ISDC level of data processing                  
	CREATOR = 'dp_aux_derive 1.1'  / Executable which created or modified this data 
	CONFIGUR= 'cons_sw-18.0.1_2009-12-07T21:05:31' / Software system configuration  
	DATE    = '2010-02-12T13:32:05' / Creation or modification date                 
	ERTFIRST= '2009-04-01T02:11:24' / Earth received time of the first packet       
	ERTLAST = '2009-04-01T02:43:57' / Earth received time of the last packet        
	REVOL   =                  789 / Revolution number                              
	SWID    = '078900560010'       / Science Window identifier                      
	SW_TYPE = 'POINTING'           / Type of the Science Window                     
	SWBOUND = 'OTF     '           / Reason for Science Window ending               
	BCPPID  = '07890056'           / Broadcast packet pointing ID at ScW start      
	PREVSWID= '078900550021'       / Identifier of the previous Science Window      
	OBTSTART= '00000213629501702144' / OBT of the start of the Science Window       
	OBTEND  = '00000213631552716800' / OBT of the end of the Science Window         
	TUNIT5  = 'km      '           / Unit of column DISTANCE                        
	TUNIT6  = 'km      '           / Unit of column XPOS                            
	TUNIT7  = 'km      '           / Unit of column YPOS                            
	TUNIT8  = 'km      '           / Unit of column ZPOS                            
	TUNIT9  = 'km/s    '           / Unit of column XVEL                            
	TUNIT10 = 'km/s    '           / Unit of column YVEL                            
	TUNIT11 = 'km/s    '           / Unit of column ZVEL                            
	TUNIT12 = 'deg     '           / Unit of column RA_SCX                          
	TUNIT13 = 'deg     '           / Unit of column DEC_SCX                         
	TUNIT14 = 'deg     '           / Unit of column RA_SCZ                          
	TUNIT15 = 'deg     '           / Unit of column DEC_SCZ                         
	TUNIT16 = 'deg     '           / Unit of column POSANGLE                        
	EXTVER  =                    1 / auto assigned by template parser               
	GRPID1  =                   -1 / EXTVER of Group containing this HDU            
	GRPLC1  = 'swg.fits'           / URL of file containing Group                   
	LONGSTRN= 'OGIP 1.0'           / The HEASARC Long String Convention may be used.            

See :external:ref:`Data File Headers<core-headers>` for more information about 
creating and using FITS headers.
    
Reference/API
=============

.. automodapi:: gdt.missions.integral.headers
   :inherited-members:


