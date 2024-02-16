# DigitalFilterDesign
## Current Version: V1.4

# Introduction:
**DigitalFilterDesign** is an open-source project dedicated to simplifying the process of digital filter design. The aim is to facilitate the creation of customizable digital filters with ease of design and implementation.

The current version offers Python code for the automatic design of FIR low-pass filters using three methods: the __**windowed-sinc method**__, the __**Kaiser adjustable**__ window method and the __**weighted least-squares**__ method. The algorithms are written in Python, allowing users to generate filter coefficients by adjusting parameters. After filter generation, the frequency domain magnitude response (linear and logarithmic) is displayed alongside the time domain impulse response for validation.

The Least-Squares method, which is the most performant method, is available in GUI form.

Additionally, a MATLAB code is provided for further analysis (optional validation).

# Repository Structure:
### The repository consists of three main folders:

1. **FIR**: Contains algorithms and methods for linear phase finite impulse response filter design.
2. **IIR**: Contains algorithms and methods for recursive infinite impulse response filter design.
3. **App**: Desktop app presenting a user-friendly, code-less interface for FIR design (Least-Squares method).

> Each folder includes a README providing detailed documentation and guidance

# Future Releases:
In addition to optimization, improvements, and bug fixes, upcoming releases are planned as follows:

* **V1.1** : Low-pass FIR design using the windowed-sinc method.
* **V1.2**:  Low-pass FIR design using the Kaiser adjustable window.
* **V1.3**: Optimal FIR filter design API using the Least-Squares method.
* **V1.4** __(Current)__: GUI for FIR filter generation using the Least-Squares method.
* **V1.5** : Optimal FIR filter design API using the Parks-McClellan iterative method.
* **V2.0**: IIR filter design.
* **V2.1**: __(No specific plans outlined yet)__
* **V3.0**: Implementation of the complete desktop interface (App).

# Screenshots

![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/0a990d04-e96a-4c20-b4c4-01e17451362c)



![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/4c61a98b-3fa5-4030-b146-67e3712b45cf)



![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/7051e0f1-b517-453f-8b1c-e8f48ba44d91)



![image](https://github.com/Fadi-Eid/DigitalFilterDesign/assets/113466842/b1b66916-b96e-47c0-acf2-c619b1fb0ec9)


