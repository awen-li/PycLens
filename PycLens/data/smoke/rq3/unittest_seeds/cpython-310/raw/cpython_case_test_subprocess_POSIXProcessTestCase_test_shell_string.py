# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_shell_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    newenv = os.environ.copy()
    newenv['FRUIT'] = 'apple'
    p = subprocess.Popen('echo $FRUIT', shell=1, stdout=subprocess.PIPE, env=newenv)
    with p:
        self.assertEqual(p.stdout.read().strip(b' \t\r\n\x0c'), b'apple')
