#!/usr/bin/env sh

for i in `seq 300 25 400`;
	do mkdir /home/silmar/Desktop/udl/advancedai/benchmark/5$i;
	for j in `seq 100`; 
	do
        result= $(echo  %.2f "scale=0; 4.25 * $i" | bc)
		/home/silmar/Desktop/udl/advancedai/satsolver/salsolver1.0/rnd-cnf-gen.py $i $result 3 $j > cnf-100-$i-3-$j.cnf
	done
	mv cnf* /home/silmar/Desktop/udl/advancedai/benchmark/5$i;
done 
