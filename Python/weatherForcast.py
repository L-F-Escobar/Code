import requests, json, sqlite3, datetime
from sqlite3 import Error

## Web sites of interest
# http://www.sqlitetutorial.net/sqlite-python/
# http://openweathermap.org/api
#

'''
    Script will return back basic weather information from passed in location into variable city.
'''
# Endpoint url.
currentWeatherURL = "http://api.openweathermap.org/data/2.5/weather?"
city = 'q=Mazatlan,MX'  # <-- Only change this for different cities -->
APPID = '&APPID=bc8ca41055428d37da603f783d6a300c'
units = '&units=imperial'
currentWeather = currentWeatherURL + city + APPID + units

forcastWeatherURL = 'http://api.openweathermap.org/data/2.5/forecast?'
forcastWeather = forcastWeatherURL + city + APPID + units

dailyWeatherURL = 'http://api.openweathermap.org/data/2.5/forecast/daily?'
days = '&cnt=7' # <-- How many days (1-16)
daailyForecastWeather = dailyWeatherURL + city + APPID + units + days


# Header Parameters.
headers = {
    'cache-control': "no-cache",
    'Content-Type' : 'application/json'
}


# Body Parameters.
body = {    
}


# Make HTTPS Request.
current_response = requests.request("GET", currentWeather, json=body, headers=headers)
forecast_response = requests.request("GET", forcastWeather, json=body, headers=headers)
daily_response = requests.request("GET", daailyForecastWeather, json=body, headers=headers)

# Return requests object as a dictionary of the json data.
currentWeatherResponseBody = current_response.json()    # Current day weather
forecastWeatherResponseBody = forecast_response.json()  # 5 day 3 hour incs
dailyWeatherResponseBody = daily_response.json()        # 




# # <-- Test Code for current weather data -->
# for keys in currentWeatherResponseBody:
#     if keys == 'coord':
#         print('Coordinates are')
#       
#     print('%-15s' %keys, '%-10s' %currentWeatherResponseBody[keys])
# print()

# # <-- Test Code for forecast weather data -->
# for i in range(len(forecastWeatherResponseBody['list'])):
#     for keys in forecastWeatherResponseBody['list'][i]:
#         print('%-10s' %keys, '%-10s' %forecastWeatherResponseBody['list'][i][keys])
# print()

# '''
#     Used to edit text throughout the program.
#         ex. print(color.BOLD + 'text' + color.END) ~ text will be bold.
# '''
# class colors: 
#     PURPLE = '\033[95m'
#     CYAN = '\033[96m'
#     DARKCYAN = '\033[36m'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = '\033[91m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     END = '\033[0m'


'''
    Prints the name of the city and country.
'''
def getCurrentName(jsonData):
    if 'name' in jsonData:
        cityFor = jsonData['name']
    
    if 'sys' in jsonData:
        if 'country' in jsonData['sys']:
            country = jsonData['sys']['country']

    print(str(cityFor), ',', str(country), sep='')
        
        
'''
    Will print out wind mph and direction data to the console.
'''      
def getCurrentWindInfo(jsonData):
    if 'wind' in jsonData:
        if 'speed' in jsonData['wind']:
            windDegrees = jsonData['wind']['speed']

    direction = windCompass(int(windDegrees))
    print('%-20s' %('Wind MPH:'), str(windDegrees))
    print('%-20s' %('Wind direction:'), str(direction))
     
     
    
'''
    Helper function for getWindInfo. Will convert raw degree wind direction 
    into actual human readable direction.
'''
def windCompass(windDegrees):            
    if (windDegrees > 348.75 and windDegrees <= 360) or (windDegrees >= 0 and windDegrees <= 11.25):
        return 'North'
    elif windDegrees > 11.25 and windDegrees <= 33.75:
        return 'North North Eastern'
    elif windDegrees > 33.75 and windDegrees <= 56.25:
        return 'North East'
    elif windDegrees > 56.25 and windDegrees <= 78.75:
        return 'East North Eastern'
    elif windDegrees > 78.75 and windDegrees <= 101.25:
        return 'East'
    elif windDegrees > 101.25 and windDegrees <= 123.75:
        return 'East South Eastern'
    elif windDegrees > 123.75 and windDegrees <= 146.25:
        return 'South Eastern'
    elif windDegrees > 146.25 and windDegrees <= 168.75:
        return 'South South Eastern'
    elif windDegrees > 168.75 and windDegrees <= 191.25:
        return 'South'
    elif windDegrees > 191.25 and windDegrees <= 213.75:
        return 'South South Western'
    elif windDegrees > 213.75 and windDegrees <= 236.25:
        return 'South West'
    elif windDegrees > 236.25 and windDegrees <= 258.75:
        return 'West South Western'
    elif windDegrees > 258.75 and windDegrees <= 281.25:
        return 'West'
    elif windDegrees > 281.25 and windDegrees <= 303.75:
        return 'West North West'
    elif windDegrees > 303.75 and windDegrees <= 326.25:
        return 'North West'
    elif windDegrees > 326.25 and windDegrees <= 348.75:
        return 'North North Western'
    else:
        return 'Invalid wind degree raw data.'



