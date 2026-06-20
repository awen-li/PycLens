# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_run_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    newenv = os.environ.copy()
    newenv['FRUIT'] = 'banana'
    cp = self.run_python('import sys, os;sys.exit(33 if os.getenv("FRUIT")=="banana" else 31)', env=newenv)
    self.assertEqual(cp.returncode, 33)
