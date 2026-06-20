# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestChannels_test_list_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(interpreters.list_all_channels(), [])
    created = set()
    for _ in range(3):
        ch = interpreters.create_channel()
        created.add(ch)
    after = set(interpreters.list_all_channels())
    self.assertEqual(after, created)
