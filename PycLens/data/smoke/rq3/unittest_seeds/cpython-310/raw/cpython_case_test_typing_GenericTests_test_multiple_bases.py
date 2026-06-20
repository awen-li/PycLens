# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_multiple_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MM1(MutableMapping[str, str], collections.abc.MutableMapping):
        pass

    class MM2(collections.abc.MutableMapping, MutableMapping[str, str]):
        pass
    self.assertEqual(MM2.__bases__, (collections.abc.MutableMapping, Generic))
