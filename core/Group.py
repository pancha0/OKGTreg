class Group(object):
    def __init__(self, *args, **kwargs):
        # group with one covariate must input explicitly

        n = len(args)  # number of input groups

        # check duplicates
        inputs = [i for g in args for i in g]  # flatten args
        uniqueInputs = set(inputs)
        if len(inputs) > len(uniqueInputs):
            raise ValueError("** Each index can only be in one group. "
                             "Please remove duplication. **")

        # check if groups are ordered by the first index
        firstIndices = [g[0] for g in args]
        isOrdered = all(firstIndices[i] <= firstIndices[i+1] for i in xrange(n - 1))

        if not isOrdered:
            orders = sorted(range(n), key=lambda k: firstIndices[k])
            self.partition = tuple(args[order] for order in orders)
        else:
            self.partition = args

        self.size = n

        # accept number of covariates from keyword argument
        # or set automatically as the size of the flattened args if not given
        if len(kwargs) > 0:
            for key in ('p'): setattr(self, key, kwargs.get(key))
        else:
            self.p = len(inputs)

    def getPartition(self, partitionNumber=None):
        # partitionNumber start from 1
        if partitionNumber is None:
            return self.partition
        else:
            if partitionNumber <= 0 or partitionNumber > self.size:
                raise ValueError("** 'partitionNumber' is is out of bounds. **")

            return self.partition[partitionNumber - 1]

    def __getitem__(self, index):
        return self.getPartition(index)

    def addNewCovariateToGroup(self, covariateIndex, groupNumber):
        # Add a new covariate to an existing group in the structure
        # Both arguments start from 1
        if groupNumber > self.size:
            raise ValueError("** 'groupNumber' = %d is out of bound. "
                             "Partition has %d group(s). **" % (groupNumber, self.size))

        if covariateIndex in [i for g in self.partition for i in g]:
            raise ValueError("** Covariate %d is already in the partition. **" % covariateIndex)

        updatedGroup = self.partition[groupNumber-1] + [covariateIndex]
        # print updatedGroup
        unchangedGroups = tuple(self.partition[i] for i in range(self.size) if i is not groupNumber-1)
        # print unchangedGroups
        return Group(*(unchangedGroups + (updatedGroup,)))

    def addNewCovariateAsGroup(self, covariateIndex):
        # Add a new covariate as a new group in the structure
        # covariateIndex starts from 1
        if covariateIndex in [i for g in self.partition for i in g]:
            raise ValueError("** Covariate %d is already in the partition. **" % covariateIndex)

        return Group(*(self.partition + ([covariateIndex],)) )