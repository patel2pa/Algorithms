"Rough draft of implementing the graph algo"
 
import pandas as py 
 
z = {0:[1,4,5],1:[2,6],2:[3],3:[0],4:[1],5:[2],6:[]}
x = {0:[1,4,5],1:[2,6],2:[3,7],3:[7],4:[1],5:[2],6:[],7:[3],8:[1,2],9:[0,4,5,6,7]}
 
 
y = []
count = []
cons = []
 
 
for n in x:
    for l in x[n]:
        count.append(l)
length_of_count = len(count)
 
 
for num in x:
    print('{} at this iteration /////////////////////////////////////////////'.format(num))
    for v in x:
        #print('The value of y is {}'.format(y))  
        if v == num:
            print("{} is equal to {}".format(num,v))
            continue
        else:
            y.append(num)
             
            if v in x[num]:
                print('found {} in {}'.format(v,num))
                print('The degree is -----------------1')
                cons.append(1)
                y.pop(0)
                 
                 
            else:
                 
                print('Looking for {}'.format(v))
                if x[y[0]] == []:
                    print('{} does not have any connections')
 
                     
                else:                   
                    degree = 0
                    count = 0
                    actual_degree = 1
                    k = 0
 
                    #checking v in first element of y,
                    while v not in x[y[0]]:                        
                        #if its not take the first element and append all the value of it to y
                        for m in x[y[0]]:
                            y.append(m)
                            
                        #pop the first element
                             
                        y.pop(0)
                         
                        if degree == count:
                            degree = len(y)
                            actual_degree = actual_degree + 1
                            count = 0
                        count = count + 1
                        k = k + 1
                         
                        if v in x[y[0]]:
                            print(y)
                            print('The degree is -----------------{}'.format(actual_degree))
                            cons.append(degree)
                        if k > 17:
                            print('Did not find path going from {} to {}'.format(num, v))
                            break                            
        y = []                      
 
 
 
def unique(input_list):
     
    unique_list = []
     
    for q in input_list: 
        
        if q not in unique_list: 
            unique_list.append(q)
     
    return sorted(unique_list)
 
 
 
def table():
     
    list_1 = unique(cons)
     
    for number in list_1:
        print('The count of {} is {}'.format(number,cons.count(number)))
 
  
print(table())
