#!/bin/bash
./run.sh $1 $2 $3 $4 $5

angle_start="$1"
angle_stop="$2"
n_angles="$3"
n_nodes="$4"
n_levels="$5"

anglediff=$((($angle_stop-$angle_start)/$n_angles))
for i in `seq 0 $n_angles`;
do
  angle=$(($angle_start + $anglediff*i))
  python dolfin-convert.py "/home/ubuntu/naca_airfoil/msh/r0a""$angle""n""$4"".xml" "/home/ubuntu/naca_airfoil/xml/""$angle"".xml"
done
