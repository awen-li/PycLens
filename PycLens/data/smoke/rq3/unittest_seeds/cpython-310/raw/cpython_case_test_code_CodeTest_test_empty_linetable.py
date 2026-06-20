# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CodeTest_test_empty_linetable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        pass
    new_code = code = func.__code__.replace(co_linetable=b'')
    self.assertEqual(list(new_code.co_lines()), [])
