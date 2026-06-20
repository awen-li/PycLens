# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestReadlineFile:

        def __init__(self, file):
            self.file = file
            self.numcalls = 0

        def readline(self, size=None):
            self.numcalls += 1
            if size:
                return self.file.readline(size)
            else:
                return self.file.readline()

        def __getattr__(self, name):
            file = self.__dict__['file']
            a = getattr(file, name)
            if not isinstance(a, int):
                setattr(self, name, a)
            return a
    f = TestReadlineFile(tempfile.TemporaryFile('wb+'))
    self.addCleanup(f.close)
    f.write(b'x' * 256 * 1024)
    f.seek(0)
    env = {'REQUEST_METHOD': 'PUT'}
    fs = cgi.FieldStorage(fp=f, environ=env)
    self.addCleanup(fs.file.close)
    self.assertGreater(f.numcalls, 2)
    f.close()
