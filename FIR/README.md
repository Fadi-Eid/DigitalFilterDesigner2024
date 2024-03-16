# Introduction
### Two algorithms are used for the generation of FIR low-pass filters:
1. **__windowed-sinc method__**: This method is used to generate the FIR filter's impulse response (coefficients) by truncating the shifted ideal response using one of five pre-defined window functions (Rectangular, Barlett, Hamming, Hann, Blackman) each having their own advantages and disadvantages. This method will generate a filter that will often exceed the specifications, such as the stop-band minimum attenuation, which makes it a safe option, but will result in far from optimal number of coefficients, which is sometimes not desired due to the delay introduced

2. __**Kaiser Adjustable window method**__: This method makes use of the Kaiser adjustable window, which is controlled by a variable "beta". This method is a sub-optimal method and will result in a filter whose specifications are very close to what is needed thus, lowering the number of coefficients needed, which in turns, decreases the delay cause by the filter.
The disatvantages of this method is that for large attenuation values, the generated filter's stop-band attenuation may be less than, but very close to the desired attenuation. This requires a validation effort from the user part.
> For attenuation values > 60dB, validation is recommended for critical applications.

### One algorithm is used for the generation of multiband filters:
1. __**Weighted least-squares method**__: This method consists of finding the optimal filter coefficients in the least-squares sense, by solving a linear system of equations. This method provide fewer filter coefficients for the same filter specifications compared to the windowed-sinc and the kaiser adjustable window methods, while also allowing for a high order filter to be designed (attenuation > 160dB and/or narrow transition band).
> The behavior in the transition band is not specified thus, should be validated. It is possible for the transition band to behave badly for filters with extreme parameters.
> Transition band may need to be narrowed (by adjusting the parameters) if it is larger than specified in the designed filter.
> Maximum attenuation that can be acheived using this filter is ~170dB, values greater than this value "can" be reached, but requires trial and error tweaking.


For the validation of any generated filter, the provided Python APIs can diplay three plots:
1. **Impulse response**: This plot can be used to visually check the shape of the impulse response.
1. **Magnitude response (Logarithmic)**: This plot is the most important plot, and should be used to check for the validity of the designed filter by checking the peak amplitude of the first lobe in the stop-band
1. **Magnitude response (Linear)**: This plot can be used to visually check the overall shape of thefrequency response of the filter, the ripple in the pass-band and stop-band, and most importantly, to validate the transition band width.
> The validation process will be outlined later in this document.


# Usage (Windowed-Sinc & Kaiser methods)
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

# Usage (Optimal Least-Squares method)
The process of designing a filter with the specs below will be demonstrated.
![image](https://github.com/Fadi-Eid/DigitalFilterDesigner2024/assets/113466842/2c4b2f14-423a-4438-9d1b-f91a1d4cf53e)

### Set the desired sampling frequency
```python
Fs = 2200
```
> Note: This should be double the highest frequency of the filter to be generated
### Set the filter length (odd)
```python
Length = 501
```
> If an even number is used, it will be incremented by 1 to make it odd.
> This value should be calculated based on trial and error, the tighter the transition band and the higher the desired stop-band attenuation, the higher this value should be.
### Specify the band edges frequency values (see example)
```python
band_edges = [0, 500, 505, 720, 730, 1100]
```
### Specify the band edges frequency values (see example)
```python
band_edges = [0, 500, 505, 720, 730, 1100]
```
### Specify the desired value for each band edge
```python
desired_gain = [2, 2, 0, 0, 1.6, 1.6]
```
### Specify the weight for each band
```python
weights = [1, 2, 1]
```
> The weight represent how important is the band relative to the others. In the case of this example, the second band, which is a zero-gain band, is specified to be the most important by giving it a higher weight relative to the other bands.
> If no weights array is passed, the class will assume an all-ones weights array, giving all the bands equal importance.
> Usually, zero-gain bands are given higher weights to obtain the maximum possible attenuation.

### Complete code
```python
Fs = 4000
Length = 501
band_edges = [0, 500, 505, 720, 730, 1100]
desired_gain = [2, 2, 0, 0, 1.6, 1.6]
weights = [1, 2, 1]
Filter = FIR_Filter(Fs, Length, band_edges, desired_gain, weights)
```

# Methods
### Method to plot the linear amplitude response of the generated filter
```python
Filter.PlotAmplitudeLinear()
```
### Method to plot the logarithmic amplitude response of the generated filter
```python
Filter.PlotAmplitudeLogarithmic()
```
### Method to plot the logarithmic time-domain amplitude response of the generated filter (Coefficients)
```python
Filter.PlotImpulse()
```
### Method to print the generated filter coefficients to the console
```python
Filter.PrintCoeffs()
```
### Method to save the generated filter coefficients in a CSV file
```python
Filter.SaveCoeffs(path)
```
### Method to provide a health score based on the transition bands mean-squared-error compared to the ideal linear transition
```python
Filter.HealthScore()
```
### Method to compute the group delay of the generated filter
```python
Filter.Delay()
```

# Validation Guide
The generated Python plots can be used to validate the generated filters.

Using the logarithmic magnitude response plot, the attenuation in the stop-band can be validated by checking the peak amplitude of the lobes in the stop-band region. Note that the side lobes should exist after the cutoff frequency + half the transition band width.
e.g., for Fs=2000Hz, Fc=500Hz and transition=50Hz, the side lobe should exist at frequencies > (500 + 25).


![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/da0c3af8-be2c-4c1f-ac28-128af42591fc)



Using the linear magnitude response plot, the transition band width and the cutoff frequencies can be validated. The amplitude should be 0.5 at the cutoff frequency, and the transition band should be in the linear transition region.

![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/21cb4e94-f722-4e42-8997-91a200164bb8)


