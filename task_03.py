#1/user/bin/env python
# -*- coding: utf-8 -*-

BP_STATUS = int(raw_input("What is your blood pressure? "))
print 119


if BP_STATUS >89 or BP_STATUS < 120:
    print"Blood pressure is ideal."
elif BP_STATUS > 120 or BP_STATUS < 140:
    print "Blood pressure is warning."
print ('Your blood pressure is {}'.format(BP_STATUS))

            
                
