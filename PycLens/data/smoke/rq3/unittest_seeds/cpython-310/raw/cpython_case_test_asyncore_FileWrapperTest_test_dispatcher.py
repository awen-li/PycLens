# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: FileWrapperTest_test_dispatcher

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    data = []

    class FileDispatcher(asyncore.file_dispatcher):

        def handle_read(self):
            data.append(self.recv(29))
    s = FileDispatcher(fd)
    os.close(fd)
    asyncore.loop(timeout=0.01, use_poll=True, count=2)
    self.assertEqual(b''.join(data), self.d)
