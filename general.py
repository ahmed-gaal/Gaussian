class Distribution:
    '''Generic distribution class for calculating and visualizing probability distribution

        Attributes :
            mean (float) - the mean value of the distribution;
            std  (float) - the standard deviation value of the distribution;
            data (float) - a data file with list of floats;
    '''
    def __init__(self, mean = 0, std = 1):
        self.mean = mean
        self.std = std
        self.data = []

    def read_data(self, filename):
        ''' Function for reading in data. The data should be in a text file and should have one number per line.
            The numbers are stored in a data attribute

            Args :
                filename (string) : name of the file to read from
            ___________
            Returns: 
                None
        '''

        with open(filename) as file:
            data = []
            line = file.readline()
            while line:
                data.append(int(line))
                line = file.readline()
        file.close()

        self.data = data

            