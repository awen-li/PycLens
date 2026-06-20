# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_del___main__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    with open(filename, 'w', encoding='utf-8') as script:
        print('import sys', file=script)
        print("del sys.modules['__main__']", file=script)
    assert_python_ok(filename)
