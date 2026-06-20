# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_call_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    newenv = os.environ.copy()
    newenv['FRUIT'] = 'banana'
    rc = subprocess.call([sys.executable, '-c', 'import sys, os;sys.exit(os.getenv("FRUIT")=="banana")'], env=newenv)
    self.assertEqual(rc, 1)
