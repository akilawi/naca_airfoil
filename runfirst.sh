#!/bin/bash
./run.sh $1 $2 $3 $4 $5 $6
echo "done run"
angle_start="$1"
angle_stop="$2"
n_angles="$3"
n_nodes="$4"
n_levels="$5"
speed="$6"

anglediff=$((($angle_stop-$angle_start)/$n_angles))
for i in `seq 0 $n_angles`;
do
  angle=$(($angle_start + $anglediff*i))
  python dolfin-convert.py "/home/ubuntu/naca_airfoil/msh/r0a""$angle""n""$4"".msh" "/home/ubuntu/naca_airfoil/xml/""$angle"".xml"
  echo "convert %i done"
done

for i in `seq 0 $n_angles`;
do
  angle=$(($angle_start + $anglediff*i))
  ./home/ubuntu/naca_airfoil/navier_stokes_solver/airfoil 10 0.0001 "$speed". 1 /home/ubuntu/naca_airfoil/navier_stokes_solver/"$angle"".xml"
  cp /home/ubuntu/naca_airfoil/navier_stokes_solver/results/drag_ligt.m /home/ubuntu/naca_airfoil/navier_stokes_solver/results/"$angle"".m"
done
