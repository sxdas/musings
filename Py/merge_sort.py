#==============================================================================
# The Quick Sort algorithm in Python 2
#==============================================================================

def quicksort(alist):
    quicksorthelper(alist,0,len(alist)-1)

def quicksorthelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,list)
        
        quicksorthelper(alist,first,splitpoint-1)
        quicksorthelper(alist,splitpoint+1,last)
       
        
def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    
    while not done:
        
        while leftmark <= rightmark and\
            alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
                
        while alist[rightmark] >= pivotvalue and \
            rightmark >= leftmark:
                rightmark = rightmark - 1
                
        if rightmark < leftmark:
            done = True
        else: 
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    
    return rightmark