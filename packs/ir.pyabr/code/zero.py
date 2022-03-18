import sys
from pyabr.core import *
from pyabr.cloud import *

for i in sys.argv[1:]:
    commands.up([i])
    files.create(i)
