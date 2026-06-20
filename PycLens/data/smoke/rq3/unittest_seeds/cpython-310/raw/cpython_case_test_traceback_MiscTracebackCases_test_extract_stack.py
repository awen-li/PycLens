# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: MiscTracebackCases_test_extract_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def extract():
        return traceback.extract_stack()
    result = extract()
    lineno = extract.__code__.co_firstlineno
    self.assertEqual(result[-2:], [(__file__, lineno + 2, 'test_extract_stack', 'result = extract()'), (__file__, lineno + 1, 'extract', 'return traceback.extract_stack()')])
    self.assertEqual(len(result[0]), 4)
