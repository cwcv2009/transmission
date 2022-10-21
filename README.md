# Transmission

## Instructions for download

#### Using github.com
1. Using the same browser you logged into your github account with navigate to the following URL: `https://github.com/cwcv2009/transmission.git`
2. On the repository github page click on the green code button.
3. In the drop-down menu click download ZIP
4. Navigate to the folder the ZIP was downloaded
5. Unzip the file
+ You should now see a **transmission-master** directory containing all the repository files

#### Using computer terminal
1. Using your local terminal, navigate to your user desktop
2. Create a new directory called **transmission**
3. Navigate to the new directory
4. Using the Git utility, run `git init`
5. Using the Git utility, run `git clone https://github.com/cwcv2009/transmission.git`
+ You now have downloaded the transmission repository inside your **transmission** directory

## Instruction for use



1. Using you local terminal, navigate to the directory you downloaded the transmission repository to (if you followed the instructions for download then you will navigate to your **transmission** or **transmission-master** directory on your user computer).
2. Using the Python compiler, run either `python modulation.py` or `pythonn3 modulation.py`
3. If the command executed successfully you should be promted to **Enter message:**
4. type in a message and hit enter/return
+ You should now see an *iqData.fc32* file in the present working directory.
+ A file with an extension of .fc32 is an executable file that produces a waveform using a software defined radio. If a receiving software defined radio listens for the same preamble signal at the same frequency then the message you entered will be recieved and output to the user. Continue to simulate the process.
5. In the same directory run `python demodulation.py` or `python3 demodulation.py`
6. Notice that you message you entered earlier is out put to the terminal.
