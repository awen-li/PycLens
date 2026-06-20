# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestTraceback_test_accepts_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tb = get_tb()
    try:
        raise IndexError().with_traceback(tb)
    except IndexError as e:
        self.assertNotEqual(e.__traceback__, tb)
        self.assertEqual(e.__traceback__.tb_next, tb)
    else:
        self.fail('No exception raised')
