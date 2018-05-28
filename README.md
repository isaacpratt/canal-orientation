# canal-orientation
Measure the orientation of vascular canals in cortical bone

This project was created by Isaac Pratt between 2013 and 2018 and for a doctoral thesis. It is based on a previous set of macros created by Dr. David Cooper and used in (Britz et al, 2012). This project updates those macro to measure the 3D orientation of canals in cortical bone. For full details on how the macros function see (Pratt & Cooper, 2017) and (Pratt et al, 2018).

This repository contains the following files:

1) The macro itself - Measure 3D orientation-v1.3.5.txt

The macro is written using the imageJ script language and can be run in imageJ or in FIJI. The macro is tested and working in imageJ version 1.49u

The macro functions on lineset files produced in Amira, and can be used to subsample lineset files directly. Alternatively, if large lineset files are produced, the python subsampler below can be used. The macro requires a canal skeleton lineset and a bone centroid lineset, which can be calculated using the centroid macro provided or using the centroid function in the macro itself.

2) The python subsampler script - subsampler-v2-folder.py

This script runs in python 2 and is tested and working in python version 2.7.1.3. This script will automatically subsample lineset files in a folder. The line segment length parameter must be set directly in the script file.

3) The excel macro - PivotTable Excel macro.txt

This excel macro is tested and working in Excel 16.13.1 on the Mac platform. It takes the csv file produced by the imageJ macro and creates a pivot table with values for the Laminar, Radial, and Longitudinal indices as calculated in (Pratt et al, 2018).

4) Example canal lineset - rat_tibia_canals.lineset

This lineset is data used in (Pratt et al, 2017) and is provided as a formatting example for testing and troubleshooting.

5) Example centroid lineset - rat_tibia_centroid.lineset

This lineset is data used in (Pratt et al, 2017) and is provided as a formatting example for testing and troubleshooting.

References:

Britz, H.M. et al., 2012. The effects of immobilization on vascular canal orientation in rat cortical bone. J Anat, 220(1), pp.67–76.

Pratt, I.V. & Cooper, D.M.L., 2017. A method for measuring the three-dimensional orientation of cortical canals with implications for comparative analysis of bone microstructure in vertebrates. Micron, 92, pp.32–38.

Pratt, I.V. et al., 2018. Interpreting the three-dimensional orientation of vascular canals and cross-sectional geometry of cortical bone in birds and bats. J Anat, 14(Pt 5), p.S13.
