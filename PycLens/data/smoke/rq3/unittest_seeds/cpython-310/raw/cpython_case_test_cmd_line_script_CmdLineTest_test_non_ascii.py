# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os_helper.TESTFN_UNDECODABLE and sys.platform not in ('win32', 'darwin'):
        name = os.fsdecode(os_helper.TESTFN_UNDECODABLE)
    elif os_helper.TESTFN_NONASCII:
        name = os_helper.TESTFN_NONASCII
    else:
        self.skipTest('need os_helper.TESTFN_NONASCII')
    source = 'print(ascii(__file__))\n'
    script_name = _make_test_script(os.getcwd(), name, source)
    self.addCleanup(os_helper.unlink, script_name)
    (rc, stdout, stderr) = assert_python_ok(script_name)
    self.assertEqual(ascii(script_name), stdout.rstrip().decode('ascii'), 'stdout=%r stderr=%r' % (stdout, stderr))
    self.assertEqual(0, rc)
