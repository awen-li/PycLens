# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_os_popen_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os.popen('%s -c \'echo "line1\nline2\nline3"\'' % unix_shell) as popen:
        it = iter(popen)
        self.assertEqual(next(it), 'line1\n')
        self.assertEqual(next(it), 'line2\n')
        self.assertEqual(next(it), 'line3\n')
        self.assertRaises(StopIteration, next, it)
