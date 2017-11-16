import requests, sys, json

'''
    This script produces a getMarketSummaries text file with the market summary
    of all coins. Further, ?market=btc-ltc can be added  to the end of the
    endpoint url with any other market symbols to pull data for that specific
    market. Script isolates all endpoint data in a manner which makes it easily
    retreivable and accessable. 
'''

# Endpoint url.
url = "https://bittrex.com/api/v1.1/public/getmarketsummaries"

# Header Parameters.
headers = {
    'cache-control': "no-cache",
    'postman-token': "REMOVED_FOR_SECURITY"
}

# Body Parameters.
body = {
}

# Make HTTPS Request.
response = requests.request("GET", url, json=body, headers=headers)

# Return requests object as a dictionary of the json data.
responseBody = response.json()

# Open/create text file with relevant name - stores all market summeries.
file = open('getMarketSummaries.txt', 'w')

# Outtermost dictionary - outter brackets.
for key in responseBody:

    # If we have hit the json data which is located in a list, enter.
    if type(responseBody[key]) == list:
        # Grab the key which unlocks the nested list.
        transfer = (str(key)) + ':\n\n'
        file.write(transfer)
        
        # Iterate through the entire list of json data. 
        for i in range (len(responseBody[key])):
            
            #Iterate through the dictionary keys. This dictionary is nested
            #within the list.
            for listKeys in responseBody[key][i]:
                # Write all key/vaule pairs within the nested dictionary.
                w = '\t' + str(listKeys) + ':' + str(responseBody[key][i][listKeys]) + '\n'
                file.write(w)

            file.write('\n')
    else:
        # If we have not hit the json data located within a list.
        transfer = (str(key) + ':' + str(responseBody[key]) + '\n')
        file.write(transfer)

# Close file. 
file.close()
