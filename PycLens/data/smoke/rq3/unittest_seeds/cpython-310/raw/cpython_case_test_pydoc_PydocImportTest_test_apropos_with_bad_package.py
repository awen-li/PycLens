# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_apropos_with_bad_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkgdir = os.path.join(TESTFN, 'syntaxerr')
    os.mkdir(pkgdir)
    badsyntax = os.path.join(pkgdir, '__init__') + os.extsep + 'py'
    with open(badsyntax, 'w') as f:
        f.write('invalid python syntax = $1\n')
    with self.restrict_walk_packages(path=[TESTFN]):
        with captured_stdout() as out:
            with captured_stderr() as err:
                pydoc.apropos('xyzzy')
        self.assertEqual(out.getvalue(), '')
        self.assertEqual(err.getvalue(), '')
        with captured_stdout() as out:
            with captured_stderr() as err:
                pydoc.apropos('syntaxerr')
        self.assertEqual(out.getvalue().strip(), 'syntaxerr')
        self.assertEqual(err.getvalue(), '')
