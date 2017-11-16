'''
Created on Jul 10, 2017

@author: Luis.Escobar-Driver
'''


import requests, json, time

'''
    Script will write to text file getOpenOrders 
'''

# Example of passed in market parameter. Endpoint URL must have a market
# parameter.
market = 'market=ETH-SNT'# Market string literal is optional
API_KEY = 'apikey=REMOVED_FOR_SECURITY'# API_Key is required 
NONCE = str(int(time.time() * 1000))

# Endpoint url. Endpoint URL must have a market parameter. This is an example
# usning btc-dash parameters.
url = "https://bittrex.com/api/v1.1/account/getbalances?" + API_KEY

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

# Open/create text file with relevant name - stores market history data
# for market parameter.
file = open('publicGetMarketHistory.txt', 'w')


# Outtermost dictionary - outter brackets.
for key in responseBody:

    # If we have hit the json data which is located in a list, enter.
    if type(responseBody[key]) == list:
        transfer = str(key) + '-' + '\n'
        file.write(transfer)

        # In the list json data. Iterate through it all.
        for i in range(len(responseBody[key])):

            # Within the list. Inside the list is a dictionary. Iterate through
            # all the keys/value pairs within the dictionary.
            for innerKeys in responseBody[key][i]:
                transfer = '\t' + str(innerKeys) + ' -  ' + str(responseBody[key][i][innerKeys]) + '\n'
                file.write(transfer)
            # Create a line of spacing for each market order.
            file.write('\n')
    else:
        # If we have not hit the json data located within a list.
        transfer = str(key) + '- ' + str(responseBody[key]) + '\n'
        file.write(transfer)
        
# Close file.
file.close()
