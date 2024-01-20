# DigitalFilterDesign
### V1.0

## Introduction
This repostory contains software for automatic generation of digital filters, at this point
the algorithm for FIR filter design using the windowed-sinc method had been implemented 
in Python. The code will generate the FIR filter coefficients according to the filter specifications
defined in the code.

** A MATLAB code is provided to check the filter's characteristics if needed **

## How To Use
To use the Python script for FIR filter design, the LP_Filter() class takes in only 4 parameters which are:
* sampling: The sampling frequency in Hz
* cutoff: The desired cutoff frequency in Hz
* transition: The desired transition band width of the filter in Hz
* attenuation: The desired pass-band ripple and stop-band attenuation in dB

After an instance of the LP_Filter() class had been created, the following are the methods that can be used:
* LP_Filter.valid(): Used to check if the filter specs can be achieved (1=valid, 0=invalid)
* LP_Filter.length(): Returns the number of coefficients of the designed FIR filter. This method will return 0
if the filter is invalid
* LP_Filter.delay(): Returns the filter's group delay (delay added to the original signal) in milliseconds
* LP_Filter.impulse(): Return a numpy array containing the designed filter's coefficients

## Errata
V1.0 cannot handle negative values for the parameters, and will produce incorrect results if the transition
band extends above the Nyquist frequency.
Some improvement should be made to hande edge cases and to fix bugs.
