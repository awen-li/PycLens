# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_coding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ch = os_helper.FS_NONASCII
    cmd = f"# coding: latin1\nprint(ascii('{ch}'))"
    res = assert_python_ok('-c', cmd)
    self.assertEqual(res.out.rstrip(), ascii(ch).encode('ascii'))
