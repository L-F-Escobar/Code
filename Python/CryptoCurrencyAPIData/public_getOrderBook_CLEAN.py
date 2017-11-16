import requests

'''
    
'''

# Example of passed in market parameter. Endpoint URL must have a market
# parameter and type parameter. Market parameter is a currency trading pair
# and type parameter is either buy/sell/both. Depth is an optional parameter
# with default depth = 20.
market = 'market=BTC-LTC&type=both&depth=10'

# Endpoint url. Endpoint URL must have a market parameter. This is an example
# usning btc-ltc parameters & both.
url = "https://bittrex.com/api/v1.1/public/getorderbook?" + market

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

# Open/create text file with relevant name - stores order book data for
# passed in parameters.
file = open('publicGetOrderBook.txt', 'w')

# Outtermost dictionary - outter brackets.
for key in responseBody:

    # If we have hit the json data which is located in a dictionary, enter.
    if type(responseBody[key]) == dict:
        # Grab the key which unlocks the nested dictionary.
        transfer = str(key) + ' - \n'
        file.write(transfer)

        # Captures the innter dictionary keys | buy/sell.
        for innerKeys in responseBody[key]:
            transfer = '\t' + str(innerKeys) + ' - \n'
            file.write(transfer)
            
            # List within the inner dictionary unlocked by the inner keys | buy/sell.
            for i in range (len(responseBody[key][innerKeys])):
                # Used to switch between writing quanitiy and rate on the same line
                mod = 0

                # Dictionary within the list. Unlocked by buy/sell innerKeys.
                # Loop will gather Quanitity and Rate key/value figures.
                for innerInnerKeys in responseBody[key][innerKeys][i]:
                    # Buy orders key.
                    if mod == 0:
                        mod = mod + 1
                        # Write the key/value pair that is nested in a dictionary, within a
                        # list, with a dictionary, within a dictionary. 
                        transfer = '\t\t' + str(innerInnerKeys) + ' : ' + str('%13.8f' %(responseBody[key][innerKeys][i][innerInnerKeys])) + '{:>3}'.format(' | ')
                        file.write(transfer)
                    # Sell order key.
                    elif mod == 1:
                        mod = 0
                        # Write the key/value pair that is nested in a dictionary, within a
                        # list, with a dictionary, within a dictionary. 
                        transfer = str(innerInnerKeys) + ' : ' + str('%11.8f' %(responseBody[key][innerKeys][i][innerInnerKeys])) + '\n'
                        file.write(transfer)
                        
    # If we have not hit the json data located within a dictionary.  
    else:
        transfer = str(key) + ' - ' + str(responseBody[key]) + '\n'
        file.write(transfer)

# Close file. 
file.close()
