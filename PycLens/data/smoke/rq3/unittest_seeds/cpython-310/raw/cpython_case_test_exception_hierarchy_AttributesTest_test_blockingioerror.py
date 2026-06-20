# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: AttributesTest_test_blockingioerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = ('a', 'b', 'c', 'd', 'e')
    for n in range(6):
        e = BlockingIOError(*args[:n])
        with self.assertRaises(AttributeError):
            e.characters_written
        with self.assertRaises(AttributeError):
            del e.characters_written
    e = BlockingIOError('a', 'b', 3)
    self.assertEqual(e.characters_written, 3)
    e.characters_written = 5
    self.assertEqual(e.characters_written, 5)
    del e.characters_written
    with self.assertRaises(AttributeError):
        e.characters_written
