import time;
import random;
import sys;
import requests;
import configparser;
#import GPIO # The raspberry Pi GPIO drivers

config = configparser.ConfigParser();

config.read('config.ini')

print('test python app')
print('Python running on version ' + sys.version);
print('Hopefully this is 3.x');


# Get the app parameters from config file

mothershipAddress = 'http://localhost:3000';
mothershipPath = 'push';
pollPeriod = 2;
bogId = config['bog.agent']['AgentID'];

# Check the state of the tilt switch on app running
# Write the state to a variable lastState
lastState = random.randint(0,1);

#Loop every 1s
while True:

	
	print('Checking state of tilt switch');
	#Check the currentState of the tilt switch
	currentState = random.randint(0,1);  #vertical
	print('Found the tilt switch to be in state {}'.format(currentState))
	#If the currentState of the tilt switch has changed compared to lastState
	if(currentState!=lastState):
		#Update the lastState
		lastState=currentState;
		
		#Call the mothership
		print('*******************************************')
		print('About to make an API call to the mothership')
		print('Setting bogId {} to {}'.format(bogId,currentState))
		print('*******************************************')

		payload = {'bogId':bogId, 'currentState':currentState}
		r = requests.post(mothershipAddress + '/' + mothershipPath, data=payload);
		print (r.status_code);
		print (r.text);


	#Else (the currentState hasn't changed, do nothing)
	else:
		print('State has not changed: currentState ({}) still equals lastState ({}) - Doing nothing'.format(currentState,lastState))

	time.sleep(pollPeriod);
	print('');
	print('');

