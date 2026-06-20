# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_pipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add('foo', type=tarfile.FIFOTYPE)
    for filter in ('fully_trusted', 'tar'):
        with self.check_context(arc.open(), filter):
            if hasattr(os, 'mkfifo'):
                self.expect_file('foo', type=tarfile.FIFOTYPE)
            else:
                pass
    with self.check_context(arc.open(), 'data'):
        self.expect_exception(tarfile.SpecialFileError, "'foo' is a special file")
