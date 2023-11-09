#Preset code: our container for the methods that solve the problem.
class Solution:
        #Preset code: defines a method kidsWithCandies.
        #Self is a conventional item which is a reference to the instance of the Solution class.
        #candies is a list of int's where each int represents the # of candies each kid has.
        #extraCandies is an int that represents the # of extra candies.
        #-> List[bool] tells use that this method will return a list of boolean values.
        def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	        #Here we calculate the maximum number of candies that any single kid has BEFORE we distribute the extra candies using the 'max' function.
                maxCandies = max(candies)
                #This is an empty list that we will utilize to store the answer (which will be a list of boolean values the method returns).
	        result = []
                #The start of a 'for' loop that will iterate over the indices of the 'candies' list.
                #'len(candies)' calculates the number of elements in the 'candies' list.
                #'range(len(candies))' takes the length mentioned in the line above as an argument and generates a sequence of numbers of that length starting from 0.
                #Note that this creates a list that corresponds to indices in the 'candies' list.
                #'for i in' tells Python to start a loop, and 'in' specifies that the loop should iterate over the sequence that follows. 
                #The variable i is assigned each value from the sequence one by one, with each iteration of the loop.
	        for i in range(len(candies)):
                        #Here we check whether the current kid, at index 'i' in the candies list, has a number of candies greater than or equal to 'maxCandies' after receiving 'extraCandies'. 
		        if candies[i]+extraCandies >= maxCandies:
                                #If they do indeed have the greatest number of candies or atleast equal it, the result returns True and this result is appended to the 'result' list.
			        result.append(True)
		        #If the condition is not met, False is returned instead. 
                        else:
			        result.append(False)
	        #Once the loop is finished executing, the 'result' list is returned and we have our answer!
                return result
