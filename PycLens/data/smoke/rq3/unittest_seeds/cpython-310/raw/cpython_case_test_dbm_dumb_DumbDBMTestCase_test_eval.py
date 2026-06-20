# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_eval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(_fname + '.dir', 'w', encoding='utf-8') as stream:
        stream.write("str(print('Hacked!')), 0\n")
    with support.captured_stdout() as stdout:
        with self.assertRaises(ValueError):
            with dumbdbm.open(_fname) as f:
                pass
        self.assertEqual(stdout.getvalue(), '')
