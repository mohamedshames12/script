from optparse import OptionParser

parser = OptionParser("""
    My Tool is designed for pentesting
    we need the website url , data website
    --help for more information
         **BY Mohamed shams**                       
""")
parser.add_option("-u","--url",dest="target_url",help="the website")
parser.add_option("-d","--data",dest="target_data",help="the website data")
parser.add_option("-U","--username",dest="target_username",help="username")
parser.add_option("-P","--password",dest="target_password",help="password")
(options, args) = parser.parse_args()
if options.target_url == None and options.target_data == None and options.target_username == None and options.target_password == None:
    print(parser.usage)
    exit(0)
else:
    print("{0}:{1}:{2}:{3}".format(options.target_url, options.target_data, options.target_username, options.target_password))