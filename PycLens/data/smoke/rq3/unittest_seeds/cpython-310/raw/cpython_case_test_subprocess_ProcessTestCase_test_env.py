# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    newenv = os.environ.copy()
    newenv['FRUIT'] = 'orange'
    with subprocess.Popen([sys.executable, '-c', 'import sys,os;sys.stdout.write(os.getenv("FRUIT"))'], stdout=subprocess.PIPE, env=newenv) as p:
        (stdout, stderr) = p.communicate()
        self.assertEqual(stdout, b'orange')
