__author__ = 'panc'

from okgtreg.simulation.sim_01252016_1017.models import *
from okgtreg.groupStructureDetection.backwardPartition import backwardPartition

import sys, os
import datetime
import pickle

# Current time
currentTimeStr = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

# Parse model id from command line input
args = sys.argv
model_id = int(args[1])

# Selected model
model = selectModel(model_id)

# Kernel
kernel = Kernel('gaussian', sigma=0.5)

# Print simulation information
s1 = "# Simulation time: %s" % currentTimeStr
s2 = "# Selected Model: %d" % model_id
s3 = "# Kernel: Gaussian (0.5)"
s4 = "# Training method: vanilla"
swidth = max(len(s1), len(s2), len(s3), len(s4)) + 2
s0 = ''.join(np.repeat("#", swidth))
s5 = ''.join(np.repeat("#", swidth))
print '\n'.join((s0, s1, s2, s3, s4, s5))

# Simulation
nSample = 500
nSim = 100
seeds = np.arange(nSim)
res = {}

## simulate data
for i in range(nSim):
    print("=== seed: %d ===" % seeds[i])
    np.random.seed(seeds[i])
    data, tgroup = model(nSample)
    optimalRes = (backwardPartition(data, kernel))
    res[optimalRes['group']] = optimalRes['r2p']

# Pickle results
mydir = os.getcwd()
filename = 'script-model-' + str(model_id) + '.pkl'
saveto = mydir + '/' + filename
pickle.dump(res, open(saveto, 'wb'))

# # Create bash script
# for i in range(10):
#     print("python -u script.py %d > script-model-%d.out" % (i + 1, i + 1))
