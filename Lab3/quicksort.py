

def partition(the_list, p, r,compare_func):                     #Partion List
    j=p
    for index in range(p,r):
        if compare_func(the_list[index] , the_list[r]):
            swap = the_list[j]
            the_list[j] = the_list[index]
            the_list[index] = swap
            j=j+1

    temp = the_list[r]
    the_list[r] = the_list[j]
    the_list[j] = temp


    return j



def quicksort(the_list, p, r, compare_func):        #Quicksort a list


    if  p<r:                                        #Base case

        q=partition(the_list,p,r,compare_func)
        quicksort(the_list,p,q-1,compare_func)
        quicksort(the_list,q+1,r,compare_func)





def compare_ints(a,b):                             #Compare functios
    return b<=a

def compare_strings(a, b):
    return str.lower(a) <= str.lower(b)

def sort(the_list, compare_func):                   #Sort function which calls quicksort
    quicksort(the_list,0,len(the_list)-1, compare_func)

