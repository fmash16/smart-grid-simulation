#!/usr/bin/python3

load = [0.655 , 0.625 , 0.595 , 0.545 , 0.510 , 0.480 , 0.405 , 0.385 , 0.380
        , 0.335 , 0.300 , 0.315 , 0.325 , 0.355 , 0.355 , 0.360 , 0.360 , 0.365
        , 0.390 , 0.425 , 0.455 , 0.475 , 0.480 , 0.495 , 0.515 , 0.525 , 0.530
        , 0.530 , 0.530 , 0.530 , 0.555 , 0.575 , 0.595 , 0.600 , 0.610 , 0.615
        , 0.645 , 0.680 , 0.695 , 0.710 , 0.735 , 0.745 , 0.755 , 0.770 , 0.775
        , 0.715 , 0.720 , 0.650 , 0.620 , 0.590 , 0.560 , 0.545 , 0.535 , 0.515
        , 0.515 , 0.525 , 0.525 , 0.535 , 0.540 , 0.550 , 0.575 , 0.590 , 0.625
        , 0.645 , 0.665 , 0.690 , 0.720 , 0.740 , 0.765 , 0.740 , 0.725 , 0.685
        , 0.650]

load_new = [ 3760 ,3760 ,3760 ,3760 ,3760 ,3760 ,3745 ,3545 ,3545 ,3545 ,3545
        ,3545 ,3485 ,3485 ,3485 ,3485 ,3485 ,3485 ,3485 ,3485 ,3470 ,3470 ,3470
        ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470
        ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470
        ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3470 ,3843 ,3843 ,3843 ,3843 ,3843
        ,3843 ,3843 ,3843 ,3843 ,3878 ,3878 ,3878 ,3505 ,3505 ,3505 ,3505 ,3505
        ,3505 ,3505 ,2065 ,2065 ,2065 ,2065 ,2065 ,2065 ,2065 ,2065 ,565  ,565 
        ,565  ,565  ,565  ,580  ,500  ,700  ,700  ,700  ,700  ,715  ,715  ,715 
        ,715  ,715  ,700  ,700  ,425  ,425  ,365  ,365  ,365  ,365  ,365  ,365 
        ,365  ,365  ,365  ,365  ,365  ,365  ,365  ,365  ,365  ,580  ,580  ,580 
        ,580  ,580  ,580  ,580  ,580  ,580  ,580  ,580  ,580  ,580  ,565  ,565 
        ,565  ,565  ,565  ,565  ,565  ,565  ,565  ,565  ,565  ,550  ,610  ,610 
        ,410  ,410  ,410  ,410  ,410  ,410  ,410  ,410  ,410  ,410  ,410  ,410 
        ,410  ,410  ,410  ,425  ,425  ,425  ,425  ,425  ,425  ,425  ,1925 ,1925
        ,1925 ,2185 ,2185 ,2185 ,2185 ,2185 ,2185 ,2185 ,2185 ,2185 ,2185 ,2185
        ,2385 ,2385 ,2370 ,2370 ,2370 ,2370 ,2370 ,2370 ,2170 ,2170 ,2170 ,670 
        ,670  ,670  ,670  ,730  ,530  ,530  ,530  ,530  ,530  ,530  ,530  ,730 
        ,730  ,730  ,730  ,730  ,730  ,730  ,730  ,730  ,745  ,745  ,745  ,765 
        ,765  ,765  ,705  ,705  ,705  ,720  ,720  ,720  ,720  ,720  ,720  ,720 
        ,740  ,815  ,1015 ,1015 ,1015 ,1015 ,1015 ,1015 ,1015 ,1015 ,1015 ,1015
        ,815  ,815  ,2315 ,2315 ,2255 ,2255 ,2255 ,2255 ,2235 ,2235 ,2235 ,2235
        ,2235 ,2235 ,2235 ,2235 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435
        ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435 ,2435
        ,2420 ,2420 ,2420 ,2440 ,2440 ,2440 ,2440 ,2440 ,3940 ,3940 ,3740 ,3720
        ,3520 ,3520 ]

