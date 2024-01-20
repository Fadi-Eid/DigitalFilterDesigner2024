# DigitalFilterDesign
### V1.1

## Introduction
This repostory contains software for the automatic generation of digital filters.
Version V1.1 contains the algorithm for FIR low-pass filter design written in Python. The algorithm used is the __windowed-sinc__ method for FIR design.
The FIR filter coefficients will be calculated, printed and plotted according to the desired filter specifications such as the cutoff frequency, the transition band width, and the desired attenuation and ripple.

**A MATLAB script is provided to check the filter's characteristics if needed**


## How To Use
To design a low-pass FIR filter, an instance of the class LP_Filter() should be created. The LP_Filter() class constructor requires four parameters that are the desired filter's specifications:
* sampling: The sampling frequency in Hz 
> The sampling frequency should be twice the maximum frequency present in the signal to be filtered.
* cutoff: The desired cutoff frequency in Hz
* transition: The desired transition band width of the filter in Hz
* attenuation: The desired pass-band ripple and stop-band attenuation in dB
> the windowed-sinc method will create a filter with the same ripple in both the pass-band and the stop-band

The methods that can be used with the **__LP_Filter() class__**:
* __LP_Filter.valid()__: Return 1 if the filter is valid and 0 if not.
* __LP_Filter.length()__: Returns the number of coefficients of the designed FIR filter. This method will return 0
if the filter is invalid
* __LP_Filter.delay()__: Returns the filter's group delay (delay added to the original signal) in milliseconds
* __LP_Filter.impulse()__: Return a numpy array containing the designed filter's coefficients

## Errata
V1.1 needs some improvement to cover edge cases such as negative parameters, very large values for the transition bands and other possible bugs.
Future versions should be able to safely handle all possible edge cases and possible failure points.
