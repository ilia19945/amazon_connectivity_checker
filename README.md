# amazon_connectivity_checker
Amazon Connectivity check script

Checks connection to amazon connect call center endpoints in case you face the unstable connection from your place to amazon connect endpoints
Async using on Grequests.


To run the script:
1. install python
2. dowload project files
3. create a new folder
4. cd to folder and create and activate venv 
5. pip install import grequests
6. open runme.bat
7. edit path to activate venv and to connectivity_test.py file if needed
8. doubleclick on runme.bat

The script will run on the console there will be an output every min with the results of checking. 
The results will be collected on the .csv file for the current day 
Amazon endpoints are taken from https://www.connect-tools.net/endpoint-test/ -> Chrome Dev console -> Network