'''
    Will print out the cloud coverage percentage of the area.
'''
def getCurrentCloudData(jsonData):
    if 'clouds' in jsonData:
        if 'all' in jsonData['clouds']:
            cloudPercentage = str(jsonData['clouds']['all']) +'%'
            
    print('%-20s' %('Cloud cover is:'), str(cloudPercentage))
    
    

'''
    Will print out visibility data.
'''
def getCurrentVisibilityData(jsonData):
    if 'visibility' in jsonData:
        visibility = str(jsonData['visibility'])
            
    print('%-20s' %('Visibility is:'), visibility, 'ft.')
    
    
    
'''
    Will print to console humidity percentage and current temperature.
'''
def getCurrentTempAndHumidity(jsonData):
    if 'main' in jsonData:
        if 'temp' in jsonData['main']:
            temp = jsonData['main']['temp']
            
        if 'humidity' in jsonData['main']:
            humidity = str(jsonData['main']['humidity']) + '%'
            
    print('%-20s' %('Temperature is:'), str(temp), 'deg')   
    print('%-20s' %('Humidity is:'), str(humidity)) 
    
    
    
'''
    Will print to console the longitude and latitude of searched city.
'''
def getCurrentLongAndLatCoor(jsonData):
    if 'coord' in jsonData:
        if 'lon' in jsonData['coord']:
            longitude = jsonData['coord']['lon']
            
        if 'lat' in jsonData['coord']:
            latitude = jsonData['coord']['lat']
            
    print('%-20s' %('Longitude:'), str(longitude))   
    print('%-20s' %('Latitude:'), str(latitude)) 
    


'''
    Will get UNIX data formats for sunrise/sunset and convert them to readable 
    sunrise/sunset formats. Will print to console.
'''
def getCurrentSunRiseSetData(jsonData):
    if 'sys' in jsonData:
        if 'sunrise' in jsonData['sys']:
            sunRiseUNIX = jsonData['sys']['sunrise']
            
        if 'sunset' in jsonData['sys']:
            sunSetUNIX = jsonData['sys']['sunset']
    
    sunRise = datetime.datetime.fromtimestamp(int(sunRiseUNIX)).strftime('%Y-%m-%d %H:%M:%S')
    sunSet = datetime.datetime.fromtimestamp(int(sunSetUNIX)).strftime('%Y-%m-%d %H:%M:%S')
    
    print('%-20s' %('Sunrise:'), str(sunRise), 'AM')   
    print('%-20s' %('Sunset:'), str(sunSet), 'PM')    
  
    
    
        
'''
    <----------------------> FUTURE FORECAST STARTS HERE <---------------------->
'''

