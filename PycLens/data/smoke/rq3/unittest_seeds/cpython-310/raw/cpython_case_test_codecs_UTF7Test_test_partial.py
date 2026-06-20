# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF7Test_test_partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_partial('a+-b\x00c\x80dĀe𐀀f', ['a', 'a', 'a+', 'a+-', 'a+-b', 'a+-b', 'a+-b', 'a+-b', 'a+-b', 'a+-b\x00', 'a+-b\x00c', 'a+-b\x00c', 'a+-b\x00c', 'a+-b\x00c', 'a+-b\x00c', 'a+-b\x00c\x80', 'a+-b\x00c\x80d', 'a+-b\x00c\x80d', 'a+-b\x00c\x80d', 'a+-b\x00c\x80d', 'a+-b\x00c\x80d', 'a+-b\x00c\x80dĀ', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe', 'a+-b\x00c\x80dĀe𐀀', 'a+-b\x00c\x80dĀe𐀀f'])
