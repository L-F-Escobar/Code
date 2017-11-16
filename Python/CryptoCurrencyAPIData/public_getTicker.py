import requests, sys, json

'''
    Script will produce a publicGetRicket text file with the passed in market
    string literal. Further, the script isloates all endpoint data in a
    ,anner which makes it easily retreivable and accessable.
'''

# Exmaple of passed in market parameter. End point URL must have a market
# parameter.
market = 'market=BTC-LTC'

# Endpoint url.
url = "https://bittrex.com/api/v1.1/public/getticker?" + market

# Header Parameters.
headers = {
    'cache-control': "no-cache",
    'postman-token': "23745368-d19c-533e-4c8e-2448ca8e6ce1"
}

# Body Parameters.
body = {	
}

# Make HTTPS Request.
response = requests.request("GET", url, json=body, headers=headers)

# Return requests object as a dictionary of the json data.
responseBody = response.json()

# Open/create text file with relevant name - store all currency information.
file = open('publicGetTicker.txt','w')

# Write the market name to the text file for easy recognition.
transfer = market + '\n'

# Outtermost dictionary - outter brackets.
for key in responseBody:

    # If we have hit the json data which is located in a dictionary, either.
    if type(responseBody[key]) == dict:
        # Grab the key which unlocks the nested dictionary.
        transfer = (str(key)) + ':\n'
        file.write(transfer)

        # Iterate through the dictionary keys. This dictionary is nested
        # within the outter most dictionary.
        for keys in responseBody[key]:
            # Write all key/value pairs within the nested dictionary
            transfer = '\t' + ('%-5s' %str(keys)) + ': ' + str(responseBody[key][keys]) + '\n'
            file.write(transfer)
    else:
        # If the code has not hit the json data within a dictionary.
        transfer = str(key) + ': ' + str(responseBody[key]) + '\n'
        file.write(transfer)

# Close file.
file.close()
    
