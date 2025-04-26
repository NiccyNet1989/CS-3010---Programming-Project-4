def read_file(path):
    try:
        with open(path, 'r') as file:
            contents = file.read()
            contents = contents.split()
            return contents

    except FileNotFoundError:
        print("Error: File was not found")
        return []
    except Exception as e:
        print("Error: An unexpected exception occured")
        return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = read_file("input2.txt")

    # for index in range(len(data)):
    #     print(data[index])

    xValuesInitial = data[:(len(data) // 2)]
    yValuesInitial = data[(len(data) // 2):]

    # print(xValuesInitial)
    # print(yValuesInitial)

    denominatorPyramid = []
