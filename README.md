# amazon_connectivity_checker
Amazon Connectivity check script

Checks connection to amazon connect call center endpoints in case you face the unstable connection from your place to amazon connect endpoints.
It takes the worst responce time as a set of 10 requests to the url.
If there oneof the attemps is failed - it adds "cound't ping" to the log .csv file

Async using on Grequests.


To run the script:
1. install python
2. download project files
3. create a new folder
4. move all files and cd to folder
5. create and activate venv 
6. pip install import grequests
7. open runme.bat
8. edit path to activate venv and to connectivity_test.py file if needed
9. doubleclick on runme.bat to run the script continuosly on cmd

There will be an output every min with the results of checking in the console + the result will be added to the .csv file for the current day.

Amazon endpoints are taken from https://www.connect-tools.net/endpoint-test/ -> Chrome Dev console -> Network
