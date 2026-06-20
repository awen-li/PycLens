# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_pipesize_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys; sys.stdin.read(); sys.stdout.write("out"); sys.stderr.write("error!")'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, pipesize=-1)
    try:
        (fp_r, fp_w) = os.pipe()
        try:
            default_pipesize = fcntl.fcntl(fp_w, fcntl.F_GETPIPE_SZ)
            for fifo in [p.stdin, p.stdout, p.stderr]:
                self.assertEqual(fcntl.fcntl(fifo.fileno(), fcntl.F_GETPIPE_SZ), default_pipesize)
        finally:
            os.close(fp_r)
            os.close(fp_w)
        p.stdin.close()
    finally:
        p.kill()
        p.wait()
