#! /usr/bin/gnuplot --persist

set terminal x11 noenhanced background rgb 'white' font 'FreeSerif, 20' size 1000, 500
set tics font 'FreeSerif, 20'
set datafile separator ','
set datafile commentschars "%"

# Labels
set ylabel 'Power (Watt)' # label for the Y axis
set xlabel 'Time' # label for the X axis
set xtics rotate
set key outside right center 
set tmargin 3


set grid
set xzeroaxis lt 1 lc rgb 'black'
plot x

set linetype 9 lc rgb "#ff6666"

# Time data
set xdata time # tells gnuplot the x axis is time data
set timefmt '%Y-%m-%d %H:%M:%S PDT' # specify our time string format
set format x '%H:%M:%S' # otherwise it will show only MM:SS


# Plot lines
# plot ARG1 using 1:4 with lines lw 3
plot for [i=2:10] ARG1 skip 7 using 1:i with lines lw 3 title columnheader
