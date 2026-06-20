# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_preexec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;sys.stdout.write(os.getenv("FRUIT"))'], stdout=subprocess.PIPE, preexec_fn=lambda : os.putenv('FRUIT', 'apple'))
    with p:
        self.assertEqual(p.stdout.read(), b'apple')
