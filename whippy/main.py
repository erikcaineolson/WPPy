import sys
import getopt
from whippy import whippy

use_defaults = False

try:
    opts, args = getopt.getopt(sys.argv, 'd', ['defaults'])
except getopt.GetoptError:
    print('whippy [-d|--defaults]')
    sys.exit()

for arg in args:
    if arg == '-d' or arg == '--defaults':
        use_defaults = True

wppy = whippy.Whippy(use_defaults)
wppy.create_wp_database()
wppy.create_wp_site()
