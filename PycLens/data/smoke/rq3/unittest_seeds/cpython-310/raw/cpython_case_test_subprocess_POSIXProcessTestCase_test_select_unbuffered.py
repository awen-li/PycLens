# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_select_unbuffered

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    select = import_helper.import_module('select')
    p = subprocess.Popen([sys.executable, '-c', 'import sys;sys.stdout.write("apple")'], stdout=subprocess.PIPE, bufsize=0)
    f = p.stdout
    self.addCleanup(f.close)
    try:
        self.assertEqual(f.read(4), b'appl')
        self.assertIn(f, select.select([f], [], [], 0.0)[0])
    finally:
        p.wait()
