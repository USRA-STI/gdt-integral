.. _integral-spi_acs:


*****************************************************************
Integral SPI_ACS Data (:mod:`gdt.missions.integral.spi.spi_acs`)
*****************************************************************
The INTEGRAL SPI-ACS lightcurve can be downloaded from INTEGRAL website
`MMODA <https://www.astro.unige.ch/mmoda>`_ or using INTEGRAL OSA 
`software <https://www.isdc.unige.ch/integral/analysis>`_. In MMODA, users can 
provide the source information to download the desired lightcurve. Here, for 
example we have choosen GRB 230307A between time interval UT 
2023-03-07 15:41:11.000 to UT 2023-03-07 15:50:11.000.
 
 .. image:: figs/MMODA.png
 
It will download the lightcurve "spiacs_lc_query-3.fits"

Let's open a lightcurve file:

	>>> from gdt.missions.integral.spi.spi_acs import Spi_acs
	>>> from gdt.core import data_path
	>>> filepath = data_path.joinpath('integral/spiacs_lc_query-3.1.fits')
    >>> acs = spi_acs.open(filepath)
    >>> type(acs)
	<spi_acs(filename="spiacs_lc_query-3.fits") at 0x16923c170>

We can plot the lightcurve:

	>>> import matplotlib.pyplot as plt
	>>> from gdt.core.plot.lightcurve import Lightcurve
	>>> lcplot = Lightcurve(acs.to_lightcurve(), interactive=True)
	>>> plt.show()
	
 .. image:: figs/spi_acs.png

The data and the headder information can also be accessed 

    >>> acs.mjdref #Reference MJD
	51544.0
	
    >>> acs.obsdate
    '2023-03-07 15:41:11.005'
	
	>>> acs.obsdateend
	'2023-03-07 15:50:11.005'
	
	>>> acs.rates
	array([90360.        , 91586.66666667, 90620.        , ...,
	       89660.        , 91300.        , 90860.        ], dtype='>f8')
		   
	>>> acs.time
	array([-269.95016806, -269.82516779, -269.70016784, ...,  269.75016788,
	        269.85016828,  269.95016774], dtype='>f8')
	
	
	
For more details about working with the data, see	
See :external:ref:`The Binning Package
<binning>` and 
:external:ref:`Plotting Lightcurves <plot-lightcurve>`, 

=============

.. automodapi:: gdt.missions.integral.spi.spi_acs
   :inherited-members:


