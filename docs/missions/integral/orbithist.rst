.. _integral-orbithist:


*************************************************************************************
Integral Position/Attitude History Data (:mod:`gdt.missions.integral.orbithist`)
*************************************************************************************

The ORBITHIST contains the spacecraft location, velosity in orbit and pointing information
of an entire observation duration. 

To read a ORBITHIST file, we open it with the |OrbitHist| class:

    >>> from gdt.core import data_path
    >>> from gdt.missions.integral.orbithist import OrbitHist
    >>> filepath = data_path.joinpath('integral-gbm/glg_orbithist_all_170101_v01.fit')
    >>> orbithist = OrbitHist.open("sc_orbit_param.fits.gz" )
    >>> orbithist
    <SPIOrbit(filename="sc_orbit_param.fits.gz") at 0x11fde4b60>
	
	No.	Name	Ver	Type	Cards	Dimensions
	0	PRIMARY	1	PrimaryHDU	20	()
	1	INTL-ORBI-SCP	1	BinTableHDU	90	244R x 16C
	
	
The data and the headder information of orbitfile can also be accessed:

    >>> orbithist.ertfirst
	'2009-04-01T02:11:24'
	
	>>> orbithist.date
	'2010-02-12T13:32:05'
	
	>>> orbithist.obtstart
	'00000213629501702144'
	
	>>> orbithist.obtend
	'00000213631552716800'
	
	>>> orbithist.swid
	'078900560010'
	
	>>> orbithist.revol_header
	'789'
	
	>>> orbithist.bcppid
	'07890056'

