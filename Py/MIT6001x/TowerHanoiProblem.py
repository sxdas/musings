# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:41:41 2016

@author: sayooj
"""

def pmove(fr,to):
    print('move from '+str(fr) + ' to ' + str(to))
    
def towers(n,fr,to,spare):
    if n==1:
        pmove(fr,to)
    else:
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)
        
print(towers(4,'Tower 1','Tower 2','Tower 3'))