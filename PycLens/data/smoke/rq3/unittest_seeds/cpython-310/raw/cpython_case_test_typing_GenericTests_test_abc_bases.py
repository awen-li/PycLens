# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_abc_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MM(MutableMapping[str, str]):

        def __getitem__(self, k):
            return None

        def __setitem__(self, k, v):
            pass

        def __delitem__(self, k):
            pass

        def __iter__(self):
            return iter(())

        def __len__(self):
            return 0
    MM().update()
    self.assertIsInstance(MM(), collections.abc.MutableMapping)
    self.assertIsInstance(MM(), MutableMapping)
    self.assertNotIsInstance(MM(), List)
    self.assertNotIsInstance({}, MM)
