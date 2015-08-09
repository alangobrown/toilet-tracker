#MockGPIO module

print ("This is the mockGPIO module")

def setmode(mode_type):
	print ('MockGPIO - Mode has been set to ', mode_type)


BCM = 'BCM'


OUT = 'OUT'
IN = 'IN'


def setup(pin, mode_type):
	print ('MockGPIO - pin ', pin, ' setup as ', mode_type)



def output(pin, value):
	print ('MockGPIO - pin ', pin, ' set to ', value)


def input(pin):
	print ('MockGPIO - pin ', pin, ' has been read')
	return True



