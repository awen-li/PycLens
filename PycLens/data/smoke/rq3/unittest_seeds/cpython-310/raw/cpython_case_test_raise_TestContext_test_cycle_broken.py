# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_cycle_broken

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        try:
            1 / 0
        except ZeroDivisionError as e:
            raise e
    except ZeroDivisionError as e:
        self.assertIsNone(e.__context__)
