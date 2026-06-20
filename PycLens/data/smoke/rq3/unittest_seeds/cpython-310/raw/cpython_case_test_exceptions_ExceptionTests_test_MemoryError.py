# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_MemoryError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import traceback
    from _testcapi import raise_memoryerror

    def raiseMemError():
        try:
            raise_memoryerror()
        except MemoryError as e:
            tb = e.__traceback__
        else:
            self.fail('Should have raised a MemoryError')
        return traceback.format_tb(tb)
    tb1 = raiseMemError()
    tb2 = raiseMemError()
    self.assertEqual(tb1, tb2)
