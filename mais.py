import csv
with open('data.csv', 'r') as csv_file:   # opens the file for reading
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:   # for each line in the csv it creates a temporary value for interest and purpose
        temp = line[16]
        tempinterest = line[5]
        counter = 0
        i = 0

        array =[]
        for i in range (len(array)):   #sees if any purpose in the array is in the file's line
            if array[i][0] == temp:
                counter = counter +1

            if counter == 0:             # if there is no match of purposes, add the purpose to a new line in the array
                newline = len(array) +1
                array[(newline)][0] = temp

                i=1

                while i<4:                         #initialize the rest of the array with zeros
                    array[newline][i] = 0
                    i+= 1
            else:          # if there is a match of purposes add the interest value in the file to the sum
                           # of interest values for that purposes. add one to the number of values
                i = 0

                while i < len(array):
                    if array[i][0] == temp:
                        array[i][1] = array[i][1] + tempinterest
                        array[i][2] += 1


        i=0
        while i< len(array):  # fills out the average section of the array
            total = array[i][1]
            num_values = array[i][2]
            array[i][3] = (total/num_values)


        finalarray= []
        i=0
        while i < len(array):      creates a final array to be written to a csv to be plotted
            finalarray[i][0] = array[i][0]
            finalarray[i][1] = array[i][3]

with open('average.csv','w') as new_file:

    csv_writer = csv.writer(new_file, delimiter=',')
    csv_writer.writerows(finalarray)


#import csv
#with open('average.csv', 'r') as csv_file:
#    csv_reader = csv.reader(csv_file)

#    for line in csv_file:
#        print(line)
