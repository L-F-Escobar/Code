import requests, sys, json

'''
    This script produces marketPairs & publicGetMarket text files with
    all relevant json data. Isolate all the endpoint data in a manner which
    makes it easily retreivable and accessable. 
'''

# Will store all currency pairs in marketPairs text file.
makeMarketPairBTCKey = 'market=BTC-'
makeMarketPairETHKey = 'market=ETH-'
pairFile = open('marketPairs.txt', 'w')

# Function to write all ehtereum currency pairs.
def makeKeyPairETH(getPair, makeMarketPairETHKey, pairFile):
    # Complete currency pair key with the other half.
    makeMarketPairETHKey = makeMarketPairETHKey + getPair + '\n'#Make pair key
    # Write the pair key to an output file.
    pairFile.write(makeMarketPairETHKey)
    # Reset pair key to default.
    makeMarketPairETHKey = 'market=ETH-'
    # Reset temp pair key to default.
    getPair = ''

# Function to write all bitcoin currency pairs.
def makeKeyPairBTC(getPair, makeMarketPairBTCKey, pairFile):
    # Complete currency pair key with the other half.
    makeMarketPairBTCKey = makeMarketPairBTCKey + getPair + '\n'#Make pair key
    # Write the pair key to an output file.
    pairFile.write(makeMarketPairBTCKey)
    # Reset pair key to default.
    makeMarketPairBTCKey = 'market=BTC-'
    # Reset temp pair key to default.
    getPair = ''

    
# Endpoint url.
url = "https://bittrex.com/api/v1.1/public/getmarkets"

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

# Open/create text file with relevant name - stores market pair data.
file = open('publicGetMarket.txt', 'w')

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
                w = '\t' + str(listKeys) + ':' + str(responseBody[key][i][listKeys]) + '\n'
                file.write(w)
                

                '''
                    The next set of if - if elif states are intended to make currency pairs
                    and output them to a text file for future use. By capturing all currency
                    pairs, we can use the resulting text file to iterate through all pairs
                    at will for any specific endpoint which requires a currency pair string
                    literal.
                '''
                # If key is equal to the currency pair - enter.
                if listKeys == 'MarketCurrency':
                    # Save the first part of the pair.
                    getPair = str(responseBody[key][i][listKeys])

                # If the key is the base pair and that base pair is Bitcoin - enter.
                if listKeys == 'BaseCurrency' and responseBody[key][i][listKeys] == 'BTC':
                    # Make currency pair for bitcion and write to output file.
                    makeKeyPairBTC(getPair, makeMarketPairBTCKey, pairFile)
                    
                # If the key is the base pair and that base pair is Etheruem - enter.
                elif listKeys == 'BaseCurrency' and responseBody[key][i][listKeys] == 'ETH':
                    # Make currency pair for ehtereum and write to output file.
                    makeKeyPairETH(getPair, makeMarketPairETHKey, pairFile)
                '''
                    End of code which captures and writes all currency pairs to
                    an output file. 
                '''

            file.write('\n')
    else:
        # If we have not hit the json data located within a list.
        transfer = (str(key) + ':' + str(responseBody[key]) + '\n')
        file.write(transfer)

# Close both files. 
file.close()
pairFile.close()

    
    
