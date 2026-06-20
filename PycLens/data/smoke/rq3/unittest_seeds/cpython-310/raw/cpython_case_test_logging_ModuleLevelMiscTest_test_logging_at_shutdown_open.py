# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ModuleLevelMiscTest_test_logging_at_shutdown_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    code = textwrap.dedent(f'\n            import builtins\n            import logging\n\n            class A:\n                def __del__(self):\n                    logging.error("log in __del__")\n\n            # basicConfig() opens the file, but logging.shutdown() closes\n            # it at Python exit. When A.__del__() is called,\n            # FileHandler._open() must be called again to re-open the file.\n            logging.basicConfig(filename={filename!r}, encoding="utf-8")\n\n            a = A()\n\n            # Simulate the Python finalization which removes the builtin\n            # open() function.\n            del builtins.open\n        ')
    assert_python_ok('-c', code)
    with open(filename, encoding='utf-8') as fp:
        self.assertEqual(fp.read().rstrip(), 'ERROR:root:log in __del__')
