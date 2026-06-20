# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: StatAttributeTests_test_statvfs_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = os.statvfs(self.fname)
    self.assertEqual(result.f_bfree, result[3])
    members = ('bsize', 'frsize', 'blocks', 'bfree', 'bavail', 'files', 'ffree', 'favail', 'flag', 'namemax')
    for (value, member) in enumerate(members):
        self.assertEqual(getattr(result, 'f_' + member), result[value])
    self.assertTrue(isinstance(result.f_fsid, int))
    self.assertEqual(len(result), 10)
    try:
        result.f_bfree = 1
        self.fail('No exception raised')
    except AttributeError:
        pass
    try:
        result.parrot = 1
        self.fail('No exception raised')
    except AttributeError:
        pass
    try:
        result2 = os.statvfs_result((10,))
        self.fail('No exception raised')
    except TypeError:
        pass
    try:
        result2 = os.statvfs_result((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    except TypeError:
        pass