time_new = [ "2019-09-30 00:00:00", "2019-09-30 00:05:00", "2019-09-30 00:10:00", "2019-09-30 00:15:00", "2019-09-30 00:20:00", "2019-09-30 00:25:00", "2019-09-30 00:30:00", "2019-09-30 00:35:00", "2019-09-30 00:40:00", "2019-09-30 00:45:00", "2019-09-30 00:50:00", "2019-09-30 00:55:00", "2019-09-30 01:00:00", "2019-09-30 01:05:00", "2019-09-30 01:10:00", "2019-09-30 01:15:00", "2019-09-30 01:20:00", "2019-09-30 01:25:00", "2019-09-30 01:29:59", "2019-09-30 01:34:59", "2019-09-30 01:39:59", "2019-09-30 01:44:59", "2019-09-30 01:49:59", "2019-09-30 01:54:59", "2019-09-30 01:59:59", "2019-09-30 02:04:59", "2019-09-30 02:09:59", "2019-09-30 02:14:59", "2019-09-30 02:19:59", "2019-09-30 02:24:59", "2019-09-30 02:29:59", "2019-09-30 02:34:59", "2019-09-30 02:39:59", "2019-09-30 02:44:59", "2019-09-30 02:49:59", "2019-09-30 02:54:59", "2019-09-30 02:59:59", "2019-09-30 03:04:59", "2019-09-30 03:09:59", "2019-09-30 03:14:59", "2019-09-30 03:19:59", "2019-09-30 03:24:59", "2019-09-30 03:29:59", "2019-09-30 03:34:59", "2019-09-30 03:39:59", "2019-09-30 03:44:59", "2019-09-30 03:49:59", "2019-09-30 03:54:59", "2019-09-30 03:59:59", "2019-09-30 04:04:59", "2019-09-30 04:09:59", "2019-09-30 04:14:59", "2019-09-30 04:19:59", "2019-09-30 04:24:59", "2019-09-30 04:29:59", "2019-09-30 04:34:59", "2019-09-30 04:39:59", "2019-09-30 04:44:59", "2019-09-30 04:49:59", "2019-09-30 04:54:59", "2019-09-30 04:59:59", "2019-09-30 05:04:59", "2019-09-30 05:09:59", "2019-09-30 05:14:59", "2019-09-30 05:19:59", "2019-09-30 05:24:59", "2019-09-30 05:29:59", "2019-09-30 05:34:59", "2019-09-30 05:39:59", "2019-09-30 05:44:59", "2019-09-30 05:49:59", "2019-09-30 05:54:59", "2019-09-30 05:59:59", "2019-09-30 06:04:59", "2019-09-30 06:09:59", "2019-09-30 06:14:59", "2019-09-30 06:19:59", "2019-09-30 06:24:59", "2019-09-30 06:29:59", "2019-09-30 06:34:59", "2019-09-30 06:39:59", "2019-09-30 06:44:59", "2019-09-30 06:49:59", "2019-09-30 06:54:59", "2019-09-30 06:59:59", "2019-09-30 07:04:59", "2019-09-30 07:09:59", "2019-09-30 07:14:59", "2019-09-30 07:19:59", "2019-09-30 07:24:59", "2019-09-30 07:29:59", "2019-09-30 07:34:59", "2019-09-30 07:39:59", "2019-09-30 07:44:59", "2019-09-30 07:49:59", "2019-09-30 07:54:59", "2019-09-30 07:59:59", "2019-09-30 08:04:59", "2019-09-30 08:09:59", "2019-09-30 08:14:59", "2019-09-30 08:19:59", "2019-09-30 08:24:59", "2019-09-30 08:29:59", "2019-09-30 08:34:59", "2019-09-30 08:39:59", "2019-09-30 08:44:59", "2019-09-30 08:49:59", "2019-09-30 08:54:59", "2019-09-30 08:59:59", "2019-09-30 09:04:59", "2019-09-30 09:09:59", "2019-09-30 09:14:59", "2019-09-30 09:19:59", "2019-09-30 09:24:59", "2019-09-30 09:29:59", "2019-09-30 09:34:59", "2019-09-30 09:39:59", "2019-09-30 09:44:59", "2019-09-30 09:49:59", "2019-09-30 09:54:59", "2019-09-30 09:59:59", "2019-09-30 10:04:59", "2019-09-30 10:09:59", "2019-09-30 10:14:59", "2019-09-30 10:19:59", "2019-09-30 10:24:59", "2019-09-30 10:29:59", "2019-09-30 10:34:59", "2019-09-30 10:39:59", "2019-09-30 10:44:59", "2019-09-30 10:49:59", "2019-09-30 10:54:59", "2019-09-30 10:59:59", "2019-09-30 11:04:59", "2019-09-30 11:09:59", "2019-09-30 11:14:59", "2019-09-30 11:19:59", "2019-09-30 11:24:59", "2019-09-30 11:29:59", "2019-09-30 11:34:59", "2019-09-30 11:39:59", "2019-09-30 11:44:59", "2019-09-30 11:49:59", "2019-09-30 11:54:59", "2019-09-30 11:59:59", "2019-09-30 12:04:59", "2019-09-30 12:09:59", "2019-09-30 12:14:59", "2019-09-30 12:19:59", "2019-09-30 12:24:59", "2019-09-30 12:29:59", "2019-09-30 12:34:59", "2019-09-30 12:39:59", "2019-09-30 12:44:59", "2019-09-30 12:49:59", "2019-09-30 12:54:59", "2019-09-30 12:59:59", "2019-09-30 13:04:59", "2019-09-30 13:09:59", "2019-09-30 13:14:59", "2019-09-30 13:19:59", "2019-09-30 13:24:59", "2019-09-30 13:29:59", "2019-09-30 13:34:59", "2019-09-30 13:39:59", "2019-09-30 13:44:59", "2019-09-30 13:49:59", "2019-09-30 13:54:59", "2019-09-30 13:59:59", "2019-09-30 14:04:59", "2019-09-30 14:09:59", "2019-09-30 14:14:59", "2019-09-30 14:19:59", "2019-09-30 14:24:59", "2019-09-30 14:29:59", "2019-09-30 14:34:59", "2019-09-30 14:39:59", "2019-09-30 14:44:59", "2019-09-30 14:49:59", "2019-09-30 14:54:59", "2019-09-30 14:59:59", "2019-09-30 15:04:59", "2019-09-30 15:09:59", "2019-09-30 15:14:59", "2019-09-30 15:19:59", "2019-09-30 15:24:59", "2019-09-30 15:29:59", "2019-09-30 15:34:59", "2019-09-30 15:39:59", "2019-09-30 15:44:59", "2019-09-30 15:49:59", "2019-09-30 15:54:59", "2019-09-30 15:59:59", "2019-09-30 16:04:59", "2019-09-30 16:09:59", "2019-09-30 16:14:59", "2019-09-30 16:19:59", "2019-09-30 16:24:59", "2019-09-30 16:29:59", "2019-09-30 16:34:59", "2019-09-30 16:39:59", "2019-09-30 16:44:59", "2019-09-30 16:49:59", "2019-09-30 16:54:59", "2019-09-30 16:59:59", "2019-09-30 17:04:59", "2019-09-30 17:09:59", "2019-09-30 17:14:59", "2019-09-30 17:19:59", "2019-09-30 17:24:59", "2019-09-30 17:29:59", "2019-09-30 17:34:59", "2019-09-30 17:39:59", "2019-09-30 17:44:59", "2019-09-30 17:49:59", "2019-09-30 17:54:59", "2019-09-30 17:59:59", "2019-09-30 18:04:59", "2019-09-30 18:09:59", "2019-09-30 18:14:59", "2019-09-30 18:19:59", "2019-09-30 18:24:59", "2019-09-30 18:29:59", "2019-09-30 18:34:59", "2019-09-30 18:39:59", "2019-09-30 18:44:59", "2019-09-30 18:49:59", "2019-09-30 18:54:59", "2019-09-30 18:59:59", "2019-09-30 19:04:59", "2019-09-30 19:09:59", "2019-09-30 19:14:59", "2019-09-30 19:19:59", "2019-09-30 19:24:59", "2019-09-30 19:29:59", "2019-09-30 19:34:59", "2019-09-30 19:39:59", "2019-09-30 19:44:59", "2019-09-30 19:49:59", "2019-09-30 19:54:59", "2019-09-30 19:59:59", "2019-09-30 20:04:59", "2019-09-30 20:09:59", "2019-09-30 20:14:59", "2019-09-30 20:19:59", "2019-09-30 20:24:59", "2019-09-30 20:29:59", "2019-09-30 20:34:59", "2019-09-30 20:39:59", "2019-09-30 20:44:59", "2019-09-30 20:49:59", "2019-09-30 20:54:59", "2019-09-30 20:59:59", "2019-09-30 21:04:59", "2019-09-30 21:09:59", "2019-09-30 21:14:59", "2019-09-30 21:19:59", "2019-09-30 21:24:59", "2019-09-30 21:29:59", "2019-09-30 21:34:59", "2019-09-30 21:39:59", "2019-09-30 21:44:59", "2019-09-30 21:49:59", "2019-09-30 21:54:59", "2019-09-30 21:59:59", "2019-09-30 22:04:59", "2019-09-30 22:09:59", "2019-09-30 22:14:59", "2019-09-30 22:19:59", "2019-09-30 22:24:59", "2019-09-30 22:29:59", "2019-09-30 22:34:59", "2019-09-30 22:39:59", "2019-09-30 22:44:59", "2019-09-30 22:49:59", "2019-09-30 22:54:59", "2019-09-30 22:59:59", "2019-09-30 23:04:59", "2019-09-30 23:09:59", "2019-09-30 23:14:59", "2019-09-30 23:19:59", "2019-09-30 23:24:59", "2019-09-30 23:29:59", "2019-09-30 23:34:59", "2019-09-30 23:39:59", "2019-09-30 23:44:59", "2019-09-30 23:49:59", "2019-09-30 23:54:59", "2019-10-01 00:00:00"] 
time = ["2019-09-30 00:01:00", "2019-09-30 00:20:00", "2019-09-30 00:40:00",
        "2019-09-30 01:00:00", "2019-09-30 01:20:00", "2019-09-30 01:40:00",
        "2019-09-30 02:00:00", "2019-09-30 02:20:00", "2019-09-30 02:40:00",
        "2019-09-30 03:00:00", "2019-09-30 03:20:00", "2019-09-30 03:40:00",
        "2019-09-30 04:00:00", "2019-09-30 04:20:00", "2019-09-30 04:40:00",
        "2019-09-30 05:00:00", "2019-09-30 05:20:00", "2019-09-30 05:40:00",
        "2019-09-30 06:00:00", "2019-09-30 06:20:00", "2019-09-30 06:40:00",
        "2019-09-30 07:00:00", "2019-09-30 07:20:00", "2019-09-30 07:40:00",
        "2019-09-30 08:00:00", "2019-09-30 08:20:00", "2019-09-30 08:40:00",
        "2019-09-30 09:00:00", "2019-09-30 09:20:00", "2019-09-30 09:40:00",
        "2019-09-30 10:00:00", "2019-09-30 10:20:00", "2019-09-30 10:40:00",
        "2019-09-30 11:00:00", "2019-09-30 11:20:00", "2019-09-30 11:40:00",
        "2019-09-30 12:00:00", "2019-09-30 12:20:00", "2019-09-30 12:40:00",
        "2019-09-30 13:00:00", "2019-09-30 13:20:00", "2019-09-30 13:40:00",
        "2019-09-30 14:00:00", "2019-09-30 14:20:00", "2019-09-30 14:40:00",
        "2019-09-30 15:00:00", "2019-09-30 15:20:00", "2019-09-30 15:40:00",
        "2019-09-30 16:00:00", "2019-09-30 16:20:00", "2019-09-30 16:40:00",
        "2019-09-30 17:00:00", "2019-09-30 17:20:00", "2019-09-30 17:40:00",
        "2019-09-30 18:00:00", "2019-09-30 18:20:00", "2019-09-30 18:40:00",
        "2019-09-30 19:00:00", "2019-09-30 19:20:00", "2019-09-30 19:40:00",
        "2019-09-30 20:00:00", "2019-09-30 20:20:00", "2019-09-30 20:40:00",
        "2019-09-30 21:00:00", "2019-09-30 21:20:00", "2019-09-30 21:40:00",
        "2019-09-30 22:00:00", "2019-09-30 22:20:00", "2019-09-30 22:40:00",
        "2019-09-30 23:00:00", "2019-09-30 23:20:00", "2019-09-30 23:40:00",
        "2019-09-30 00:00:00" ]

print(len(time_new))
print(len(load_new))

import random
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter 

def moving_avg(x, n):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[n:] - cumsum[:-n]) / float(n)


for i in range(55):
    result_load_new = []
    for j in range(len(load_new)):
        if load_new[j] <= load_new[j-1]:
            factor = random.uniform(1, 1.1)
        else:
            factor = random.uniform(0.9, 1)
        result_load_new.append(round(load_new[j]*factor, 4))
    
    # load_new_filtered = moving_avg(result_load_new, 1)
    load_new_filtered = savgol_filter(result_load_new, 11, 2)

    with open('load_profile_%s.player' % str(i+1), 'a') as f:
        for k in range(len(load_new)):
            print(time_new[k] + ', ' + str(round(load_new_filtered[k], 4)))
            f.writelines(time_new[k] + ', ' + str(round(load_new_filtered[k], 4)) + "\n")

