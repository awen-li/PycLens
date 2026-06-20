# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_shuffle_random_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    shuffle = self.gen.shuffle
    mock_random = unittest.mock.Mock(return_value=0.5)
    seq = bytearray(b'abcdefghijk')
    with self.assertWarns(DeprecationWarning):
        shuffle(seq, mock_random)
    mock_random.assert_called_with()
