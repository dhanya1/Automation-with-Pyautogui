#!/bin/bash

for fl in *.json; do

cp $fl $fl.old

cat $fl.old | jq --compact-output '.' > ./transformed/$fl

aws kinesis put-record --stream-name invoices --partition-key 123 --data  file://./transformed/$fl

rm -f $fl.old

sleep .5

done
