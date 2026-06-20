# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_reraise_cycle_broken

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        try:
            xyzzy
        except NameError as a:
            try:
                1 / 0
            except ZeroDivisionError:
                raise a
    except NameError as e:
        self.assertIsNone(e.__context__.__context__)
