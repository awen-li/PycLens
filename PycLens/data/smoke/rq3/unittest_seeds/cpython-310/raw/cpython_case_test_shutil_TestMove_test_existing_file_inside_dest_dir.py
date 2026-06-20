# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_existing_file_inside_dest_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.dst_file, 'wb'):
        pass
    self.assertRaises(shutil.Error, shutil.move, self.src_file, self.dst_dir)
