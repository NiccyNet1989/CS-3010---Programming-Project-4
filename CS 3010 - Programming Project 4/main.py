# First create a function which reads in the contents of the txt file
def read_file(path):
    try:
        with open(path, 'r') as file:
            contents = file.read()
            contents = contents.split()
            contents = [float(element) for element in contents]
            return contents

    except FileNotFoundError:
        print("Error: File was not found")
        return []
    except Exception as e:
        print("Error: An unexpected exception occured")
        return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use function to read in file contents
    data = read_file("input2.txt")

    # for index in range(len(data)):
    #     print(data[index])


    # Now split input file into two arrays
    xValuesInitial = data[:(len(data) // 2)]
    yValuesInitial = data[(len(data) // 2):]

    # print(xValuesInitial)
    # print(yValuesInitial)


    # Begin calculating pyramid
    # First, find denominators and numerators
    denominatorPyramid = []
    order = 1
    index = 0

    while len(xValuesInitial) - order != 0:
        # Create a temporary array to add to the denominatorPyramid
        denominators = [0] * (len(xValuesInitial)-order)

        # Initial case when there is no previous array to copy from
        if order == 1:
            for i in range(len(denominators)):
                denominators[i] = xValuesInitial[index + order] - xValuesInitial[index]
                index = index + 1
            denominatorPyramid.append(denominators)
            order = order + 1
        else:
            # Now calculate cases past initial case
            index = 0
            for i in range(len(denominators)):
                denominators[i] = (xValuesInitial[index + order] - xValuesInitial[index])
                index = index + 1
            denominatorPyramid.append(denominators)
            order = order + 1


        # Now, find numerator pyramid
        # Divided difference pyramid must be calculated in parallel
            #This is because each next order of numerators is dependent on the previous order of divided differences
        