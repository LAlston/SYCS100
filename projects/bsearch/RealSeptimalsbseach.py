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

def bsearch(list, element):              #bsearch function definition 
    if len(list) != 0:                     #condition checking for emptiness 
        first = 0                   
        last = len(list)-1                #declaration of last index variable 
        found = False                        #bool found variable defined 
        while not found:                  #while loops until element is found 
            midpoint = (first + last)/2         #updates midpoint checking
            if (first==last) and (element != list[first]):      #when one element is left to be searched and that element is not the desired value   
                print 'Element is not in list.'     
                return -1                                   #ends function 
            elif element < list[midpoint]:              #if element is less than element at current list position 
                last = midpoint - 1                     #updates last index value 
            elif element > list[midpoint]:              #if element is greater than element at current list positon 
                first = midpoint + 1                    #updates first index value 
            else:                                       #else element equals element at current list positon 
                found = True                        #ends while loop 
                return midpoint     #returns index of searched element 
    else:                           #list is empty 
        print 'Element cannot be found. List is empty.'
        return -1













