# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: MiscTests_test_getoutput

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(subprocess.getoutput('echo xyzzy'), 'xyzzy')
    self.assertEqual(subprocess.getstatusoutput('echo xyzzy'), (0, 'xyzzy'))
    dir = None
    try:
        dir = tempfile.mkdtemp()
        name = os.path.join(dir, 'foo')
        (status, output) = subprocess.getstatusoutput(('type ' if mswindows else 'cat ') + name)
        self.assertNotEqual(status, 0)
    finally:
        if dir is not None:
            os.rmdir(dir)
