# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlretrieveNetworkTests_test_reporthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    records = []

    def recording_reporthook(blocks, block_size, total_size):
        records.append((blocks, block_size, total_size))
    with self.urlretrieve(self.logo, reporthook=recording_reporthook) as (file_location, fileheaders):
        expected_size = int(fileheaders['Content-Length'])
    records_repr = repr(records)
    self.assertGreater(len(records), 1, msg='There should always be two calls; the first one before the transfer starts.')
    self.assertEqual(records[0][0], 0)
    self.assertGreater(records[0][1], 0, msg="block size can't be 0 in %s" % records_repr)
    self.assertEqual(records[0][2], expected_size)
    self.assertEqual(records[-1][2], expected_size)
    block_sizes = {block_size for (_, block_size, _) in records}
    self.assertEqual({records[0][1]}, block_sizes, msg='block sizes in %s must be equal' % records_repr)
    self.assertGreaterEqual(records[-1][0] * records[0][1], expected_size, msg='number of blocks * block size must be >= total size in %s' % records_repr)
