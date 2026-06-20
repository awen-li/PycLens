# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_apropos_with_unreadable_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.unreadable_dir = os.path.join(TESTFN, 'unreadable')
    os.mkdir(self.unreadable_dir, 0)
    self.addCleanup(os.rmdir, self.unreadable_dir)
    with self.restrict_walk_packages(path=[TESTFN]):
        with captured_stdout() as out:
            with captured_stderr() as err:
                pydoc.apropos('SOMEKEY')
    self.assertEqual(out.getvalue(), '')
    self.assertEqual(err.getvalue(), '')
