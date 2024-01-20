# DigitalFilterDesign
### V1.1


## Introduction
This repostory contains software for the automatic generation of digital filters.
Version V1.1 presents an algorithm for FIR low-pass filter design, and is written in Python. The algorithm used is the __windowed-sinc__ method.
The FIR filter's coefficients will be calculated, printed and plotted according to the desired filter specifications such as the cutoff frequency, the transition band width, and the desired attenuation and ripple.

**A MATLAB script is also provided to check anf validate the filter's characteristics if needed**

![matlab_frequency_response](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/6af83828-c50a-451b-a067-8e62ad76c57b)

**The example code in Python will generate a visual plot of the generated impulse response, as well as the window function used.**

![python_plot](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/ee0287c6-48da-458c-aaee-46437fc7c4ae)


## How To Use
To design a low-pass FIR filter, an instance of the class LP_Filter() should be created. The LP_Filter() class constructor requires four parameters that represemt the desired filter's specifications:
* sampling: The sampling frequency in Hz 
> The sampling frequency should be twice the maximum frequency present in the signal to be filtered.
* cutoff: The desired cutoff frequency in Hz, the frequencies above the cutoff frequency will be filtered.
* transition: The desired transition band width of the filter in Hz. The lower this value, the sharper the transition from the pass-band to the stop-band.
* attenuation: The desired pass-band ripple and stop-band attenuation in dB.
> the windowed-sinc method will create a filter with the same ripple in both the pass-band and the stop-band
> 
![python_code](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/40893112-d8aa-4107-b74a-327d6b8371a1)

The methods that can be used with the **__LP_Filter() class__**:
* __LP_Filter.valid()__: Returns 1 if the filter is valid and 0 if not.
* __LP_Filter.length()__: Returns the number of coefficients of the designed FIR filter. This method will return 0 if the filter is invalid.
* __LP_Filter.delay()__: Returns the filter's group delay (delay added to the original signal) in milliseconds
* __LP_Filter.impulse()__: Returns a numpy array containing the designed filter's coefficients


## Future Releases
Future releases will include:
* Bugs fix
* New methods for FIR filter design
* Design of IIR filters
* Design of IIR and FIR filters of different types (high-pass, band-pass, band-stop)
* User interface in the form of a desktop app
* Automatic C code generation for embedded systems