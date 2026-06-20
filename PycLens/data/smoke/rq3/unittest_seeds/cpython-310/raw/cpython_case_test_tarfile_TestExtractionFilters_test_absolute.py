# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_absolute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add(self.outerdir / 'escaped.evil')
    with self.check_context(arc.open(), 'fully_trusted'):
        self.expect_file('../escaped.evil')
    for filter in ('tar', 'data'):
        with self.check_context(arc.open(), filter):
            if str(self.outerdir).startswith('/'):
                outerdir_stripped = str(self.outerdir).lstrip('/')
                self.expect_file(f'{outerdir_stripped}/escaped.evil')
            else:
                self.expect_exception(tarfile.AbsolutePathError, '[\'"].*escaped.evil[\'"] has an absolute path')
