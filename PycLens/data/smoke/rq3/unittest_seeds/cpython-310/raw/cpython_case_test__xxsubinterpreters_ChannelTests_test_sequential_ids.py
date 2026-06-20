# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_sequential_ids

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before = interpreters.channel_list_all()
    id1 = interpreters.channel_create()
    id2 = interpreters.channel_create()
    id3 = interpreters.channel_create()
    after = interpreters.channel_list_all()
    self.assertEqual(id2, int(id1) + 1)
    self.assertEqual(id3, int(id2) + 1)
    self.assertEqual(set(after) - set(before), {id1, id2, id3})
