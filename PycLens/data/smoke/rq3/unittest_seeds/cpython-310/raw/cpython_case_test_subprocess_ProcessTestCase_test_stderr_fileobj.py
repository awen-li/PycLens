# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_stderr_fileobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tf = tempfile.TemporaryFile()
    self.addCleanup(tf.close)
    p = subprocess.Popen([sys.executable, '-c', 'import sys; sys.stderr.write("strawberry")'], stderr=tf)
    p.wait()
    tf.seek(0)
    self.assertEqual(tf.read(), b'strawberry')
