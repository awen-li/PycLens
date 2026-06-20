# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: IOTests_test_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def stuff(a: IO) -> AnyStr:
        return a.readline()
    a = stuff.__annotations__['a']
    self.assertEqual(a.__parameters__, (AnyStr,))
