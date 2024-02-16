# Introduction
### Three algorithms are used for the generation of FIR low-pass filters:
1. **__windowed-sinc method__**: This method is used to generate the FIR filter's impulse response (coefficients) by truncating the shifted ideal response using one of five pre-defined window functions (Rectangular, Barlett, Hamming, Hann, Blackman) each having their own advantages and disadvantages. This method will generate a filter that will often exceed the specifications, such as the stop-band minimum attenuation, which makes it a safe option, but will result in far from optimal number of coefficients, which is sometimes not desired due to the delay introduced

2. __**Kaiser Adjustable window method**__: This method makes use of the Kaiser adjustable window, which is controlled by a variable "beta". This method is a sub-optimal method and will result in a filter whose specifications are very close to what is needed thus, lowering the number of coefficients needed, which in turns, decreases the delay cause by the filter.
The disatvantages of this method is that for large attenuation values, the generated filter's stop-band attenuation may be less than, but very close to the desired attenuation. This requires a validation effort from the user part.
> For attenuation values > 60dB, validation is recommended for critical applications.

3. __**Weighted least-squares method**__: This method consists of finding the optimal filter coefficients in the least-squares sense, by solving a linear system of equations. This method provide fewer filter coefficients for the same filter specifications compared to the windowed-sinc and the kaiser adjustable window methods, while also allowing for a high order filter to be designed (attenuation > 160dB and/or narrow transition band).
> The behavior in the transition band is not specified thus, should be validated. It is possible for the transition band to behave badly for filters with extreme parameters.
> Transition band may need to be narrowed (by adjusting the parameters) if it is larger than specified in the designed filter.
> Maximum attenuation that can be acheived using this filter is ~170dB, values greater than this value "can" be reached, but require tweaking (by trial and error) to value of the weight "K", as well as the calculations that determines the filter's order.

For the validation of any generated filter, the provided Python code will diplay three plots:
1. **Impulse response + window function**: This plot can be used to visually check the shape of the window function and the sinc shaped impulse response.
1. **Magnitude response (Logarithmic)**: This plot is the most important plot, and should be used to check for the validity of the designed filter by checking the peak amplitude of the first lobe in the stop-band
1. **Magnitude response (Linear)**: This plot can be used to visually check the overall shape of thefrequency response of the filter, the ripple in the pass-band and stop-band, and most importantly, to validate the transition band width.
> The validation process will be outlined later in this document.


# Usage
### Create filter instance
```python
sampling = 2000
cutoff = 500
transition = 50
attenuation = 30

lowPass = LP_Filter(attenuation, transition, cutoff, sampling)
```
## Main methods:
### Save the filter coefficients (coefficients.csv)
```python
lowPass.SaveCoeffs()
```
### Validation plots
```python
lowPass.PlotImpulse()
lowPass.PlotAmplitudeLinear()
lowPass.PlotAmplitudeLog()
```

### Useful data about filter
```python
lowPass.Length()
lowPass.Delay()
lowPass.MSE()
```

# Validation Guide
The generated Python plots can be used to validate the generated filters.

Using the logarithmic magnitude response plot, the attenuation in the stop-band can be validated by checking the peak amplitude of the lobes in the stop-band region. Note that the side lobes should exist after the cutoff frequency + half the transition band width.
e.g., for Fs=2000Hz, Fc=500Hz and transition=50Hz, the side lobe should exist at frequencies > (500 + 25).


![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/da0c3af8-be2c-4c1f-ac28-128af42591fc)




Using the linear magnitude response plot, the transition band width and the cutoff frequencies can be validated. The amplitude should be 0.5 at the cutoff frequency, and the transition band should be in the linear transition region.

![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/21cb4e94-f722-4e42-8997-91a200164bb8)


# License
This code is provided under the MIT License. Feel free to use and modify it for your purposes.
