# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top >= search >= bottom):
    return -1 

   
  while ( bottom != top):
    # when bottom == top then you have found the index

    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    else:
      return mid

#Lena Alston 

def bsearch(list, element):              
    if len(list) != 0:                     
        first = 0                   
        last = len(list)-1          
        found = False                   
        while not found:                
            midpoint = (first + last)/2         
            if (first==last) and (element != list[first]):  
                print 'Element is not in list.'     
                return -1                                   
            elif element < list[midpoint]:       
                last = midpoint - 1                   
            elif element > list[midpoint]:            
                first = midpoint + 1                
            else:                                   
                found = True                      
                return midpoint     
    else:                           
        return -1













