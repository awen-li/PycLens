# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_pipe_buf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (x, y) = os.pipe()
    os.close(x)
    os.close(y)
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;sys.stdout.write(sys.stdin.read(47));sys.stderr.write("x" * %d);sys.stdout.write(sys.stdin.read())' % support.PIPE_MAX_SIZE], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stderr.close)
    self.addCleanup(p.stdin.close)
    string_to_write = b'a' * support.PIPE_MAX_SIZE
    (stdout, stderr) = p.communicate(string_to_write)
    self.assertEqual(stdout, string_to_write)
