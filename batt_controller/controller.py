#!/usr/bin/env python

red = "\033[1;31m"
green = "\033[1;32m"
clr = "\033[0m"

import sys
import csv

def decomment(csvfile):
    for row in csvfile:
        raw = row.split('#')[0].strip()
        if raw: yield raw

def controller():
    filename = "../output/test_auction.csv"

    cp = []     # clearing price
    cq = []     # clearing quantity
    load = []   # load demand

    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(decomment(csvfile), delimiter=',')
        for row in csvreader:
            cp.append(float(row[1].strip("+")))
            cq.append(float(row[2].strip("+")))

    # print(cp)
    # print(cq)


    load_file = "../loads/load_profile_1.player"

    with open(load_file, newline='') as csvfile:
        csvreader = csv.reader(decomment(csvfile), delimiter=',')
        for row in csvreader:
            load.append(float(row[1].strip()))
    # print(load)

    schedule_file = "./test.schedule"

    batt_out = [0]
    avg_price = 35
    setpoint = 0.55

    # print(len(cp))

    for i in range(1,len(cp)):
        avg_load = sum(load[i*3:i*3+2])/3;
        if cp[i] < avg_price and avg_load < setpoint:
            for j in range(3):
                batt_out.append(-0.4/load[i*3+j])
        else:
            for j in range(3):
                batt_out.append(0.5/load[i*3+j])

    # print(len(batt_out))

    with open(schedule_file, "w+") as f:
        print(green+ "[+] " + clr + "Writing schedule to file " + schedule_file)
        f.write("schedule batt_22_schedule {\n")
        for i in range(0, len(batt_out)-2, 3):
            f.write("\t0-19  {} * * * {} ;\n".format(int(i/3+1), batt_out[i]))
            f.write("\t20-39 {} * * * {} ;\n".format(int(i/3+1), batt_out[i+1]))
            f.write("\t40-59 {} * * * {} ;\n".format(int(i/3+1), batt_out[i+2]))
        f.write("}")
        print(green + "Done!" + clr)

if __name__ == "__main__":
    controller();
