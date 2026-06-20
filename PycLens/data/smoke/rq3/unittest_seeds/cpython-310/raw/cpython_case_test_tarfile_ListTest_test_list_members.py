# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ListTest_test_list_members

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tio = io.TextIOWrapper(io.BytesIO(), 'ascii', newline='\n')

    def members(tar):
        for tarinfo in tar.getmembers():
            if 'reg' in tarinfo.name:
                yield tarinfo
    with support.swap_attr(sys, 'stdout', tio):
        self.tar.list(verbose=False, members=members(self.tar))
    out = tio.detach().getvalue()
    self.assertIn(b'ustar/regtype', out)
    self.assertNotIn(b'ustar/conttype', out)