'''
'''
def getForecastFiveDaysThreeHourIncrements(forecastWeatherResponseBody):
    
    ''' Block of code to extract data from the 'list' key '''
    for i in range(len(forecastWeatherResponseBody['list'])):
        
        rainVolume = 0.0
        snowVolume = 0.0
        
        # Iterate through all the keys within the 'list' key
        for keys in forecastWeatherResponseBody['list'][i]:
    
            # Block of code to extract all information from 'main' key.
            if 'main' == keys:
                # Iterate through all the keys within 'main'
                for mainKey in forecastWeatherResponseBody['list'][i][keys]:
                    # Get the temperature for the day.
                    if mainKey == 'temp':
                        temperature = forecastWeatherResponseBody['list'][i][keys][mainKey]
                    # Get the minimum temperature for the day.
                    elif mainKey == 'temp_min':
                        minTemp = forecastWeatherResponseBody['list'][i][keys][mainKey]
                    # Get the maximum temperature for the day.
                    elif mainKey == 'temp_max':
                        maxTemp = forecastWeatherResponseBody['list'][i][keys][mainKey]
                    # Get atmospheric pressure on the sea level by default, hPa.
                    elif mainKey == 'pressure':
                        atmosphericPressure = forecastWeatherResponseBody['list'][i][keys][mainKey]
                    # Get atmospheric pressure on the sea level, hPa.
                    elif mainKey == 'sea_level':
                        atmoshpericPressureOnSeaLvl = forecastWeatherResponseBody['list'][i][keys][mainKey]
                    # Get atmospheric pressure on the ground, hPa.
                    elif mainKey == 'grnd_level':
                        atmoshpericPressureOnGroundLvl = forecastWeatherResponseBody['list'][i][keys][mainKey]
                    # Get humidity percentage.
                    elif mainKey == 'humidity':
                        humidityPercentage = str(forecastWeatherResponseBody['list'][i][keys][mainKey]) + '%'
            
            # Block of code to extract all information from 'weather' key.
            if 'weather' == keys: # <-- Weather is located within a list. -->
                # Iterate through the list.
                for k in range(len(forecastWeatherResponseBody['list'][i][keys])):
                    # Get the keys within the list dictionary.
                    for weatherKeys in forecastWeatherResponseBody['list'][i][keys][k]:
                        # Get the description of the weather condition. 
                        if weatherKeys == 'description':
                            timeDescription = forecastWeatherResponseBody['list'][i][keys][k][weatherKeys]
                
            # Block of code to extract all information from 'clouds' key.
            if 'clouds' == keys:
                # Iterate through all the keys within 'clouds'
                for mainKey in forecastWeatherResponseBody['list'][i][keys]:
                    # Get the cloud cover percentage. 
                    if mainKey == 'all':
                        cloudCover = str(forecastWeatherResponseBody['list'][i][keys][mainKey]) + '%'
               
            # Block of code to extract all information from 'wind' key.
            if 'wind' == keys:
                # Iterate through all the keys within 'wind'
                for mainKey in forecastWeatherResponseBody['list'][i][keys]:
                    # Get the wind speed in MPH. 
                    if mainKey == 'speed':
                        windMPH = forecastWeatherResponseBody['list'][i][keys][mainKey]
                    # Get wind direction - raw data is in degrees.
                    elif  mainKey == 'deg':
                        # Convert raw data degrees into human readable direction.
                        windDegree = forecastWeatherResponseBody['list'][i][keys][mainKey]
                        direction = windCompass(int(windDegree))
                        
            # Block of code to extract all information from 'rain' key.
            if 'rain' == keys:
                # Iterate through all the keys within 'rain'
                for mainKey in forecastWeatherResponseBody['list'][i][keys]:
                    # Get the rain volume for the last 3 hours, mm.
                    if mainKey == '3h':
                        rainVolume = float(forecastWeatherResponseBody['list'][i][keys][mainKey])
                        
            # Block of code to extract all information from 'snow' key.
            if 'snow' == keys:
                # Iterate through all the keys within 'snow'
                for mainKey in forecastWeatherResponseBody['list'][i][keys]:
                    # Get the snow volume for the last 3 hours.
                    if mainKey == '3h':
                        snowVolume = float(forecastWeatherResponseBody['list'][i][keys][mainKey])
                        
            # Block of code to extract all information from 'dt_txt' key.
            if 'dt_txt' == keys:
                dayTime = forecastWeatherResponseBody['list'][i][keys]
      
        print('-------------------------------------------')   
        print('%-20s' %('Day/Time:'), str(dayTime)) 
        print('%-20s' %('Temperature:'), str(temperature))
        #print('%-20s' %('Minimum Temp:'), str(minTemp))  
        #print('%-20s' %('Maximum Temp:'), str(maxTemp))  
        #print('%-20s' %('Atmospheric Pressure'), str(atmosphericPressure))  
        print('%-20s' %('Atmos. Sea level:'), str(atmoshpericPressureOnSeaLvl))  
        print('%-20s' %('Atmos. Ground level:'), str(atmoshpericPressureOnGroundLvl))  
        print('%-20s' %('Humidity:'), str(humidityPercentage))  
        print('%-20s' %('Conditions:'), str(timeDescription))  
        print('%-20s' %('Cloud Cover:'), str(cloudCover))  
        print('%-20s' %('Wind MPH:'), str(windMPH))  
        print('%-20s' %('Wind Direction:'), str(direction))  
        print('%-20s' %('Rain Volume mm:'), str('%.4f' %(rainVolume))) 
        print('%-20s' %('Snow Volume mm:'), str('%.4f' %(snowVolume))) 



