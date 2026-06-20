# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_benign_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with ArchiveMaker() as arc:
        arc.add('benign.txt')
    for filter in ('fully_trusted', 'tar', 'data'):
        with self.check_context(arc.open(), filter):
            self.expect_file('benign.txt')
