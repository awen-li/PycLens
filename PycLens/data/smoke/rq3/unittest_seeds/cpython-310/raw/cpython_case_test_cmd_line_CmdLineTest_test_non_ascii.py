# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    command = 'assert(ord(%r) == %s)' % (os_helper.FS_NONASCII, ord(os_helper.FS_NONASCII))
    assert_python_ok('-c', command)
