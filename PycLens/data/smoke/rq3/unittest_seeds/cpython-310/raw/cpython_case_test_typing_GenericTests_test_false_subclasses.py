# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_false_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyMapping(MutableMapping[str, str]):
        pass
    self.assertNotIsInstance({}, MyMapping)
    self.assertNotIsSubclass(dict, MyMapping)
