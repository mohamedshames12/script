from optparse import *

parser = OptionParser("""
    My Tool is designed for pentesting
    we need the website url , data website
    --help for more information
         **BY Mohamed shams**                       
""")
parser.add_option("-u","--url",dest="target_url",help="the website")
parser.add_option("-d","--data",dest="target_data",help="the website data")

#----------- Advanced Group --------------------

new_group = OptionGroup(parser,"advanced option group", "some options for advanced usage")
new_group.add_option("-p","--payload",dest="target_payload",help="the payload", default="something went wrong!")
new_group.add_option("-D","--downlaod",dest="target_download",help="the download", default="something went wrong!")
parser.add_option_group(new_group)

(options, args) = parser.parse_args()
if options.target_url == None and options.target_data == None:
    print(parser.usage)
    exit(0)
else:
    print("{0}:{1}".format(options.target_url, options.target_data))
    print("{0}:{1}".format(options.target_payload, options.target_download))