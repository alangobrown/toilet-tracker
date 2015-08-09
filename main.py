import time;
import random;
import sys;
import requests;
import configparser;
import json;



#import GPIO # The raspberry Pi GPIO drivers

config = configparser.ConfigParser();

config.read('config.ini')

print('test python app')
print('Python running on version ' + sys.version);
print('Hopefully this is 3.x');


# Get the app parameters from config file

firebaseAddress = 'https://alans-project-loo.firebaseio.com';
firebasePath = 'bogs';
pollPeriod = 2;
bogId = config['bog.agent']['AgentID'];





# Check the state of the tilt switch on app running
# Write the state to a variable lastState
lastState = requests.get(firebaseAddress + '/' + firebasePath + '/' + bogId + '.json');
print ('Checking the initial state....');
lastState = lastState.json();
print (lastState['currentState']);


# print('The last state for bog {} is {}', format(bogId,lastState))
lastState = random.randint(0,1);

#Loop every 1s
while True:

	
	print('Checking state of tilt switch');
	#Check the currentState of the tilt switch
	currentState = random.randint(0,1);  #vertical
	if currentState==1:
		currentState = 'open'
	else:
		currentState = 'closed'

	print('Found the tilt switch to be in state {}'.format(currentState),{})
	#If the currentState of the tilt switch has changed compared to lastState
	if(currentState!=lastState):
		#Update the lastState
		lastState=currentState;
		
		#Call firebase
		print('*******************************************')
		print('About to make an API call to firebase')
		print('Setting bogId {} to {}'.format(bogId,currentState))
		print('Posting to {}'.format(firebaseAddress + '/' + firebasePath + '/' + bogId + '.json'));
		print('*******************************************')

		payload = {'currentState':currentState}; 
		result = requests.patch(firebaseAddress + '/' + firebasePath + '/' + bogId + '.json', data=json.dumps(payload))
		print (result)


	#Else (the currentState hasn't changed, do nothing)
	else:
		print('State has not changed: currentState ({}) still equals lastState ({}) - Doing nothing'.format(currentState,lastState))

	time.sleep(pollPeriod);
	print('');
	print('');

