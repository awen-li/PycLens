# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: HandlerExceptionTest_test_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = expat.ParserCreate()
    parser.StartElementHandler = self.StartElementHandler
    try:
        parser.Parse(b'<a><b><c/></b></a>', True)
        self.fail()
    except RuntimeError as e:
        self.assertEqual(e.args[0], 'a', "Expected RuntimeError for element 'a', but" + ' found %r' % e.args[0])
        entries = traceback.extract_tb(e.__traceback__)
        self.assertEqual(len(entries), 3)
        self.check_traceback_entry(entries[0], 'test_pyexpat.py', 'test_exception')
        self.check_traceback_entry(entries[1], 'pyexpat.c', 'StartElement')
        self.check_traceback_entry(entries[2], 'test_pyexpat.py', 'StartElementHandler')
        if sysconfig.is_python_build() and (not (sys.platform == 'win32' and platform.machine() == 'ARM')):
            self.assertIn('call_with_frame("StartElement"', entries[1][3])
