# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    init(C)
    init(P)
    global TEST_ALL, DEBUG
    TEST_ALL = arith if arith is not None else is_resource_enabled('decimal')
    DEBUG = debug
    if todo_tests is None:
        test_classes = all_tests
    else:
        test_classes = [CIBMTestCases, PyIBMTestCases]
    for filename in os.listdir(directory):
        if '.decTest' not in filename or filename.startswith('.'):
            continue
        (head, tail) = filename.split('.')
        if todo_tests is not None and head not in todo_tests:
            continue
        tester = lambda self, f=filename: self.eval_file(directory + f)
        setattr(CIBMTestCases, 'test_' + head, tester)
        setattr(PyIBMTestCases, 'test_' + head, tester)
        del filename, head, tail, tester
    try:
        run_unittest(*test_classes)
        if todo_tests is None:
            from doctest import IGNORE_EXCEPTION_DETAIL
            savedecimal = sys.modules['decimal']
            if C:
                sys.modules['decimal'] = C
                run_doctest(C, verbose, optionflags=IGNORE_EXCEPTION_DETAIL)
            sys.modules['decimal'] = P
            run_doctest(P, verbose)
            sys.modules['decimal'] = savedecimal
    finally:
        if C:
            C.setcontext(ORIGINAL_CONTEXT[C])
        P.setcontext(ORIGINAL_CONTEXT[P])
        if not C:
            warnings.warn('C tests skipped: no module named _decimal.', UserWarning)
        if not orig_sys_decimal is sys.modules['decimal']:
            raise TestFailed("Internal error: unbalanced number of changes to sys.modules['decimal'].")
