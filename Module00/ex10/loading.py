import sys
import time
from progressbar import ProgressBar


def ft_progress(listy):
    start = time.time()
    length = len(listy)
    i = 0
    prog = "#                   "
    run = 1
    for elem in listy:
        i = i + 1
        perc = (i / length) * 100
        if (perc > 5 * run):
            prog = ""
            for j in range(1, run + 1):
                prog = prog + '#'
            for j in range(run + 1, 20):
                prog = prog + ' '
            run = run + 1
        e_time = time.time() - start
        eta = (e_time / i) * length - e_time
        time.sleep(0.1)
        sys.stdout.write(f"\rETA: {eta:.2f}s [{perc:03.0f}%] ")
        sys.stdout.write(f"[{prog}] {i}/{length} | elapsed time {e_time:.2f}s")
        yield elem


listy = range(100)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
