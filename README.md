# PulseDetect 
 
**PulseDetect** is a tool for real-time audio frequency detection using Python and associated libraries like numpy, pyaudio, and scipy. This program allows you to record audio and display the dominant frequency present in the sound. 
 
## Features 
- Record audio from the microphone for a specified duration 
- Compute and display the dominant frequency in the audio 
- Simple command-line interface 
 
## Installation 
- **Install Required Libraries**: Use pip to install the necessary libraries: 
```bash 
pip install numpy pyaudio scipy 
``` 
 
- **Download or Clone the Project**: 
```bash 
git clone https://github.com/nomadsdev/pulse-detect.git 
cd PulseDetect 
``` 
 
## Usage 
You can use PulseDetect via the command line with the following options: 
 
- `-f` : Enable frequency detection 
- `-t` : Duration for frequency detection (in seconds), default is 1 second 
 
### Example Usage
- **Detect Audio Frequency**: 
```bash 
python main.py -f -t 2 
``` 
This command will start recording audio for 2 seconds and display the dominant frequency. 
 
- **General Usage**: If `-f` is not specified, the program will display a warning message and will not start frequency detection: 
```bash 
python main.py 
``` 
 
## File Structure
- `main.py`: Main file for frequency detection 
- `README.md`: This document 
 
## Contributing
If you'd like to contribute to this project, you can open an issue or submit a pull request with your improvements or bug fixes. 
 
## Contact 
 
For any questions or suggestions, please contact support@jmmentertainment.com
