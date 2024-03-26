.. _integral-frame:

********************************************************
Integral Spacecraft Frame (:mod:`gdt.missions.integral.frame`)
********************************************************

The  Integral spacecraft frame, | IntegralFrame |, is the frame that is aligned
with the Integral spacecraft coordinate frame, and is represented by a 
quaternion that defines the rotation from spacecraft coordinates to the ICRS
coordinate frame.  This frame takes advantage of the Astropy coordinate frame
design, so we can use the IntegralFrame to convert Astropy SkyCoord objects 
between the IntegralFrame and any celestial frame.

The IntegralFrame is initialized when reading from a mission 
orbit history file (e.g. |OrbitHist|).



Reference/API
=============

.. automodapi:: gdt.missions.integral.frame
   :inherited-members:


