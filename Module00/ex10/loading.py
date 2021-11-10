import sys
import time


def ft_progress(listy):
    start = time.time()
    length = len(listy)
    i = 0
    prog = "#                   "
    run = 1
    s = ""
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
        s0 = s
        s = f"ETA: {eta:.2f}s [{perc:03.0f}%] [{prog}] {i}/{length} | elapsed time {e_time:.2f}s"
        if (len(s) < len(s0)):
            for k in range(0, len(s0) - len(s)):
                s = s + " "
        sys.stdout.write(f"\r{s}")
        sys.stdout.flush()
        yield elem


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
