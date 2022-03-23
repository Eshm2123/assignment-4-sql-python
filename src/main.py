import sys
from repository import repo


def main(argv):
    configfile = open(argv[1], 'r')
    configfile = configfile.readlines()
    ordersfile = open(argv[2], 'r')
    ordersfile = ordersfile.readlines()
    outputfile = open(argv[3], 'w')
    amounts = configfile[0].split(',')
    create_data_base(amounts, configfile)
    orders(ordersfile, outputfile)


def create_data_base(amounts, configfile):
    repo.create_tables()
    num_of_hats = int(amounts[0]) + 1
    num_of_suppliers = int(amounts[1]) + num_of_hats
    for hat in range(1, num_of_hats):
        tmp = configfile[hat].split(',')
        repo.hats.insert(tmp)
    for supplier in range(num_of_hats, num_of_suppliers):
        tmp = configfile[supplier].split(',')
        if str(tmp[1]).__contains__('\n'):
            tmp[1] = tmp[1][:len(tmp[1]) - 1]
        repo.suppliers.insert(tmp)


def orders(ordersfile, outputfile):
    length = len(ordersfile)
    output = []
    for order in range(0, length):
        tmp = [order + 1]
        tmp += ordersfile[order].split(",")
        if str(tmp[2]).__contains__('\n'):
            tmp[2] = tmp[2][:len(tmp[2]) - 1]
        output += [repo.execute_order(tmp)]
        repo.orders.insert(tmp)
    for line in output:
        outputfile.write(str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n')


if __name__ == '__main__':
    main(sys.argv)
