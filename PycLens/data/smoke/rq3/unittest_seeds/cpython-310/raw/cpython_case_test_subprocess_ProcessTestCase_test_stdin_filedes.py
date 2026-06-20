# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stdin_filedes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tf = tempfile.TemporaryFile()
    self.addCleanup(tf.close)
    d = tf.fileno()
    os.write(d, b'pear')
    os.lseek(d, 0, 0)
    p = subprocess.Popen([sys.executable, '-c', 'import sys; sys.exit(sys.stdin.read() == "pear")'], stdin=d)
    p.wait()
    self.assertEqual(p.returncode, 1)
