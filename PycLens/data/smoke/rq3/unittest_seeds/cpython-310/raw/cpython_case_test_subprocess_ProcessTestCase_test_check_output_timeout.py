# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_check_output_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(subprocess.TimeoutExpired) as c:
        output = subprocess.check_output([sys.executable, '-c', "import sys, time\nsys.stdout.write('BDFL')\nsys.stdout.flush()\ntime.sleep(3600)"], timeout=3)
        self.fail('Expected TimeoutExpired.')
    self.assertEqual(c.exception.output, b'BDFL')
