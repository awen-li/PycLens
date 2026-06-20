# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipimport_support.py
# case: ZipSupportTests_test_doctest_issue4197

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_src = inspect.getsource(test_doctest)
    test_src = test_src.replace('from test import test_doctest', 'import test_zipped_doctest as test_doctest')
    test_src = test_src.replace('test.test_doctest', 'test_zipped_doctest')
    test_src = test_src.replace('test.sample_doctest', 'sample_zipped_doctest')
    sample_sources = {}
    for mod in [sample_doctest, sample_doctest_no_doctests, sample_doctest_no_docstrings]:
        src = inspect.getsource(mod)
        src = src.replace('test.test_doctest', 'test_zipped_doctest')
        mod_name = mod.__name__.split('.')[-1]
        mod_name = mod_name.replace('sample_', 'sample_zipped_')
        sample_sources[mod_name] = src
    with os_helper.temp_dir() as d:
        script_name = make_script(d, 'test_zipped_doctest', test_src)
        (zip_name, run_name) = make_zip_script(d, 'test_zip', script_name)
        with zipfile.ZipFile(zip_name, 'a') as z:
            for (mod_name, src) in sample_sources.items():
                z.writestr(mod_name + '.py', src)
        if verbose:
            with zipfile.ZipFile(zip_name, 'r') as zip_file:
                print('Contents of %r:' % zip_name)
                zip_file.printdir()
        os.remove(script_name)
        sys.path.insert(0, zip_name)
        import test_zipped_doctest
        try:
            known_good_tests = [test_zipped_doctest.SampleClass, test_zipped_doctest.SampleClass.NestedClass, test_zipped_doctest.SampleClass.NestedClass.__init__, test_zipped_doctest.SampleClass.__init__, test_zipped_doctest.SampleClass.a_classmethod, test_zipped_doctest.SampleClass.a_property, test_zipped_doctest.SampleClass.a_staticmethod, test_zipped_doctest.SampleClass.double, test_zipped_doctest.SampleClass.get, test_zipped_doctest.SampleNewStyleClass, test_zipped_doctest.SampleNewStyleClass.__init__, test_zipped_doctest.SampleNewStyleClass.double, test_zipped_doctest.SampleNewStyleClass.get, test_zipped_doctest.sample_func, test_zipped_doctest.test_DocTest, test_zipped_doctest.test_DocTestParser, test_zipped_doctest.test_DocTestRunner.basics, test_zipped_doctest.test_DocTestRunner.exceptions, test_zipped_doctest.test_DocTestRunner.option_directives, test_zipped_doctest.test_DocTestRunner.optionflags, test_zipped_doctest.test_DocTestRunner.verbose_flag, test_zipped_doctest.test_Example, test_zipped_doctest.test_debug, test_zipped_doctest.test_testsource, test_zipped_doctest.test_trailing_space_in_test, test_zipped_doctest.test_DocTestSuite, test_zipped_doctest.test_DocTestFinder]
            fail_due_to_missing_data_files = [test_zipped_doctest.test_DocFileSuite, test_zipped_doctest.test_testfile, test_zipped_doctest.test_unittest_reportflags]
            for obj in known_good_tests:
                _run_object_doctest(obj, test_zipped_doctest)
        finally:
            del sys.modules['test_zipped_doctest']
