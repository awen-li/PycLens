# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ListTest_test_list_verbose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tio = io.TextIOWrapper(io.BytesIO(), 'ascii', newline='\n')
    with support.swap_attr(sys, 'stdout', tio):
        self.tar.list(verbose=True)
    out = tio.detach().getvalue()
    self.assertRegex(out, b'\\?rw-r--r-- tarfile/tarfile\\s+7011 \\d{4}-\\d\\d-\\d\\d\\s+\\d\\d:\\d\\d:\\d\\d ustar/\\w+type ?\\r?\\n' * 2)
    self.assertIn(b'ustar/symtype -> regtype', out)
    self.assertIn(b'./ustar/linktest2/symtype -> ../linktest1/regtype', out)
    self.assertIn(b'./ustar/linktest2/lnktype link to ./ustar/linktest1/regtype', out)
    self.assertIn(b'gnu' + b'/123' * 125 + b'/longlink link to gnu' + b'/123' * 125 + b'/longname', out)
    self.assertIn(b'pax' + b'/123' * 125 + b'/longlink link to pax' + b'/123' * 125 + b'/longname', out)
