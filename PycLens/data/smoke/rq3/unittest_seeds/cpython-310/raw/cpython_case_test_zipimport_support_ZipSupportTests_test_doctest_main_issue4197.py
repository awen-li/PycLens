# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipimport_support.py
# case: ZipSupportTests_test_doctest_main_issue4197

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_src = textwrap.dedent('                    class Test:\n                        ">>> \'line 2\'"\n                        pass\n\n                    import doctest\n                    doctest.testmod()\n                    ')
    pattern = 'File "%s", line 2, in %s'
    with os_helper.temp_dir() as d:
        script_name = make_script(d, 'script', test_src)
        (rc, out, err) = assert_python_ok(script_name)
        expected = pattern % (script_name, '__main__.Test')
        if verbose:
            print('Expected line', expected)
            print('Got stdout:')
            print(ascii(out))
        self.assertIn(expected.encode('utf-8'), out)
        (zip_name, run_name) = make_zip_script(d, 'test_zip', script_name, '__main__.py')
        (rc, out, err) = assert_python_ok(zip_name)
        expected = pattern % (run_name, '__main__.Test')
        if verbose:
            print('Expected line', expected)
            print('Got stdout:')
            print(ascii(out))
        self.assertIn(expected.encode('utf-8'), out)
