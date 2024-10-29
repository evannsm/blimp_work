import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lbaird38/evanns_blimp/install/blimp_mpc_ros'
