import csv
import os
from postgresql.models import Molwt

def run():
    file = open('/Users/benst.john/Desktop/postgre/postgre/scripts/MolWtSol.csv')
    read_file=csv.reader(file)

    Molwt.objects.all().delete()

    count=1

    for record in read_file:
        if count==1:
            pass
        else:
            print(record) 
            Molwt.objects.create(MolLogP=record[0],MoltWt=record[1],NumRotatableBonds=record[2],AromaticProportion=record[3])
        cunt=count+1