
import math
from operator import indexOf
import random

# Define mock datasets
stockA = ["CMG", 1247.49, 1233.56, 1223.38, 1270.96, 1338.43, 1362.99, 1387.97, 1355.75, 1390.94]

stockB = ["ADN",
            2.9, 1.19, 1.25, 1.29, 1.41, 1.56, 1.54, 1.41, 1.48, 1.31, 1.26, 1.41, 1.49
        ]
stockC = ["AAPL",
            132.08, 134.29, 133.13, 132.87, 140.28, 147.08, 148.58, 144.35, 147.03
        ]
stockD = ["EE",
            24.56, 27, 25.23, 26.29, 26.35, 27.83, 29.31, 27.86, 30.47, 29.35, 28.75, 26.87
        ]

# Define global variables
targetCorrelation = 0
targetNumAssets = 0

data = [stockA, stockB, stockC, stockD]

# --- Define statistical functions ---

# Define standard deviation
def stdDev(list, limiter=10):
    """Takes a list as an argument and will return standard deviation of the list starting at
    the second index to avoid the ticker, and up to the index specified by a limiter argument"""
    
    # Slice the list to exclude ticker
    newList = list[1:limiter]
    
    # Compute N and mean values
    N = len(newList)    
    mean = sum(newList) / N
    
    # Take sliced array and calculate sum of all Xi - Mean values
    varianceList = []
    for value in newList:
        varianceList.append((value - mean) ** 2)
        
    sumXi = sum(varianceList)
    
    # Divide by N-1 and take square root
    stdevX = math.sqrt(sumXi / (N - 1))
    
    return stdevX
    

# Define covariance
def covar(listX, listY):
    """Takes two lists and calculates their covariance.  Will trim the lists to an equal length
    if one is longer than the other so that the calculation can be run."""
    
    # Measure the length of the two lists and trim to length if necessary.  Exclude ticker.
    listX = listX[1:]
    listY = listY[1:]
    
    # determine which list is the shorter
    shorter = len(listX)
    if (len(listY) < shorter):
        shorter = len(listY)
        
    # Assign N to the smaller value    
    N = shorter
    
    # Trim the longer list, if they are not equal in size
    if (len(listY) > len(listX)):
        listY = listY[:len(listX)]
    elif (len(listX) > len(listY)):
        listX = listX[:len(listY)]
        
    # Compute mean for each list
    meanX = sum(listX) / N
    meanY = sum(listY) / N
    
    # Compute numerator for covariance by multiplying Sum Xi - XBar & Yi - YBar    
    productList = []
    for element in range(N):
        productList.append((listX[element] - meanX) * (listY[element] - meanY))

    sumProduct = sum(productList)
    
    # Compute denominator for sample covariance
    covariance = sumProduct / (N - 1)
    
    return covariance
    

# Correlation function
def correlate(asset1, asset2):
    """Takes two lists and computes correlation from sample covariance and standard deviation"""
    covariance = covar(asset1, asset2)
    
    # Define limiter
    shorter = len(asset1)
    if (len(asset2) < shorter):
        shorter = len(asset2)
        
    # Assign limiter to the smaller value    
    limiter = shorter
    
    stdev1 = stdDev(asset1, limiter)
    stdev2 = stdDev(asset2, limiter)
    
    return covariance / (stdev1 * stdev2)


# Function that iterates through the datasets and finds correlations
def correlationMap(dataset):
    """Takes a list of lists and runs correlation on each pair within the dataset,
    outputting them into a new list containing unique correlations"""
    
    # Count the number of sublists in the dataset
    assetCount = len(dataset)
    
    # Define empty list to store correlation pairs
    results = []
    
    # Loop through and run correlate() function
    # Be sure to include the first element ticker to identify which assets produced results
    i = 0
    while i < len(dataset):
        for list in dataset:
            
            # Only run the correlation if the loop is looking at a unique pair of tickers
            if (list != dataset[i]) & (dataset.index(list) > i):
                # Append a list of both tickers in a sublist and the correlation value to results
                results.append([[list[0], dataset[i][0]], [correlate(list, dataset[i])]])
        i += 1

# ---------- Utility functions for calculating weighted portfolio risk ---------- 

def assign_weights(*assets):
    """Takes a list of assets and converts to a new list with randomly assigned weights"""
    
    # Create new list to return
    weighted_list = []

    # Keep track of the cumlative percentage already applied to assets
    cumulative_weight = 0

    # TODO: Start at a random index using range(len(assets)) instead of index 0 each time to make random assignment more fair
    for asset in assets:

        weight = random.uniform(0,1)

        # Assess whether this weight would cause the cumulative weight to exceed 1
        if (cumulative_weight + weight > 1):
            weight = 1 - cumulative_weight

        weighted_list.append([asset[0], stdDev(asset), weight])
        cumulative_weight += weight

    # Assess whether there are any assets that have not received any weight
    empty_weights = []

    # If so, split the largest existing weight and assign that to the remaining assets randomly...
    # First append those assets' tickers to a new list
    for asset in weighted_list:
        if (asset[2] == 0):
            empty_weights.append(asset[0])

    # Then find those tickers in the weighted_list and assign them new weights by dividing the largest weight

    divisor = len(empty_weights)
    largest = 0
    largest_index = 0

    # Find the largest weight and its index
    for asset in weighted_list:
        if (asset[2] > largest):
            largest = asset[2]
            largest_index = weighted_list.index(asset)

    # Once the largest index has been assigned, use it to allocate its weight to empty weights
    for asset in weighted_list:
        if (asset[0] in empty_weights):

            # Assign random new weight and reduce largest by that amount
            new_weight = random.uniform(0.0001, (largest / divisor))
            asset[2] = new_weight
            weighted_list[largest_index][2] -= new_weight

    for asset in weighted_list:
        print("\n", asset)

    return weighted_list

assign_weights(stockA, stockB, stockC, stockD)


def weighted_risk(*assets):
    """Takes variable number of assets and their weights as a list, and calculates the weighted portfolio risk"""
    print(assets)


# --- Main body of the program (genetic algorithm) ---
def main():

    # Take user input on number of assets to include and target correlation
    def targetNumAssets():
        print("\nAssets in dataset: ", len(data))
        try:
            userChoice = int(input("\nSelect a number of assets to run correlation on."))

            if (userChoice > len(data)):
                print("Select a valid number of assets to correlate.")
                targetNumAssets()
            elif (userChoice <2):
                print("You cannot correlate less than 2 assets.")
                targetNumAssets()
            else:
                print(int(userChoice))
        except:
            print("You must enter an integer.")
            targetNumAssets()

    targetNumAssets()

    def targetRisk():
        try:
            userTarget = float(input("Enter a target risk (standard deviation) for the assets to reach."))
            print("Target Risk: ", userTarget)
        except:
            print("You must enter a valid target Risk.")
            targetRisk()

    targetRisk()
    
    # Take variable number of assets and their historical prices
    def combineAssets(dataset, num, iterations):
        """Takes a dataset of assets and combines num number of them together randomly iterations number of times.
        Returns a list of the assets and their portfolio weighted risk"""

        for attempt in range(len(iterations)):
            # Combine [num] assets from [dataset] into a weighted-portfolio-risk calculation
            print(attempt)
    
    # Randomly combine different assets using random weights

    # Compute portfolio risk of different combinations
    
    # Assess fit of weighted portfolio risk to within acceptable error of target
    
    # Discard lowest quartile and re-run algorithm if outside of bounds
    
    # Return resulting successful mix with proportions of assets

#main()
