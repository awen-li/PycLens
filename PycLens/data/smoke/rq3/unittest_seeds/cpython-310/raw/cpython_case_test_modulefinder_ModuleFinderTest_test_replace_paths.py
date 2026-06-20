# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_modulefinder.py
# case: ModuleFinderTest_test_replace_paths

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_path = os.path.join(TEST_DIR, 'a', 'module.py')
    new_path = os.path.join(TEST_DIR, 'a', 'spam.py')
    with support.captured_stdout() as output:
        self._do_test(maybe_test, debug=2, replace_paths=[(old_path, new_path)])
    output = output.getvalue()
    expected = 'co_filename %r changed to %r' % (old_path, new_path)
    self.assertIn(expected, output)
