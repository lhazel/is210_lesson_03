Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
What is your blood pressure?  
>>> 
>>> raw_input('What is your blood pressure?  ')
What is your blood pressure?  125
'125'
>>> BP_STATUS = int( raw_input("What is your blood pressure?  "))
What is your blood pressure?  125
>>> BP_STATUS
125
>>> BP_STATUS = 125
>>> ================================ RESTART ================================
>>> BP_STATUS

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    BP_STATUS
NameError: name 'BP_STATUS' is not defined
>>> raw_input('What is your blood pressure?  ')
What is your blood pressure?  125
'125'
>>> BP_STATUS = int( raw_input("What is your blood pressure?  "))
What is your blood pressure?  125
>>> BP_STATUS
125
>>> 
if BP_STATUS > 89 or BP_STATUS < 120:
	print "Blood pressure is ideal."
elif BP_STATUS > 120 or  BP_STATUS < 140:
	print "Blood pressure is warning."
else BP_STATUS > 140 or BP_STATUS <= 159:
	
SyntaxError: invalid syntax
>>> if BP_STATUS > 89 or BP_STATUS < 120:
	print "Blood pressure is ideal."
elif BP_STATUS >120 or BP_STATUS < 140:
	print "Blood Pressure is warning."
print ('Your blood pressure is {}'.format(BP_STATUS))
SyntaxError: invalid syntax
>>> if BP_STATUS > 89 or BP_STATUS < 120:
	print "Blood pressure is ideal."
elif BP_STATUS >120 or BP_STATUS < 140:
	print "Blood Pressure is warning."
print ('Your blood pressure is {}'.format(BP_STATUS))
SyntaxError: invalid syntax
>>> if BP_STATUS > 89 or BP_STATUS < 120:
	print "Blood pressure is ideal."
elif BP_STATUS >120 or BP_STATUS < 140:
	print "Blood Pressure is warning."
print ('Your blood pressure is {}' .format(BP_STATUS))
SyntaxError: invalid syntax
>>> if BP_STATUS > 89 or BP_STATUS < 120:
	print "Blood pressure is ideal."
elif BP_STATUS >120 or BP_STATUS < 140:
	print "Blood Pressure is warning."
print 'Your blood pressure is {}' .format(BP_STATUS)
SyntaxError: invalid syntax
>>> if BP_STATUS > 89 or BP_STATUS < 120:
	print "Blood pressure is ideal."
elif BP_STATUS >120 or BP_STATUS < 140:
	print "Blood Pressure is warning."
print 'Your blood pressure is {}' .format(BP_STATUS)
