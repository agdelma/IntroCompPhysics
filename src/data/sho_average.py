'''
sho_average.py
Compute the average energy of the simple harmonic osscilator from an input
file
'''

import math

# -----------------------------------------------------------------------------
def sho_energy(T):
    '''Return the energy of a simple harmonic osscilator at temperature T.'''
    # \hbar \omega / k_B = 1
    return 0.5/math.tanh(0.5/T)


# -----------------------------------------------------------------------------
def main():
    # open the file for reading
    data_file = open('sho_energy.dat', 'r')

    # get the column labels
    data_labels = data_file.readline()

    # split it at the spaces
    labels = data_labels.split()

    # remove the comment character
    labels.remove('#')

    # create an empty dictionary that will hold the data
    data = {}

    # initialize it with empty lists
    for label in labels:
        data[label] = []

    # go through each line of the file
    for line in data_file.readlines():
        # get a list of columns
        values = line.split()

        # go through each value, convert to float and add to our list
        for n,value in enumerate(values):
            data[labels[n]].append(float(value))

    # close the file
    data_file.close()

    # now that we have all the data, we can compute the averages
    data_average = {}
    for label in labels:
        data_average[label] = 0.0

        for value in data[label]:
            data_average[label] += value

        data_average[label] /= len(data[label])

    print('Total Energy = %6.3f K' % (data_average['Kinetic'] + data_average['Potential']))
    print('Exact Energy = %6.3f K' % sho_energy(0.5))

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
