# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadingExceptionTests_test_multithread_modify_file_noerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def modify_file():
        with open(os_helper.TESTFN, 'w', encoding='utf-8') as fp:
            fp.write(' ')
            traceback.format_stack()
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    threads = [threading.Thread(target=modify_file) for i in range(100)]
    for t in threads:
        t.start()
        t.join()
