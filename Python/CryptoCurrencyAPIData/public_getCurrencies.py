import requests

'''
    Script will produce a publicGetCurrencies text file with all currency
    data. Further, the script isolates all endpoint data in a manner which
    makes it easily retreivable and accessable. 
'''

# Endpoint url.
url = "https://bittrex.com/api/v1.1/public/getcurrencies"

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

# Open/create text file with relevant name - stores all currency information.
file = open('publicGetCurrencies.txt', 'w')

# Outtermost dictionary - outter brackets.
for key in responseBody:

    # If we have hit the json data which is located in a list, enter.
    if type(responseBody[key]) == list:
        # Grab the key which unlocks the nested list.
        transfer = (str(key)) + ':\n\n'
        file.write(transfer)

        # Iterate through the entire list of json data. 
        for i in range (len(responseBody[key])):
            
            # Iterate through the dictionary keys. This dictionary is nested
            # within the nested list.
            for listKeys in responseBody[key][i]:
                # Write all key/vaule pairs within the nested dictionary.
                transfer = '\t' + str(listKeys) + ':' + str(responseBody[key][i][listKeys]) + '\n'
                file.write(transfer)

            file.write('\n')
    else:
        # If we have not hit the json data located within a list.
        transfer = (str(key) + ':' + str(responseBody[key]) + '\n')
        file.write(transfer)

# Close file. 
file.close()
