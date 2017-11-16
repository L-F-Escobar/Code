import requests, json

url = "https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=both&depth=10"

headers = {
    'cache-control': "no-cache",
    'postman-token': "REMOVED_FOR_SECURITY"
}

body = {
    }

response = requests.request("GET", url, json=body, headers=headers)

responseBody = response.json()

file = open('publicGetOrderBook.txt', 'w')

''' Contains the entire dictionary - Outter dictionary brackets '''
for key in responseBody:

    ''' Captures the first inner nested dictionary '''
    if type(responseBody[key]) == dict:
        transfer = str(key) + ' - \n'
        file.write(transfer)

        ''' Captures the innter dictionary keys | buy/sell '''
        for innerKeys in responseBody[key]:

            transfer = '\t' + str(innerKeys) + ' - \n'
            file.write(transfer)

            #if responseDict[key][innerKeys] == list:
                #print('3')
            ''' List within the inner dictionary unlocked by the inner keys '''
            for i in range (len(responseBody[key][innerKeys])):
                
                # Used to switch between writing quanitiy and rate on the same line
                mod = 0

                ''' Dictionary within the list. Unlocked by buy/sell innerKeys.
                    This loop will gather Quanitity and Rate key/value figures.
                '''
                for innerInnerKeys in responseBody[key][innerKeys][i]:

                    if mod == 0:
                        mod = mod + 1
                        transfer = '\t\t' + str(innerInnerKeys) + ' : ' + str('%13.8f' %(responseBody[key][innerKeys][i][innerInnerKeys])) + '{:>3}'.format(' | ')
                        file.write(transfer)
                    elif mod == 1:
                        mod = 0
                        transfer = str(innerInnerKeys) + ' : ' + str('%11.8f' %(responseBody[key][innerKeys][i][innerInnerKeys])) + '\n'
                        file.write(transfer)

    ''' Will write to file the outtermost dictionary keys & values  '''  
    else:


        transfer = str(key) + ' - ' + str(responseBody[key]) + '\n'
        file.write(transfer)

file.close()
