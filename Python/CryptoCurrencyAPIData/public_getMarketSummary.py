import requests, json

'''
    Will report back a market summary for the passed in market string literal.
    Will output all market data into a text file named publicGetMarketSummary.
    Isolate all the endpoint data in a manner which makes it easily retreivable
    and accessable. 
'''

# Endpoint url.
url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=BTC-LTC"

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

# Open/create text file with relevant name - stores market summary data.
file = open('publicGetMarketSummary.txt', 'w')

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
    else:
        # If we have not hit the json data located within a list.
        transfer = str(key) + '- ' + str(responseBody[key]) + '\n'
        file.write(transfer)
        
# Close file.
file.close()
