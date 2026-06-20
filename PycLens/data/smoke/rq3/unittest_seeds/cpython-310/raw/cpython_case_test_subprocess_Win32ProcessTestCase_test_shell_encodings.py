# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_shell_encodings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for enc in ['ansi', 'oem']:
        newenv = os.environ.copy()
        newenv['FRUIT'] = 'physalis'
        p = subprocess.Popen('set', shell=1, stdout=subprocess.PIPE, env=newenv, encoding=enc)
        with p:
            self.assertIn('physalis', p.stdout.read(), enc)
