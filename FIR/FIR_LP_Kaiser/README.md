# LP_Kaiser.py:

## Introduction
This Python script generates the coefficients for a Low Pass Finite Impulse Response (FIR) filter using the Kaiser window method. The Kaiser window is an adjustable window adjustable using a parameter \beta. This parameter is automatically computed to provide a frequency response that approximates the response specified by the user.


## Usage
**Set user-defined variables**:

- `sampling`: Sampling rate in samples per second (Hz).
- `cutoff`: Cutoff frequency of the filter in Hertz.
- `transition`: Transition band width in Hertz.
- `attenuation`: Desired attenuation in decibels.

```python
# User-defined variables
sampling = 2000         # Sampling rate in samples/s or Hz
cutoff = 300            # Cutoff frequency in Hz
transition = 80         # Transition band width in Hz
attenuation = 72        # Attenuation in dB
```

**Instantiate an LP_Filter object with the specified parameters**:

```python
lowPass = LP_Filter(attenuation, transition, cutoff, sampling)
```
**Generate the filter coefficients using the impulse method:

```python
h = lowPass.impulse()
```

**Optionally, inspect the filter characteristics**:

```python
# Print coefficients
for i in h:
    print(f"{i}, ")

# Print filter's length and group delay
print(f"The number of coefficients is {lowPass.length()}")
print(f"The delay of this filter is {lowPass.GroupDelay()} ms")
```

## Dependencies
- `numpy`: Used for numerical operations and array manipulations.
- `matplotlib`: Used for plotting the impulse response and frequency response.

### Make sure to install the dependencies using:
```bash
pip install numpy matplotlib
```

## Validation Code
The validation code below the user code section provides visualizations of the filter's impulse response and frequency response.