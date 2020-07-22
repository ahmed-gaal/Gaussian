import math
import matplotlib.pyplot as plt 
from general import Distribution

class Gaussian(Distribution):
    ''' Gaussian distribution class for calculating and visualizing Gaussian distribution

        Attributes :
            mean (float) - the mean;
            std  (float) - the standard deviation;
            data (float) - a data file with list of floats;
    '''
    def __init__(self, mean = 0, std = 1):
        self.mean = mean
        self.std = std
        self.data = []

    def calculate_mean(self):
        ''' Function for calculating the mean
            Args : None
            _________
            Returns :
                (float) : mean of the data
        '''
        avg = 1 * sum(self.data) / len(self.data)

        self.mean = avg

        return self.mean

    def calculate_std(self, sample = True):
        ''' Function for calculating the standard deviation
            Args : 
                Sample (bool) : whether data represents sample or population
            _________
            Returns:
                (float) : standard deviation of the data
        '''
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean
        std = 0

        for i in self.data:
            std += (i - mean) ** 2

        std = math.sqrt(std/n)

        self.std = std

        return self.std
    
    def read_data(self, filename, sample = True):
        ''' Function for reading data from a text file .
            The text file should have one number per line.
            The numbers are stored in a data attributes. After reading the data,
            mean and standard deviation are calculated.

            Args : 
                filename (string) : name of the file to read from;
            _________
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
        self.mean = self.calculate_mean()
        self.std = self.calculate_std(sample)

    def plot_hist(self):
        ''' Function for plotting histogram of the instance variable data using the Matplotlib library
            Args:
                None
            _________
            Returns:
                None
        '''

        plt.hist(self.data)
        plt.title('Histogram of the data')
        plt.xlabel('Data')
        plt.ylabel('Count')
    
    def pdf(self, x):
        ''' Probability density function calculator for Gaussian distribution
            Args:
                x (float) : point for calculating the probability density function;
            _________
            Returns: 
                float : probability density function output
        '''

        return (1 / (self.std * math.sqrt(2 * math.pi))) * math.exp(-.5 * ((x - self.mean) / self.std) ** 2) 

    def plot_hist_pdf(self, n_spaces = 50):
        ''' Function to plot a normalized histogram of the data and a plot of the probability density function along same range
            Args:
                n_spaces (int) : number of data points;
            _________
            Returns:
                list : x values for the probability density function plot
                list : y values for the probability density function plot
        '''

        min_range = min(self.data)
        max_range = max(self.data) 

        # Calculate the interval between x values 

        interval =  1 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # Calculate x and y values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # Making plots  
        fig, axes = plt.subplots(2, sharex = True)
        fig.subplots_adjust (hspace = .5) 
        axes[0].hist(self.data, density = True)
        axes[0].set_title('Normal Histogram of data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y) 
        axes[1].set_title('Normal Distribution for \n sample mean & standard deviation') 
        axes[1].set_ylabel('Density')
        plt.show()

        return x, y  
    
    def __add__(self, other):
        ''' Function for adding two Gaussian distributions
            Args: 
                Other (Gaussian) : Gaussian Instance
            ___________
            Returns:
                Gaussian Distribution
        '''

        result = Gaussian()
        result.mean = self.mean + other.mean 
        result.std = math.sqrt(self.std ** 2 + other.std ** 2)

        return result
    
    def __repr__(self):
        ''' Function ro output characteristics of gaussian instance
            Args:
                None
            _____________
            Returns:
                string : characteristics of Gaussian 
        '''

        return 'Mean {}, Standard Deviation {}'.format(self.mean, self.std)