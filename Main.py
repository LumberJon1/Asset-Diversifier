
import math

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
    
    print(newList)
    
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
    print(limiter)
    print(len(asset2))
    
    stdev1 = stdDev(asset1, limiter)
    stdev2 = stdDev(asset2, limiter)
    
    print("Covariance: ", covariance)
    print("stdev1: ", stdev1)
    print("stdev2: ", stdev2)
    print("correlation: ", covariance / (stdev1 * stdev2))
    
    return covariance / (stdev1 * stdev2)

print(correlate(stockA, stockB))

# Function that iterates through the datasets and finds correlations

# --- Main body of the program (genetic algorithm) ---

    # Take user input on number of assets to include and target correlation

    # Take variable number of assets and their historical prices

    # Compute statistical functions and find correlation of different combinations
    
    # Randomly combine different assets using random weights
    
    # Assess fit of correlation to within acceptable error of target
    
    # Discard lowest quartile and re-run algorithm if outside of bounds
    
    # Return resulting successful mix with proportions of assets