'''
    <----------------------> DAILY FORECAST STARTS HERE <---------------------->
'''
'''
    
'''
def getDailyForecast(dailyWeatherResponseBody):
    ''' Block of code to extract data from the 'list' key '''
    for i in range(len(dailyWeatherResponseBody['list'])):
        
        # Iterate through all the keys within the 'list' key
        for keys in dailyWeatherResponseBody['list'][i]:
            if 'dt' == keys:
                UNIXday = dailyWeatherResponseBody['list'][i][keys]
                dayTime = datetime.datetime.fromtimestamp(int(UNIXday)).strftime('%Y-%m-%d %H:%M:%S')
                
                
            # Block of code to extract all information from 'temp' key.
            if 'temp' == keys:
                # Iterate through all the keys within 'temp'
                for mainKey in dailyWeatherResponseBody['list'][i][keys]:
                    # Get the temperature for the day.
                    if mainKey == 'day':
                        dayTemp = dailyWeatherResponseBody['list'][i][keys][mainKey]
                    elif mainKey == 'min':
                        minTemp = dailyWeatherResponseBody['list'][i][keys][mainKey]
                    elif mainKey == 'max':
                        maxTemp = dailyWeatherResponseBody['list'][i][keys][mainKey]
                    elif mainKey == 'night':
                        nightTemp = dailyWeatherResponseBody['list'][i][keys][mainKey]
                    elif mainKey == 'eve':
                        eveTemp = dailyWeatherResponseBody['list'][i][keys][mainKey]
                    elif mainKey == 'morn':
                        mornTemp = dailyWeatherResponseBody['list'][i][keys][mainKey]
                
            if 'pressure' == keys:
                pressure = dailyWeatherResponseBody['list'][i][keys]
    
            # Block of code to extract all information from 'weather' key.
            if 'weather' == keys: # <-- Weather is located within a list. -->
                # Iterate through the list.
                for k in range(len(dailyWeatherResponseBody['list'][i][keys])):
                    # Get the keys within the list dictionary.
                    for weatherKeys in dailyWeatherResponseBody['list'][i][keys][k]:
                        # Get the description of the weather condition. 
                        if weatherKeys == 'description':
                            timeDescription = dailyWeatherResponseBody['list'][i][keys][k][weatherKeys]
    
        print('-------------------------------------------')   
        print('%-20s' %('Day/Time:'), str(dayTime)) 
        print('%-20s' %('Day temperature:'), str(dayTemp))
        print('%-20s' %('Minimum temperature:'), str(minTemp))
        print('%-20s' %('Maximum temperature:'), str(maxTemp))
        print('%-20s' %('Night temperature:'), str(nightTemp))
        print('%-20s' %('Evening temperature:'), str(eveTemp))
        print('%-20s' %('Morning temperature:'), str(mornTemp))
        print('%-20s' %('Pressure pHa:'), str(pressure))
        print('%-20s' %('Conditions:'), str(timeDescription))




