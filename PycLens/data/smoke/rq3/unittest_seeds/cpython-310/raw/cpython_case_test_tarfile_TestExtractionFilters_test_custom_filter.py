# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_custom_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def custom_filter(tarinfo, path):
        self.assertIs(path, self.destdir)
        if tarinfo.name == 'move_this':
            return tarinfo.replace(name='moved')
        if tarinfo.name == 'ignore_this':
            return None
        return tarinfo
    with ArchiveMaker() as arc:
        arc.add('move_this')
        arc.add('ignore_this')
        arc.add('keep')
    with self.check_context(arc.open(), custom_filter):
        self.expect_file('moved')
        self.expect_file('keep')
