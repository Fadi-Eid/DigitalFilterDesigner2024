# Introduction
### Two algorithms are used for the generation of FIR low-pass filters:
1. **__windowed-sinc method__**: This method is used to generate the FIR filter's impulse response (coefficients) by truncating the shifted ideal response using one of five pre-defined window functions (Rectangular, Barlett, Hamming, Hann, Blackman) each having their own advantages and disadvantages. This method will generate a filter that will often exceed the specifications, such as the stop-band minimum attenuation, which makes it a safe option, but will result in far from optimal number of coefficients, which is sometimes not desired due to the delay introduced

1. __**Kaiser Adjustable window method**__: This method makes use of the Kaiser adjustable window, which is controlled by a variable "beta". This method is a sub-optimal method and will result in a filter whose specifications are very close to what is needed thus, lowering the number of coefficients needed, which in turns, decreases the delay cause by the filter.
The disatvantages of this method is that for large attenuation values, the generated filter's stop-band attenuation may be less than, but very close to the desired attenuation. This requires a validation effort from the user part.
> For attenuation values > 60dB, validation is recommended for critical applications.

For the validation of any generated filter, the provided Python code will diplay three plots:
1. **Impulse response + window function**: This plot can be used to visually check the shape of the window function and the sinc shaped impulse response.
1. **Magnitude response (Logarithmic)**: This plot is the most important plot, and should be used to check for the validity of the designed filter by checking the peak amplitude of the first lobe in the stop-band
1. **Magnitude response (Linear)**: This plot can be used to visually check the overall shape of thefrequency response of the filter, the ripple in the pass-band and stop-band, and most importantly, to validate the transition band width.
> The validation process will be outlined later in this document.


# Code Structure (**__FIR_WinSinc.py)__**

This Python code generates the coefficients of a Low Pass FIR (Finite Impulse Response) filter using the windowed-sinc method. The designed filter's impulse response is computed, and its magnitude response is plotted for validation.

## Modules
- `math`: Provides mathematical functions.
- `numpy`: Used for numerical operations.
- `matplotlib.pyplot`: Enables plotting.

## Constants
- `PI`: Mathematical constant π.

## Window Function Types
- `RECTANGULAR = 0`
- `BARLETT = 1`
- `HANN = 2`
- `HAMMING = 3`
- `BLACKMAN = 4`

## Window Class
### Properties
- `attenuation`: Peak approximation error in dB.
- `transition`: Transition band width in radians per second.
- `winFunc`: Window function type.
- `L`: Window length.
- `M`: Filter order.

### Methods
- `window()`: Generates and returns the window function based on the specified window type.

## LP_Filter Class (Inherits from Window)
### Properties
- `cutoff`: Cutoff frequency in radians per second.
- `length`: Number of filter coefficients.
- `sampling`: Sampling rate in samples per second.
- `valid`: Flag indicating the validity of input parameters.

### Methods
- `impulse()`: Computes and returns the impulse response of the filter.
- `delay()`: Computes and returns the group delay of the filter.

## User-Defined Variables
- `sampling`: Sampling rate in samples per second.
- `cutoff`: Cutoff frequency of the filter in Hz.
- `transition`: Transition band width in Hz.
- `attenuation`: Attenuation in dB.

## Filter Generation and Validation 
- `lowPass`: Instance of the LP_Filter class representing the low-pass filter.

- Impulse response and window function are plotted if the filter is valid.
- Coefficients, filter length, and group delay are printed for validation.
- Frequency response (magnitude) is plotted in both logarithmic and linear scales.


# Code Structure (**__FIR_Kaiser.py__**)

This Python code implements the design of a Low Pass FIR (Finite Impulse Response) filter using the Kaiser window method. The Kaiser window is utilized for its configurability, allowing users to adjust the filter specifications through parameters such as attenuation, transition bandwidth, and sampling frequency. The Kaiser window method is known for producing filters with a reduced number of coefficients, thus minimizing filter delay. The validation of the generated filter is facilitated through plots of the impulse response and magnitude response.


## Kaiser Class
### Properties
- `attenuation`: Desired attenuation in dB.
- `transition`: Transition bandwidth in Hz.
- `sampling`: Sampling rate in samples per second.
- `beta`: Kaiser window parameter.
- `N`: Window length.
### Methods
- `zeroth_bessel(x)`: Computes the zeroth-order modified Bessel function of the first kind.
- `window()`: Generates and returns the Kaiser window.

## LP_Filter Class (Inherits from Kaiser)
### Properties
- `valid`: Flag indicating the validity of input parameters.
- `cutoff`: Cutoff frequency in Hz.
### Methods
- `impulse()`: Computes and returns the impulse response of the filter.
- `delay()`: Computes and returns the group delay of the filter (in seconds).
- `length()`: Returns the number of filter coefficients.
### User-Defined Variables
- `sampling`: Sampling rate in samples per second.
- `cutoff`: Cutoff frequency of the filter in Hz.
- `transition`: Transition band width in Hz.
- `attenuation`: Attenuation in dB.
### Filter Generation and Validation
- `lowPass`: Instance of the LP_Filter class representing the low-pass filter.
> Filter coefficients, delay, and length are printed for validation.
> Impulse response and magnitude response are plotted for visual validation.


# Usage
```python
# Example Usage
sampling = 2000
cutoff = 500
transition = 50
attenuation = 30

lowPass = LP_Filter(attenuation, transition, cutoff, sampling)

h = lowPass.impulse()
w = lowPass.window()
```
# Validation Guide
The generated Python plots can be used to validate the generated filters.

Using the logarithmic magnitude response plot, the attenuation in the stop-band can be validated by checking the peak amplitude of the lobes in the stop-band region. Note that the side lobes should exist after the cutoff frequency + half the transition band width.
e.g., for Fs=2000Hz, Fc=500Hz and transition=50Hz, the side lobe should exist at frequencies > (500 + 25).

![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/da0c3af8-be2c-4c1f-ac28-128af42591fc)




Using the linear magnitude response plot, the transition band width and the cutoff frequencies can be validated. The amplitude should be 0.5 at the cutoff frequency, and the transition band should be in the linear transition region.

![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/21cb4e94-f722-4e42-8997-91a200164bb8)

