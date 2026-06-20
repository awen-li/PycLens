# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_workers_available_cores

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('sys.argv', new=[sys.executable, self.directory, '-j0']):
        compileall.main()
        self.assertTrue(compile_dir.called)
        self.assertEqual(compile_dir.call_args[-1]['workers'], 0)