The spacecraft **frame** can be created from the orbithist object. The spacecraft
position and orientation as a function of time, and other spacecraft informations
can be asseced in the following way:

	>>> orbithist._obtime # The Central on-board time
	array([[    0, 49739, 32496,     0],
	       [    0, 49739, 32624,     0],
	       [    0, 49739, 32752,     0],
	       ... ... ...
	       [    0, 49739, 63472,     0],
	       [    0, 49739, 63600,     0]], dtype=uint16)
		   
	>>> orbithist.revol_frac
	array([789.63171907, 789.63175003, 789.63178098, 789.63181194,
	       789.6318429 , 789.63187386, 789.63190481, 789.63193577,
	       789.63196673, 789.63199769, 789.63202864, 789.6320596 ,
	       ... ... ...
	       789.63890121, 789.63893216, 789.63896312, 789.63899408,
	       789.63902504, 789.63905599, 789.63908695, 789.63911791,
	       789.63914887, 789.63917982, 789.63921078, 789.63924174],
	      dtype='>f8')

    >>> orbithist._distance # distance of spacecraft from the center of the Earth
	array([152873.50458927, 152869.90392388, 152866.30236285, 152862.69990592,
	       152859.09655321, 152855.49230478, 152851.88716029, 152848.28111949,
	       152844.67418299, 152841.0663504 , 152837.45762176, 152833.84799724,
	       ... ... ... 
	       152014.06864013, 152010.25912516, 152006.44870551, 152002.63738093,
	       151998.82515173, 151995.01201739, 151991.19797804, 151987.38303371,
	       151983.56718419, 151979.75042971, 151975.93277014, 151972.11420526],
	      dtype='>f8')
		  

    >>> orbithist._xpos # The X component of the s/c position vector
	array([ -9869.01716747,  -9874.22968703,  -9879.4421359 ,  -9884.65451437,
	        -9889.86682214,  -9895.07905905,  -9900.29122547,  -9905.50332169,
	        -9910.71534674,  -9915.92730106,  -9921.1391845 ,  -9926.35099672,
	        ... ... ....
	       -11076.34480159, -11081.53981805, -11086.73475384, -11091.92960924,
	       -11097.12438369, -11102.31907782, -11107.51369135, -11112.70822413,
	       -11117.90267637, -11123.09704764, -11128.29133803, -11133.48554772],
	      dtype='>f8')

    >>> orbithist._yvel #The Y component of the s/c velocity vector
	array([-0.07534239, -0.07534906, -0.07535574, -0.07536242, -0.07536909,
	       -0.07537577, -0.07538245, -0.07538912, -0.0753958 , -0.07540248,
	       -0.07540915, -0.07541583, -0.0754225 , -0.07542918, -0.07543586,
	       ... ... ...
	       -0.07687639, -0.07688305, -0.07688971, -0.07689638, -0.07690304,
	       -0.0769097 , -0.07691636, -0.07692303, -0.07692969, -0.07693635,
	       -0.07694301, -0.07694968, -0.07695634, -0.076963  ], dtype='>f8')
		   
    
    >>> orbithist._ra_scx # Right ascension of s/c viewing direction
	array([300.6038247 , 300.68771488, 300.77160933, 300.85550816,
	       300.93941146, 300.97924805, 300.97924805, 300.97924805,
	       300.97924805, 300.97937012, 300.97937012, 300.97937012,
	       ... ... ...
	       300.97943115, 300.97943115, 300.97943115, 300.97943115,
	       300.97943115, 300.97943115, 300.97943115, 300.97943115,
	       300.97943115, 300.97943115, 300.97949219, 300.97949219],
	      dtype='>f8')
	
    >>> orbithist._dec_scz # Declination of the s/c Z-axis
	array([6.66949393, 6.66861575, 6.6677966 , 6.66703648, 6.66633538,
	       6.6748333 , 6.6748333 , 6.6748333 , 6.6748333 , 6.67769432,
	       6.67769432, 6.67769432, 6.67769432, 6.67777777, 6.67777777,
	       ... ... ...
	       6.67777777, 6.67777777, 6.67777777, 6.67777777, 6.67777777,
	       6.67777777, 6.67777777, 6.67777777, 6.67769432, 6.67769432,
	       6.67769432, 6.67769432, 6.67808342, 6.67808342], dtype='>f8')
		   
		   
    >>> orbithist._posangle #Position angle in degree
	array([-83.31257692, -83.31308774, -83.31353566, -83.31392067,
	       -83.31424276, -83.30554264, -83.30554264, -83.30554264,
	       -83.30554264, -83.3026745 , -83.3026745 , -83.3026745 ,
	       ... ... ...
	       -83.3025897 , -83.3025897 , -83.3025897 , -83.3025897 ,
	       -83.3025897 , -83.3025897 , -83.3026761 , -83.3026761 ,
	       -83.3026761 , -83.3026761 , -83.30228349, -83.30228349],
	      dtype='>f8')
   
   
   Regarding the spacecraft frame, we can retrieve it as a |SpacecraftFrame| 
   object:

       >>> integral_frame = orbithist.get_spacecraft_frame()
	   >>> integral_frame[0]
	   <IntegralFrame: 1 frames;
	    obstime=[J2000.000]
	    obsgeoloc=[(-9869017.16747001, 7480682.06699442, 1.52371094e+08) m]
	    obsgeovel=[(-651.56893536, -75.34238658, -490.01369203) m / s]
	    quaternion=[(x, y, z, w) [-0.56344884,  0.35278101, -0.34882014,  0.66060236]]>

   This frame has a location in Earth Inertial Coordinates 
   (``obsgeoloc``), the velocity of the spacecraft with reference to the Earth 
   Inertial Coordinate frame (``obsgeovel``), and the spacecraft orientation
   quaternion, each for a given time stamp (``obstime``).

Now if we define a SkyCoord of some object of interest in RA and Dec:

    >>> coord = SkyCoord(100.0, -30.0, unit='deg')
	
And we can rotate this into the INTEGRAL frame with the following:

	>>> integral_coord = coord.transform_to(integral_frame[0])
	>>> (integral_coord.az,integral_coord.el)
	(<Longitude [142.63112391] deg>, <Latitude [13.75208102] deg>)
	
Now we can tranform to ICRS coordinates:

	>>> integral_coord.icrs
	<SkyCoord (ICRS): (ra, dec) in deg
	    [(100., -30.)]>
	
or Galactic coordinates:
	
	>>> integral_coord.galactic
	<SkyCoord (Galactic): (l, b) in deg
	    [(239.1152521, -15.45266077)]>

or any other coordinate frames provided by Astropy.


Reference/API
=============

.. automodapi:: gdt.missions.integral.orbithist
   :inherited-members:


