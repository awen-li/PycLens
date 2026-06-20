# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_sly_relative0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add('../moo', symlink_to='..//tmp/moo')
    try:
        with self.check_context(arc.open(), filter='fully_trusted'):
            if os_helper.can_symlink():
                if isinstance(self.raised_exception, FileExistsError):
                    self.expect_exception(FileExistsError)
                else:
                    self.expect_file('../moo', symlink_to='..//tmp/moo')
            else:
                pass
    except FileExistsError:
        pass
    for filter in ('tar', 'data'):
        with self.check_context(arc.open(), filter):
            self.expect_exception(tarfile.OutsideDestinationError, "'../moo' would be extracted to " + "'.*moo', which is outside " + 'the destination')
