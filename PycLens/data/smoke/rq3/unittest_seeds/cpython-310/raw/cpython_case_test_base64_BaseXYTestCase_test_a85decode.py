# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_a85decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    tests = {b'': b'', b'GB\\6`E-ZP=Df.1GEb>': b'www.python.org', b'! ! * -\'"\n\t\t9eu\r\n7#  RL\x0bhG$k3[W&.oNg\'GVB"(`=52*$$(B+<_pR,UFcb-n-Vr/1iJ-0JP==1c70M3&s#]4?Ykm5X@_(6q\'R884cEH9MJ8X:f1+h<)lt#=BSg3>[:ZC?t!MSA7]@cBPD3sCi+\'.E,fo>FEMbNG^4U^I!pHnJ:W<)KS>/9Ll%"IN/`jYOHG]iPa.Q$R$jD4S=Q7DTV8*TUnsrdW2ZetXKAY/Yd(L?[\'d?O\\@K2_]Y2%o^qmn*`5Ta:aN;TJbg"GZd*^:jeCE.%f\\,!5gtgiEi8N\\UjQ5OekiqBum-X60nF?)@o_%qPq"ad`r;HT': bytes(range(255)), b'@:E_WAS,RgBkhF"D/O92EH6,BF`qtRH$VbC6UX@47n?3D92&&T:Jand;cHat=\'/U/0JP==1c70M3&r-I,;<FN.OZ`-3]oSW/g+A(H[P': b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}', b'DJpY:@:Wn_DJ(RS': b'no padding..', b'H=_,8+Cf>,E,oN2F(oQ1z': b'zero compression\x00\x00\x00\x00', b'H=_,8+Cf>,E,oN2F(oQ1!!!!': b'zero compression\x00\x00\x00', b'6>q!aA79M(3WK-[!!': b'Boundary:\x00\x00\x00\x00', b';fH/TAKYK$D/aMV+<VdL': b'Space compr:    ', b'rr': b'\xff', b's8N': b'\xff' * 2, b's8W*': b'\xff' * 3, b's8W-!': b'\xff' * 4}
    for (data, res) in tests.items():
        eq(base64.a85decode(data), res, data)
        eq(base64.a85decode(data, adobe=False), res, data)
        eq(base64.a85decode(data.decode('ascii'), adobe=False), res, data)
        eq(base64.a85decode(b'<~' + data + b'~>', adobe=True), res, data)
        eq(base64.a85decode(data + b'~>', adobe=True), res, data)
        eq(base64.a85decode('<~%s~>' % data.decode('ascii'), adobe=True), res, data)
    eq(base64.a85decode(b'yy', foldspaces=True, adobe=False), b' ' * 8)
    eq(base64.a85decode(b'y+<Vd', foldspaces=True, adobe=False), b' ' * 7)
    eq(base64.a85decode(b'y+<U', foldspaces=True, adobe=False), b' ' * 6)
    eq(base64.a85decode(b'y+9', foldspaces=True, adobe=False), b' ' * 5)
    self.check_other_types(base64.a85decode, b'GB\\6`E-ZP=Df.1GEb>', b'www.python.org')
