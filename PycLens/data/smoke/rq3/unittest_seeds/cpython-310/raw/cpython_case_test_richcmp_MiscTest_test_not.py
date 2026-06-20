# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: MiscTest_test_not

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import operator

    class Exc(Exception):
        pass

    class Bad:

        def __bool__(self):
            raise Exc

    def do(bad):
        not bad
    for func in (do, operator.not_):
        self.assertRaises(Exc, func, Bad())
