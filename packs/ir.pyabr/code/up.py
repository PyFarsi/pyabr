import sys
from pyabr.core import *
from pyabr.cloud import *

for i in sys.argv[1:]:
    d = Drive()
    d.Upload(i)
