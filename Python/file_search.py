import platform, sys, os

class UnknownOSError(Exception):
    ''' Exception raised when script is 
        unable to identify operating system '''
    
    def __init__(self, message, reason):
        self.message = message
        self.reason = reason
        super(UnknownOSError, self).__init__(message, reason) 



##
# 
def find_file(file_name='', root=''):
    
    if file_name == '' or file_name == None:
        return False, "File name is invalid."

    if root == '': 
        if 'windows' in platform.system().lower():
            print('Windows')
            root = 'C:\\Intel'
        elif 'linux' in platform.system().lower():
            print('Linux')
            root = '/home/'
        elif 'darwin' in platform.system().lower():
            print("Apple")
            root = '/Users/'
        else:            
            try:
                raise UnknownOSError(message="Exiting the program.", reason='Unknown OS system.')
            except UnknownOSError as uos:
                print('[ACTION]', uos.args[0])
                print('[REASON]', uos.args[1])
            
            return False, 'Unknown OS system.'

    for folderName, subfolders, filenames in os.walk(top=root):
        print('The current folder is ' + folderName)
        # pass
        
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            # pass

        for filename in filenames:
            if filename == file_name:
                print("\n\nFile has been found at loction: %s" % (folderName + '\\'+ filename))
                found_file = os.path.join(folderName, filename)
                return True, found_file
            print('FILE INSIDE ' + folderName + ': '+ filename)
        
        print()
        # print()

    return False, "File not found."


# print(os.getcwd())
# print(os.listdir(path='.'))
# print(os.listdir(path='..'))
# print()
# print(os.walk(top="C:\\"))
# print(os.popen('wmic logicaldisk get caption'))

# print(sys.platform)
# print(platform.platform(terse=1))
# print(platform.system())
# print(platform.release())
# print(platform.version())

# print()

# def linux_distribution():
#   try:
#     return platform.linux_distribution()
#   except:
#     return "N/A"

# print("""Python version: %s
# dist: %s
# linux_distribution: %s
# system: %s
# machine: %s
# platform: %s
# uname: %s
# version: %s
# mac_ver: %s
# """ % (
# sys.version.split('\n'),
# str(platform.dist()),
# linux_distribution(),
# platform.system(),
# platform.machine(),
# platform.platform(),
# platform.uname(),
# platform.version(),
# platform.mac_ver(),
# ))