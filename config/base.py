
import os

HOST = str(os.environ.get('HOST', '0.0.0.0'))
PORT = int(os.environ.get('PORT', 8001)) 
#MODE = bool(os.environ.get('DEV', True)) 

#data = {'reloader': MODE,
#        'host': HOST,
#        'port': PORT }