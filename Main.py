
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
def stdDev(list):
    """Takes a list as an argument and will return standard deviation of the 2nd - last indices"""
    
    print(list)
    
    # Slice the list to exclude ticker
    newList = list[1:]
    
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
    
    
print(stdDev(stockA))

# Function that iterates through the datasets and finds correlations

# --- Main body of the program (genetic algorithm) ---

    # Take user input on number of assets to include and target correlation

    # Take variable number of assets and their historical prices

    # Compute statistical functions and find correlation of different combinations
    
    # Randomly combine different assets using random weights
    
    # Assess fit of correlation to within acceptable error of target
    
    # Discard lowest quartile and re-run algorithm if outside of bounds
    
    # Return resulting successful mix with proportions of assets
