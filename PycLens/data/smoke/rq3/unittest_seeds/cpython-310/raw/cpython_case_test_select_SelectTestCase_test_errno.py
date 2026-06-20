# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_select.py
# case: SelectTestCase_test_errno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(__file__, 'rb') as fp:
        fd = fp.fileno()
        fp.close()
        try:
            select.select([fd], [], [], 0)
        except OSError as err:
            self.assertEqual(err.errno, errno.EBADF)
        else:
            self.fail('exception not raised')
