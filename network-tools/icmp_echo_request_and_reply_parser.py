import subprocess


output = subprocess.check_output('ping -c %s -W %s -t %s 8.8.8.8' % (self.numPings, (self.pingTimeout * 1000), self.maxWaitTime), shell=True)

output = output.split('\n')[-3:]
# -1 is a blank line, -3 & -2 contain the actual results

xmit_stats = output[0].split(",")
timing_stats = output[1].split("=")[1].split("/")

packet_loss = float(xmit_stats[2].split("%")[0])

ping_min = float(timing_stats[0])
ping_avg = float(timing_stats[1])
ping_max = float(timing_stats[2])
