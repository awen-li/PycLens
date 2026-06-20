# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AifcMiscTest_test_close_opened_files_on_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_aifc_file = findfile('pluck-pcm8.wav', subdir='audiodata')
    with check_no_resource_warning(self):
        with self.assertRaises(aifc.Error):
            self.f = aifc.open(non_aifc_file, 'rb')
        with mock.patch.object(aifc.Aifc_write, 'initfp', side_effect=RuntimeError):
            with self.assertRaises(RuntimeError):
                self.fout = aifc.open(TESTFN, 'wb')
