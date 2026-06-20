# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_parent_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add('current', symlink_to='.')
        arc.add('parent', symlink_to='current/..')
        arc.add('parent/evil')
    if os_helper.can_symlink():
        with self.check_context(arc.open(), 'fully_trusted'):
            if self.raised_exception is not None:
                self.expect_exception(FileExistsError)
                return
            else:
                self.expect_file('current', symlink_to='.')
                self.expect_file('parent', symlink_to='current/..')
                self.expect_file('../evil')
        with self.check_context(arc.open(), 'tar'):
            self.expect_exception(tarfile.OutsideDestinationError, '\'parent/evil\' would be extracted to [\'"].*evil[\'"], ' + 'which is outside the destination')
        with self.check_context(arc.open(), 'data'):
            self.expect_exception(tarfile.LinkOutsideDestinationError, '\'parent\' would link to [\'"].*outerdir[\'"], ' + 'which is outside the destination')
    else:
        with self.check_context(arc.open(), 'fully_trusted'):
            self.expect_file('parent/evil')
        with self.check_context(arc.open(), 'tar'):
            self.expect_file('parent/evil')
        with self.check_context(arc.open(), 'data'):
            self.expect_file('parent/evil')
