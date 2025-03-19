import subprocess
import EventProducer.config.param as para

for gp in para.gridpacklist:
    cmd = f'ls {para.gp_dir}{gp}.tar.gz'
    p = subprocess.Popen(cmd, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if len(stderr) != 0:
        print(f'GP {gp} does not exist')
