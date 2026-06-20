# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_update2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.environ.clear()
    os.environ.update(HELLO='World')
    with os.popen("%s -c 'echo $HELLO'" % unix_shell) as popen:
        value = popen.read().strip()
        self.assertEqual(value, 'World')
