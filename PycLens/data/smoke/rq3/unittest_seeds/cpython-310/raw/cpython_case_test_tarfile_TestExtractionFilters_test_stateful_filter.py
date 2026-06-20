# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_stateful_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class StatefulFilter:

        def __enter__(self):
            self.num_files_processed = 0
            return self

        def __call__(self, tarinfo, path):
            try:
                tarinfo = tarfile.data_filter(tarinfo, path)
            except tarfile.FilterError:
                return None
            self.num_files_processed += 1
            return tarinfo

        def __exit__(self, *exc_info):
            self.done = True
    with ArchiveMaker() as arc:
        arc.add('good')
        arc.add('bad', symlink_to='/')
        arc.add('good')
    with StatefulFilter() as custom_filter:
        with self.check_context(arc.open(), custom_filter):
            self.expect_file('good')
    self.assertEqual(custom_filter.num_files_processed, 2)
    self.assertEqual(custom_filter.done, True)
