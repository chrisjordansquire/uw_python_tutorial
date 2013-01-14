import numpy as np
import matplotlib 

#This line just forces matplotlib to not display the drawings and
#instead just write them to file. 
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import sys

def main():
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
        mu = float(sys.argv[2])
        sigma = float(sys.argv[3])
        out = sys.argv[4]
    else:
        N = 500
        mu = 0.1
        sigma = 1
        out = 'out.png' 

    plot_random_walk(N, mu, sigma, out)

def plot_random_walk(N, mu, sigma, out):
    """Generate random walk and save plot to filename out
    """

    #Note matplotlib is an enormous package, with lots of
    #functionality. Fortunately their website is also filled
    #with how to's, and pretty pictures to help you figure
    #out what you want to add to your graphics. 

    plt.ioff()
    ticks = np.arange(N)
    deltas = mu + sigma*np.random.randn(N)

    totals = deltas.cumsum()
    plt.plot(ticks, totals, linewidth=3, color='blue', )
    plt.title('Random Walk Example') 
    plt.xlabel('Iteration') 
    plt.ylabel('Cumulative Sum') 
    plt.savefig(out)

if __name__ == "__main__":
    main() 
