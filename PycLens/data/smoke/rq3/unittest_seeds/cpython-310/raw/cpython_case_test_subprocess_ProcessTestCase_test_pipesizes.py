# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_pipesizes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (test_pipe_r, test_pipe_w) = os.pipe()
    try:
        pipesize_default = fcntl.fcntl(test_pipe_w, fcntl.F_GETPIPE_SZ)
    finally:
        os.close(test_pipe_r)
        os.close(test_pipe_w)
    pipesize = pipesize_default // 2
    if pipesize < 512:
        raise unittest.SkipTest('default pipesize too small to perform test.')
    p = subprocess.Popen([sys.executable, '-c', 'import sys; sys.stdin.read(); sys.stdout.write("out"); sys.stderr.write("error!")'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, pipesize=pipesize)
    try:
        for fifo in [p.stdin, p.stdout, p.stderr]:
            self.assertEqual(fcntl.fcntl(fifo.fileno(), fcntl.F_GETPIPE_SZ), pipesize)
        p.stdin.write(b'pear')
        p.stdin.close()
    finally:
        p.kill()
        p.wait()
