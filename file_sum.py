# Author: Faith Elledge
# Githubuser: Elledgef
# Date: 10/25/22
# Description: This code will create num.txt using values given in class and will create sum.txt that will display the
#the sum of all values in num.txt



def file_sum(num_list):
    """ Creates num.txt and calculates the sum of the numbers in num.txt in sum.txt"""
    total = 0
    num_list = [23.77, 116, 94, -12.8, 0, 14.999]
    with open('num.txt', 'w') as outfile:
        for num in num_list:
            outfile.write(str(num) + "\n")
    with open('num.txt', 'r') as infile:
        for line in infile:
             numbers = line.split(',')
    with open('sum.txt', 'w') as outfile:
        for num in num_list:
            total += float(num)
        outfile.write(str(total)+'\n')

if __name__ == '__main__':
    file_sum('num_list')














