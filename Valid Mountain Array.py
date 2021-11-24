class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # condition to know the length of the array is more than 2
        if len(arr) <= 2:
            return False
        
        # getting the peak of the mountain
        largest = 0
        position = 0 
        for i in range(len(arr)):
            if largest < arr[i]:
                largest = arr[i]
                position = i 
            
        #condition is the peak is in the begining or in the end
        if position == 0 or position == len(arr) - 1:
            return False
        
        #dividing the list into two slices
        slice1 = arr[:position + 1]
        slice2 = arr[position:]
        
        #making sure that slice1 is strictly increasing
        for i in range(len(slice1)-1):
            if slice1[i] >= slice1[i+1]:
                return False
        
        #making sure that slice2 is strictly decreasing
        for k in range(len(slice2)-1):
            if slice2[k] <= slice2[k+1]:
                return False
        
        #if all the conditions are flitered
        return True
        
            