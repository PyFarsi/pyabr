import sys

from pyabr.core import *
from pyabr.account import *

for i in sys.argv[1:]:
    d = Drive()
    d.Unlink(i)

    commands.rm([i])
