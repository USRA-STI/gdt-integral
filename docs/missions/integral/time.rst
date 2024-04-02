.. _integral-time:


*****************************************************************
Integral Mission Epoch  (:mod:`gdt.missions.integral.time`)
*****************************************************************

The Integral Mission epoch, also called the Integral Mission Elapsed Time (MET) is 
the number of seconds elapsed since 2000-01-01 00:00:00.000 TT, including 
leap seconds.  We have defined a specialized epoch to work with Astropy ``Time``
objects so that Integral MET can be easily converted to/from other formats and time
scales.

To use this, we simply import and create an astropy Time object with a `'integral'`
format:

    >>> from gdt.missions.integral.time import Time
    >>> integral_met = Time(761461614, format='integral')
    >>> integral_met
    <Time object: scale='tt' format='integral' value=761461614.0>
    
Now, say we want to retrieve the GPS timestamp:

    >>> integral_met.gps
    1392181562.816
	

The Astropy ``Time`` object readily converts it for us. We can also do the 
reverse conversion:

    >>> gps_time = Time(integral_met.gps, format='gps')
    >>> gps_time
    <Time object: scale='tai' format='gps' value=1392181562.816>
    
    >>> gps_time.integral
    761461614.0

And we should, of course, get back the Integral MET we started with.  This enables
you do do any time conversions already provided by Astropy, as well as time
conversions between other missions within the GDT.

In addition to time conversions, all time formatting available in Astropy is 
also available here.  For example, we can format the Integral MET in ISO format:

    >>> integral_met.iso
    '2024-02-17 05:06:54.000'
    

    
Reference/API
=============

.. automodapi:: gdt.missions.integral.time
   :inherited-members:


