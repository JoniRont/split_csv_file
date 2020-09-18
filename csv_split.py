import argparse
import os
from pathlib import Path
import csv
import glob
import threading
# to do:
# 1. splitattavan tiedoston tulee sijaita samassa kansiossa
# 2. Päätteen lisääminen tehdään poistamalla 4 viimeistä merkkiä ja korvaamalla ne .csv tekstillä
# 3. tarkista onko tiedostossa tarpeeksi rivejä jakamiseen
# 4. Tarkista jotenkin csv tiedoston tyyppi(onko eu vai amerikka eroittimet)(encode=utf8?)
def get_path():

    my_path = "C:\Python"
    filepath = glob.glob(my_path + '\**\*.csv', recursive=True)
    return filepath

def initialize():
    add_counter_to_name = 0
    data=[]
    # C:\Python\Python basics>py csv_split.py -i scores.csv -o pisteet.csv -r 10
    parser = argparse.ArgumentParser(description="Harjoitus 11.6 split csv file")
    parser.add_argument("-i", help="input file", metavar="only .csv files allowed", required=True)  # all .csv files accepted
    parser.add_argument("-o", help="output file", metavar="only .csv files allowed (default is empty if no value is set: splitfile(s).csv)", default="splitfile.csv")
    parser.add_argument("-r", help="row limit to split", type=int, required=True)
    args = parser.parse_args()

    filepath = get_path()

    args, header, data = read(args, data)

    while len(data) > 0:
        add_counter_to_name = add_counter_to_name + 1  # add counter number to each file end before dot
        write(args, header, data, add_counter_to_name)
    

def read(args, data):
    
    with open(args.i, 'r') as f:
        f_csv = csv.reader(f)
        
        header = next(f_csv)

        for row in f_csv:              
            data.append(row)
    
    return args, header, data

def write(args, header, data, add_counter_to_name):             
        
    counter = 0
    file_row_limit = int(args.r)  # cast args.r to int just in case, even its forced in argument parser

    file_output_name = str(args.o)
    file_output_name = file_output_name[:-4] + str(add_counter_to_name) + ".csv"
    #header = _header
    with open(file_output_name, 'w', newline="") as f:
        writer = csv.writer(f)
        
        writer.writerow(header)
              
        # write rows in file and remove it from the list
        for rows in data[:file_row_limit]:
            data.pop(0)
            if counter > file_row_limit:               
                break      
            counter = counter + 1                                         
            writer.writerow(rows)  
                
    print(f"Taulukko {args.o} on tulostettu! Rivejä tulostettiin {counter}kpl.")
    
initialize()




    