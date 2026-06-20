# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetDefaultTempdir_test_no_files_left_behind

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryDirectory() as our_temp_directory:

        def our_candidate_list():
            return [our_temp_directory]
        with support.swap_attr(tempfile, '_candidate_tempdir_list', our_candidate_list):
            tempfile._get_default_tempdir()
            self.assertEqual(os.listdir(our_temp_directory), [])

            def raise_OSError(*args, **kwargs):
                raise OSError()
            with support.swap_attr(os, 'open', raise_OSError):
                with self.assertRaises(FileNotFoundError):
                    tempfile._get_default_tempdir()
                self.assertEqual(os.listdir(our_temp_directory), [])
            with support.swap_attr(os, 'write', raise_OSError):
                with self.assertRaises(FileNotFoundError):
                    tempfile._get_default_tempdir()
                self.assertEqual(os.listdir(our_temp_directory), [])
