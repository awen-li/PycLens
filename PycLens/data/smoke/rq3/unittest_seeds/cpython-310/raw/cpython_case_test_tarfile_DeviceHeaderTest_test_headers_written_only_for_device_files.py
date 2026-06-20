# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: DeviceHeaderTest_test_headers_written_only_for_device_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tempdir = os.path.join(TEMPDIR, 'device_header_test')
    os.mkdir(tempdir)
    try:
        tar = tarfile.open(tmpname, self.mode)
        try:
            input_blk = tarfile.TarInfo(name='my_block_device')
            input_reg = tarfile.TarInfo(name='my_regular_file')
            input_blk.type = tarfile.BLKTYPE
            input_reg.type = tarfile.REGTYPE
            tar.addfile(input_blk)
            tar.addfile(input_reg)
        finally:
            tar.close()
        tar = tarfile.open(tmpname, 'r')
        try:
            output_blk = tar.getmember('my_block_device')
            output_reg = tar.getmember('my_regular_file')
        finally:
            tar.close()
        self.assertEqual(output_blk.devmajor, 0)
        self.assertEqual(output_blk.devminor, 0)
        self.assertEqual(output_reg.devmajor, 0)
        self.assertEqual(output_reg.devminor, 0)
        with open(tmpname, 'rb') as infile:
            buf = infile.read()
        buf_blk = buf[output_blk.offset:output_blk.offset_data]
        buf_reg = buf[output_reg.offset:output_reg.offset_data]
        device_headers = slice(329, 329 + 16)
        self.assertEqual(buf_blk[device_headers], b'0000000\x00' * 2)
        self.assertEqual(buf_reg[device_headers], b'\x00' * 16)
    finally:
        os_helper.rmtree(tempdir)
