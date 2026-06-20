# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_errorlevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def extracterror_filter(tarinfo, path):
        raise tarfile.ExtractError('failed with ExtractError')

    def filtererror_filter(tarinfo, path):
        raise tarfile.FilterError('failed with FilterError')

    def oserror_filter(tarinfo, path):
        raise OSError('failed with OSError')

    def tarerror_filter(tarinfo, path):
        raise tarfile.TarError('failed with base TarError')

    def valueerror_filter(tarinfo, path):
        raise ValueError('failed with ValueError')
    with ArchiveMaker() as arc:
        arc.add('file')
    with self.check_context(arc.open(errorlevel=0), extracterror_filter):
        self.expect_file('file')
    with self.check_context(arc.open(errorlevel=0), filtererror_filter):
        self.expect_file('file')
    with self.check_context(arc.open(errorlevel=0), oserror_filter):
        self.expect_file('file')
    with self.check_context(arc.open(errorlevel=0), tarerror_filter):
        self.expect_exception(tarfile.TarError)
    with self.check_context(arc.open(errorlevel=0), valueerror_filter):
        self.expect_exception(ValueError)
    with self.check_context(arc.open(errorlevel=1), extracterror_filter):
        self.expect_file('file')
    with self.check_context(arc.open(errorlevel=1), filtererror_filter):
        self.expect_exception(tarfile.FilterError)
    with self.check_context(arc.open(errorlevel=1), oserror_filter):
        self.expect_exception(OSError)
    with self.check_context(arc.open(errorlevel=1), tarerror_filter):
        self.expect_exception(tarfile.TarError)
    with self.check_context(arc.open(errorlevel=1), valueerror_filter):
        self.expect_exception(ValueError)
    with self.check_context(arc.open(errorlevel=2), extracterror_filter):
        self.expect_exception(tarfile.ExtractError)
    with self.check_context(arc.open(errorlevel=2), filtererror_filter):
        self.expect_exception(tarfile.FilterError)
    with self.check_context(arc.open(errorlevel=2), oserror_filter):
        self.expect_exception(OSError)
    with self.check_context(arc.open(errorlevel=2), tarerror_filter):
        self.expect_exception(tarfile.TarError)
    with self.check_context(arc.open(errorlevel=2), valueerror_filter):
        self.expect_exception(ValueError)
    with self.check_context(arc.open(errorlevel='boo!'), filtererror_filter):
        self.expect_exception(TypeError)