class DataBase:
    # Constructor
    def __init__(self, db_file_location=''):
        self.db_file = db_file_location # <-- Open/Create a SQLite3 database -->
    
    
    '''
        Create a database connection to the SQLite database specified by 
        self.db_file.
        :param:
        :return Connection object or None
    '''
    def create_connection(self):
        ''' Create a database connection to a SQLite database '''
        try:
            connectionObject = sqlite3.connect(self.db_file)
            return connectionObject
        except Error as e:
            print(e)
        return None
    

    '''
        Create a table from the create_table_SQL statement.
        :param connection: connection object
        :param create_table_SQL: a CREATE TABLE statement
        :return:
    '''
    def create_table(self, connectionObject, create_table_SQL):
        try:
            cursorObject = connectionObject.cursor()
            cursorObject.execute(create_table_SQL)
        except Error as e:
            print(e)
            
            
    '''
        Create a new project into the projects table.
        :param connectionObject:
        :param project:
        :return: project id
    '''
    def create_current_weather_table(self, connectionObject, tableData):
        sql = ''' INSERT INTO current(windMPH, windDirection, cloudCover, Visibility, sunRise, sunSet, longitude, latitude)
                  VALUES(?,?,?,?,?,?,?,?)
              '''
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql, tableData)
        return cursorObject.lastrowid
    
    
    '''
    Updates the current weather db table.
    :param connectionObject
    :param task:
    :return: project id
    '''
    def update_current_weather_table(self, connectionObject, currentWeather):
        sql = ''' UPDATE current
                  SET windMPH = ? ,
                      windDirection = ? ,
                      cloudCover = ? ,
                      Visibility= ?,
                      sunRise= ?,
                      sunSet= ?,
                      longitude= ?,
                      latitude= ? 
                  WHERE id = ?
             '''
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql, currentWeather)
    


    '''
        Deletes an entry into the current weather db according to its id number.
        :param connectionObject: connection to the SQLite database
        :param id: id of the task
        :return:
    '''
    def delete_specific_current_weather_table(self, connectionObject, id):
        sql = 'DELETE FROM current WHERE id=?'
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql, (id,))


    '''
        Deletes all rows in the current weather db.
        :param connectionObject: connection to the SQLite database
        :return:
    '''
    def delete_entire_current_weather_table(self, connectionObject):
        sql = 'DELETE FROM current'
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sql)


#     # Destructor
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print(class_name, "destroyed")
#              



        
'''
    Main Program.
'''    
if __name__ == '__main__':

    # TESTING DB CLASS    
    dataBase = DataBase('/relative/path/to/file/you/want/fileName.db')
    
    current_weather = ''' CREATE TABLE IF NOT EXISTS current(
                                    id integer PRIMARY KEY,
                                    windMPH text,
                                    windDirection text,
                                    cloudCover text,
                                    Visibility text,
                                    sunRise text,
                                    sunSet text,
                                    longitude text,
                                    latitude text
                                    ); '''

    
    # Create a database connection.
    connection = dataBase.create_connection()
    if connection is not None:
        # Create projects table.
        create_table(connection, current_weather)
    else:
        print('Error! Cannot create the database connection.')
    
    # Insert data into database.
    with connection:
        # Create a new project.
        current_weather_data = ('5MPH', 'North', '6%', '562ft', '06:21AM', '8:52PM', '153.21', '231.12')
        current_weather_table = dataBase.create_current_weather_table(connection, current_weather_data)


    # Update database.
    updated_weather_data = ('666MPH', 'DirUpdate', '122%', '666ft', '06:00AM', '09:52PM', '100', '101', 9)
    with connection:
        dataBase.update_current_weather_table(connection, ('666MPH', 'DirUpdate', '122%', '666ft', '06:00AM', '09:52PM', '100', '101', 1))
          
    # Delete a task and all tasks
    with connection:
        dataBase.delete_specific_current_weather_table(connection, 2)
        #dataBase.delete_entire_current_weather_table(connection)
        #delete_all_tasks(connectionObect) # <-- Will delete all tasks -->


    print('Current weather conditions for ', end='')
    getCurrentName(currentWeatherResponseBody)
    print('-------------------------------------------')
    getCurrentWindInfo(currentWeatherResponseBody)
    #print('-------------------------------------------')
    getCurrentCloudData(currentWeatherResponseBody)
    #print('-------------------------------------------')
    getCurrentVisibilityData(currentWeatherResponseBody)
    #print('-------------------------------------------')
    getCurrentTempAndHumidity(currentWeatherResponseBody)
    #print('-------------------------------------------')
    getCurrentLongAndLatCoor(currentWeatherResponseBody)
    #print('-------------------------------------------')
    getCurrentSunRiseSetData(currentWeatherResponseBody)
    
    print('\n\n\nDaily weather forecast for ' , end='')
    getCurrentName(currentWeatherResponseBody)
    getDailyForecast(dailyWeatherResponseBody)
    
    print('\n\n\nFurture weather forecast for ' , end='')
    getCurrentName(currentWeatherResponseBody)
    getForecastFiveDaysThreeHourIncrements(forecastWeatherResponseBody)





