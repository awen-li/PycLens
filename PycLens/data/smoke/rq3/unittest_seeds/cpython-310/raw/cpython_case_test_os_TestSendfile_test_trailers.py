# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_trailers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTFN2 = os_helper.TESTFN + '2'
    file_data = b'abcdef'
    self.addCleanup(os_helper.unlink, TESTFN2)
    create_file(TESTFN2, file_data)
    with open(TESTFN2, 'rb') as f:
        os.sendfile(self.sockno, f.fileno(), 0, 5, trailers=[b'123456', b'789'])
        self.client.close()
        self.server.wait()
        data = self.server.handler_instance.get_data()
        self.assertEqual(data, b'abcde123456789')
