# DigitalFilterDesigner 2024
![DIGITAL FILTER DESIGNER](https://github.com/Fadi-Eid/DigitalFilterDesigner2024/assets/113466842/5a0c8081-733b-4910-a24a-2634a2bf702a)

## Current Version: V2.0 - Stable

# Introduction:
**DigitalFilterDesigner 2024** is an open-source project dedicated to simplifying the process of digital linear phase (FIR) filter design. The aim is to facilitate the creation of customizable multiband digital filters with ease of design and implementation.

The current version offers Python code for the automatic design of FIR low-pass filters using two methods: the __**windowed-sinc method**__ and the __**Kaiser adjustable**__ window method and a python API to automatically generate arbitrary gain, multiband FIR filter using the __**weighted least-squares**__ method. The algorithms are written in Python, allowing users to generate filter coefficients by adjusting parameters. After filter generation, the user can utilize the built-in plotting methods to validate the filter magnitude response.

The Least-Squares method, which is the most versatile and general method, is available in GUI form.

# Building from source
The software was tested using **_Python 3.10.6_** but should also work for any python version above 3.10.
Clone this repository on you machine, intsall the required modules listed in _requirements.txt_ file and run the program using the command _**python main.py**_ on Windows and _**python3 main.py**_ on Linux.
For a standalone installation (Might be a little bit slow to load), see below.


# Standalone installation
[Executable](https://drive.google.com/file/d/126CAmOu6LSp0hBe2PsIUMlClEP6Mb2Om/view?usp=sharing)


# Demonstration (V2.0)
[YouTube](https://youtu.be/LXTdjXytBno?si=6UF3J5w3Hi518mu3)

# Video demo (Old version)
[YouTube](https://youtu.be/WzR1Gm4fmk0)

# Repository Structure:
### The repository consists of three main folders:

1. **FIR**: Contains algorithms and methods for linear phase finite impulse response filter design.
2. **App**: Desktop app presenting a user-friendly, code-less interface for FIR design (Least-Squares method).
3. **Media**: Software logo and media-specific files

> Each folder includes a README providing detailed documentation and guidance.

# License:
*MIT License
Copyright (c)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:*

*The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.*

*THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

# Screenshots
![image](https://github.com/Fadi-Eid/DigitalFilterDesigner2024/assets/113466842/f0064b10-096b-4dfe-b6ee-300dc5e948ee)


![image](https://github.com/Fadi-Eid/DigitalFilterDesigner2024/assets/113466842/76ef7e28-3c70-439d-823b-33a964752fd7)



![image](https://github.com/Fadi-Eid/DigitalFilterDesigner2024/assets/113466842/8e486633-400b-48f1-b0a8-a2aae55f5097)





