# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_absolute_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add('parent', symlink_to=self.outerdir)
        arc.add('parent/evil')
    with self.check_context(arc.open(), 'fully_trusted'):
        if os_helper.can_symlink():
            self.expect_file('parent', symlink_to=self.outerdir)
            self.expect_file('../evil')
        else:
            self.expect_file('parent/evil')
    with self.check_context(arc.open(), 'tar'):
        if os_helper.can_symlink():
            self.expect_exception(tarfile.OutsideDestinationError, "'parent/evil' would be extracted to " + '[\'"].*evil[\'"], which is outside ' + 'the destination')
        else:
            self.expect_file('parent/evil')
    with self.check_context(arc.open(), 'data'):
        self.expect_exception(tarfile.AbsoluteLinkError, "'parent' is a symlink to an absolute path")
