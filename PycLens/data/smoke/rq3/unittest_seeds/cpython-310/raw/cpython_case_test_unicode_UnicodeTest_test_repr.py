# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not sys.platform.startswith('java'):
        self.assertEqual(repr('abc'), "'abc'")
        self.assertEqual(repr('ab\\c'), "'ab\\\\c'")
        self.assertEqual(repr('ab\\'), "'ab\\\\'")
        self.assertEqual(repr('\\c'), "'\\\\c'")
        self.assertEqual(repr('\\'), "'\\\\'")
        self.assertEqual(repr('\n'), "'\\n'")
        self.assertEqual(repr('\r'), "'\\r'")
        self.assertEqual(repr('\t'), "'\\t'")
        self.assertEqual(repr('\x08'), "'\\x08'")
        self.assertEqual(repr('\'"'), '\'\\\'"\'')
        self.assertEqual(repr('\'"'), '\'\\\'"\'')
        self.assertEqual(repr("'"), '"\'"')
        self.assertEqual(repr('"'), '\'"\'')
        latin1repr = '\'\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\t\\n\\x0b\\x0c\\r\\x0e\\x0f\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17\\x18\\x19\\x1a\\x1b\\x1c\\x1d\\x1e\\x1f !"#$%&\\\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\\x7f\\x80\\x81\\x82\\x83\\x84\\x85\\x86\\x87\\x88\\x89\\x8a\\x8b\\x8c\\x8d\\x8e\\x8f\\x90\\x91\\x92\\x93\\x94\\x95\\x96\\x97\\x98\\x99\\x9a\\x9b\\x9c\\x9d\\x9e\\x9f\\xa0¡¢£¤¥¦§¨©ª«¬\\xad®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\''
        testrepr = repr(''.join(map(chr, range(256))))
        self.assertEqual(testrepr, latin1repr)
        self.assertEqual(repr('𐀀' * 39 + '\uffff' * 4096), repr('𐀀' * 39 + '\uffff' * 4096))

        class WrongRepr:

            def __repr__(self):
                return b'byte-repr'
        self.assertRaises(TypeError, repr, WrongRepr())
