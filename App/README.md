# Introduction
### GUI Features:
1. **Shortcuts**: Many shortcuts are available to facilitate the use of the software.
* **CTRL + D**: Deletes all the values in the input fields
* **CTRL + T**: Toggles between light and dark mode
* **TAB**: Moves focus to the next input field or button
* **CTRL + H**: Opens the documentation in the browser

2. __**Filter Validation**__: After the input fields are all specified, the filter can be validated using the validate button, which open three interactive plots in the browser.
The first plot is the impulse response of the generated filter, the second is the linear plot of the amplitude response, and the third plot is the logarithmic plot of the amplitude response.

3. __**Filter Generation**__: Clicking the generate button will create a .csv file in the same directory of the cloned repo, called coefficients.csv that contains the coefficients of the FIR filter.

4. __**Filter data**__: After validation and/or generation, the filter length and the delay cause by the filter are displayed on the right side on the form.




For the validation of any generated filter, the provided Python code will diplay three plots:

1. **Impulse response + window function**: This plot can be used to visually check the shape of the window function and the sinc shaped impulse response.
1. **Magnitude response (Logarithmic)**: This plot is the most important plot, and should be used to check for the validity of the designed filter by checking the peak amplitude of the first lobe in the stop-band
1. **Magnitude response (Linear)**: This plot can be used to visually check the overall shape of thefrequency response of the filter, the ripple in the pass-band and stop-band, and most importantly, to validate the transition band width.





![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/0df91bc5-6b6b-4194-a81a-8c6dace6d628)
