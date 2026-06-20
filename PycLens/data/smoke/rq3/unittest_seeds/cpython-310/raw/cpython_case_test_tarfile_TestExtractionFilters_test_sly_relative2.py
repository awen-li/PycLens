# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_sly_relative2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add('tmp/')
        arc.add('tmp/../../moo', symlink_to='tmp/../..//tmp/moo')
    with self.check_context(arc.open(), 'fully_trusted'):
        self.expect_file('tmp', type=tarfile.DIRTYPE)
        if os_helper.can_symlink():
            self.expect_file('../moo', symlink_to='tmp/../../tmp/moo')
    for filter in ('tar', 'data'):
        with self.check_context(arc.open(), filter):
            self.expect_exception(tarfile.OutsideDestinationError, "'tmp/../../moo' would be extracted to " + '[\'"].*moo[\'"], which is outside the ' + 'destination')
