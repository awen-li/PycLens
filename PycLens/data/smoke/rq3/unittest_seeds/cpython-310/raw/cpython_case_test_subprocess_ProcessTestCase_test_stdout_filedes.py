# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stdout_filedes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tf = tempfile.TemporaryFile()
    self.addCleanup(tf.close)
    d = tf.fileno()
    p = subprocess.Popen([sys.executable, '-c', 'import sys; sys.stdout.write("orange")'], stdout=d)
    p.wait()
    os.lseek(d, 0, 0)
    self.assertEqual(os.read(d, 1024), b'orange')
