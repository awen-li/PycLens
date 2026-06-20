# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_file_functions.py
# case: UnicodeFileTests_test_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirname = os.path.join(os_helper.TESTFN, 'Grüß-曨曩曫')
    filename = 'ß-曨曩曫'
    with os_helper.temp_cwd(dirname):
        with open(filename, 'wb') as f:
            f.write((filename + '\n').encode('utf-8'))
        os.access(filename, os.R_OK)
        os.remove(filename)
