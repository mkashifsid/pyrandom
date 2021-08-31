# Server Monitoring Metrics

The server is used for SSL offloading and proxies around 25000 requests per second, 
as the server involves in SSL offloading operation so it uses CPU cycles, in this
case we need to monitor CPU and I/O of the server.
Below are some metrics in linux which will help to understand it.

## mpstat

mpstat is a command that is used to report processor related statistics. 
It accurately displays the statistics of the CPU usage of the system. 
It displays information about CPU utilization and performance. 
It initializes the first processor with CPU 0, the second one with CPU 1, and so on,
and from the output of this command we need to check the values of **%sys** and **%iowait**.
**%sys** shows how much CPU is utilizing.
**%iowait** shows the percentage of time that the CPU or CPUs were idle during
which the system had an outstanding disk I/O request.
To display CPU utilization for all the cores,
```
mpstat -P ALL
```
sample output
```
19:46:01     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
19:46:01     all   20.45    0.01   14.99    0.06    0.00    0.66    0.00    0.00    0.00   63.83
19:46:01       0   14.03    0.00   10.33    0.09    0.00    0.55    0.00    0.00    0.00   74.99
19:46:01       1   24.29    0.01   17.93    0.05    0.00    0.62    0.00    0.00    0.00   57.11
19:46:01       2   23.85    0.01   17.33    0.05    0.00    1.28    0.00    0.00    0.00   57.48
19:46:01       3   24.17    0.00   17.63    0.04    0.00    0.29    0.00    0.00    0.00   57.87
```

To display CPU utilization by a specific processor,
```
mpstat -P 0
```
sample output
```
11:14:23     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
11:14:23       0   14.45    0.00   10.53    0.09    0.00    0.56    0.00    0.00    0.00   74.36
```
## sar

sar is used to track the activities performed in a computer system in real time.
It shows the almost similar results as mpstat but in real time.
Below command will show the real time value for every 5 seconds,
```
sar -u 5
```
sample output
```
11:16:38        CPU     %user     %nice   %system   %iowait    %steal     %idle
11:16:43        all     17.65      0.00     12.15      0.00      0.00     70.20
11:16:48        all     28.25      0.00     16.21      0.05      0.00     55.49
11:16:53        all     20.23      0.00     12.90      0.05      0.00     66.82
```
## iostat

The iostat command without arguments, it will display information about CPU usage, 
and I/O statistics for every partition on the system.
In iostat we can monitor Throughput per second (tps) and read/write per second.
Below command will show the stats,
```
iostat
```
sample output
```
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          30.90    0.01   23.41    0.05    0.00   45.63

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
loop0             0.00         0.00         0.00        520          0
loop1             0.00         0.00         0.00         46          0
loop2             0.00         0.00         0.00        505          0
loop3             0.00         0.00         0.00       1157          0
loop4             0.05         0.05         0.00      18573          0
loop5             0.00         0.00         0.00       1196          0
loop6             0.00         0.00         0.00       1536          0
loop7             0.00         0.00         0.00        116          0
sda               3.60         9.39       305.91    3188529  103863216
dm-0              5.23         9.36       304.26    3177617  103301628
dm-1              5.12         9.35       319.80    3174885  108576812
```
