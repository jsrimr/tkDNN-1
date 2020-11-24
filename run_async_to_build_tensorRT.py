import os
import glob
import subprocess
from threading import Thread

# cfgs = glob.glob(r"tests/darknet/cfg/target_*.cfg")
cfgs = glob.glob(r"tests/darknet/cfg/mb_*.cfg")
# cfgs = glob.glob(r"tests/darknet/new_cfg/*")

n = 1 # 몇번 반복할 것인지
# build/test_custom_cfgbuilder tests/darknet/cfg/target_*.cfg [n_iteration]

def run_nsys(cfg, n):
    # tests/darknet/cfg/target_5_6.cfg
    # build/target_5_6.cfg_fp16.rt
    basename = os.path.basename(cfg)
    path = os.path.join('build', basename)
    if os.path.exists(path + "_fp16.rt"):
        os.remove(path + "_fp16.rt")
        print(f"removed {basename}_fp16.rt")
    
    process = subprocess.run(
            ['build/test_custom_cfgbuilder',f'{cfg}', str(n)],
            stdout=subprocess.PIPE,
            universal_newlines=True)
    print(process)

for cfg in cfgs:
    print(f"Let's run {cfg}")
    t = Thread(target=run_nsys, args=(cfg, n))
    t.start()