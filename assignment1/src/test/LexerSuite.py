import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_1(self):
        """test identifiers"""
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1))

    def test_2(self):
        """test comments"""
        input = """
        //abc 
        b5 //id
        """
        expect = "b5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 2))

    def test_3(self):
        """test comments"""
        input = """
           /* abcd */
           /* // 1234 */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 3))

    def test_4(self):
        """test comments"""
        input = """
           /* xyz */ // */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 4))

    def test_5(self):
        """test skip"""
        input = """
           \t\f\r\b\n \t \r \n
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 5))
    
    def test_6(self):
        """test skip"""
        input = """
           \t\f\r i
           //exp
        """
        expect = "i,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 6))

    def test_7(self):
        """test skip"""
        input = """
           \t\f
           \r\b
           \n \t \r \n
           ////
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 7))

    def test_8(self):
        """test identifiers"""
        input = """
           a1cb AA _1_a b __ 98_a
        """
        expect = "a1cb,AA,_1_a,b,__,98,_a,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 8))

    def test_9(self):
        """test identifiers"""
        input = """
           1r
        """
        expect = "1,r,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 9))

    def test_10(self):
        """test identifiers"""
        input = """
           $er
        """
        expect = "Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 10))
    def test_11(self):
        """test identifiers"""
        input = """
           b~c
        """
        expect = "b,Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 11))

    def test_12(self):
        """test identifiers"""
        input = """
           ac_#
        """
        expect = "ac_,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 12))
    
    def test_13(self):
        """test identifiers"""
        input = """
           =mm
        """
        expect = "=,mm,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 13))
    
    def test_14(self):
        """test identifiers"""
        input = """
           a__b cd
        """
        expect = "a__b,cd,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 14))

    def test_15(self):
        """test identifiers"""
        input = "ac_ 123a 4"
        expect = "ac_,123,a,4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 15))
    
    def test_16(self):
        """test identifiers"""
        input = "a1_ 10 ^"
        expect = "a1_,10,Error Token ^"
        self.assertTrue(TestLexer.test(input, expect, 16))

    def test_17(self):
        """test identifiers"""
        input = "& a1_ 10 ^"
        expect = "Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 17))
    
    def test_18(self):
        """test keyword"""
        input = """
            auto integer string void array
            while out else do for function
            false true
        """
        expect = "auto,integer,string,void,array,while,out,else,do,for,function,false,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 18))

    def test_19(self):
        """test keyword"""
        input = """
            break boolean
        """
        expect = "break,boolean,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 19))

    def test_20(self):
        """test operators"""
        input = """
            + - /
        """
        expect = "+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 20))

    def test_21(self):
        """test operators"""
        input = """
            && %
        """
        expect = "&&,%,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 21))
    
    def test_22(self):
        """test operators"""
        input = """
            || &&
        """
        expect = "||,&&,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 22))

    def test_23(self):
        """test operators"""
        input = """
            != < >
        """
        expect = "!=,<,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 23))

    def test_24(self):
        """test operators"""
        input = """
            :: >=
        """
        expect = "::,>=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 24))
    
    def test_25(self):
        """test operators"""
        input = """
            <= ! 
        """
        expect = "<=,!,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 25))
    
    def test_26(self):
        """test seperators"""
        input = """
            {}
        """
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 26))
    
    def test_27(self):
        """test seperators"""
        input = """
            []
        """
        expect = "[,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 27))

    def test_28(self):
        """test seperators"""
        input = """
            ()
        """
        expect = "(,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 28))
    
    def test_29(self):
        """test seperators"""
        input = """
            ,
        """
        expect = ",,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 29))
    
    def test_30(self):
        """test seperators"""
        input = """
            .
        """
        expect = ".,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 30))
    
    def test_31(self):
        """test seperators"""
        input = """
            ;
        """
        expect = ";,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 31))
    
    def test_32(self):
        """test seperators"""
        input = """
            :
        """
        expect = ":,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 32))

    def test_33(self):
        """test literal"""
        input = """
            0 10 1_2_301 1_2 1_0_0
        """
        expect = "0,10,12301,12,100,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 33))
    
    def test_34(self):
        """test literal"""
        input = """
            0 10 1_2_301 1_2 1_0_0 4
        """
        expect = "0,10,12301,12,100,4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 34))
    
    def test_35(self):
        """test literal"""
        input = """
            0 10 1_2_301 1_2 1_0_0 4 5
        """
        expect = "0,10,12301,12,100,4,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 35))

    def test_36(self):
        """test literal"""
        input = """
            0 10 1_2_301 1_2 1_0_0 4 9
        """
        expect = "0,10,12301,12,100,4,9,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 36))

    def test_37(self):
        """test literal"""
        input = """
            1___
        """
        expect = "1,___,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 37))

    def test_38(self):
        """test literal"""
        input = """
            1__2
        """
        expect = "1,__2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 38))
    
    def test_39(self):
        """test literal"""
        input = """
            1__
        """
        expect = "1,__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 39))
    
    def test_40(self):
        """test literal"""
        input = """
            1_00_
        """
        expect = "100,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 40))
    
    def test_41(self):
        """test literal"""
        input = """
            0.01e+0 0.01e-000 1_0.e-0 1_0.10e+1 1_0.e-1 1_2e-10
        """
        expect = "0.01e+0,0.01e-000,10.e-0,10.10e+1,10.e-1,12e-10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 41))

    def test_42(self):
        """test literal"""
        input = """
            1_0e+10 1_0.
        """
        expect = "10e+10,10.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 42))
    
    def test_43(self):
        """test literal"""
        input = """
            1_0e+10 1_0. 1e
        """
        expect = "10e+10,10.,1,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 43))
    
    def test_44(self):
        """test literal"""
        input = """
            1_0e+10 1_0. 1e+
        """
        expect = "10e+10,10.,1,e,+,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 44))
    
    def test_45(self):
        """test literal"""
        input = """
            1_0e+10 1_0. e-1
        """
        expect = "10e+10,10.,e,-,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 45))
    
    def test_46(self):
        """test literal"""
        input = """
            1_0e+10 1_0. e0
        """
        expect = "10e+10,10.,e0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 46))
    
    def test_47(self):
        """test literal"""
        input = """
            1_0e+10 1_0. e+1
        """
        expect = "10e+10,10.,e,+,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 47))
    
    def test_48(self):
        """test literal"""
        input = """
            1_0e+10 1_0. .01
        """
        expect = "10e+10,10.,.,0,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 48))

    def test_49(self):
        """test literal"""
        input = """
            1_0e+10 1_0. .
        """
        expect = "10e+10,10.,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 49))
    
    def test_50(self):
        """test literal"""
        input = """
            1_0.1_2
        """
        expect = "10.1,_2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 50))

    def test_51(self):
        """test literal"""
        input = """
            1_0.1_2 .e5
        """
        expect = "10.1,_2,.e5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 51))
    
    def test_52(self):
        """test literal"""
        input = """
            1_0.1_2_1
        """
        expect = "10.1,_2_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 52))

    def test_53(self):
        """test literal"""
        input = """
            1_0.e1_5
        """
        expect = "10.e1,_5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 53))
    
    def test_54(self):
        """test literal"""
        input = """
            1_0.e1_1 2
        """
        expect = "10.e1,_1,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 54))
    
    def test_55(self):
        """test literal"""
        input = """
            1_0.e1_1 7
        """
        expect = "10.e1,_1,7,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 55))
    
    def test_56(self):
        """test literal"""
        input = """
            1_0.e1_1 5_
        """
        expect = "10.e1,_1,5,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 56))
    
    def test_57(self):
        """test literal"""
        input = """
            1_0.e1_1 _1_2
        """
        expect = "10.e1,_1,_1_2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 57))
    
    def test_58(self):
        """test literal"""
        input = """
            " abc \n"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, 58))
    
    def test_59(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\'"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\',<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 59))
    
    def test_60(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\' %^"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\' %^,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 60))
    
    def test_61(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\' \\" &"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\' \\\" &,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 61))

    def test_62(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\' \\" #"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\' \\\" #,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 62))
    
    def test_63(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\' \\" $"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\' \\\" $,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 63))

    def test_64(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\' \\" *"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\' \\\" *,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 64))
    
    def test_65(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\' \\" &{~!@~"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\' \\\" &{~!@~,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 65))
    
    def test_66(self):
        """test literal"""
        input = """
            " abc \n xyz \n \n"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, 66))
    
    def test_67(self):
        """test literal"""
        input = """
            " abc 
            123 "
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, 67))
    
    def test_68(self):
        """test literal"""
        input = """
            " ert \n \r"
        """
        expect = "Unclosed String:  ert "
        self.assertTrue(TestLexer.test(input, expect, 68))
    
    def test_69(self):
        """test literal"""
        input = """" xyz """
        expect = "Unclosed String:  xyz "
        self.assertTrue(TestLexer.test(input, expect, 69))
    
    def test_70(self):
        """test literal"""
        input = """
            " xyz \\1"
        """
        expect = "Illegal Escape In String:  xyz \\1"
        self.assertTrue(TestLexer.test(input, expect, 70))
    
    def test_71(self):
        """test literal"""
        input = """
            " xyz \\ "
        """
        expect = "Illegal Escape In String:  xyz \\ "
        self.assertTrue(TestLexer.test(input, expect, 71))
    
    def test_72(self):
        """test literal"""
        input = """\"eee\\\""""
        expect = "Unclosed String: eee\\\""
        self.assertTrue(TestLexer.test(input, expect, 72))
    
    def test_73(self):
        """test literal"""
        input = """
            "' '""
        """
        expect = "' ',Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 73))
    
    def test_74(self):
        """test error"""
        input = """
            @
        """
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 74))
    
    def test_75(self):
        """test error"""
        input = """
            @
        """
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 75))
    
    def test_76(self):
        """test error"""
        input = """
            #
        """
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 76))
    
    def test_77(self):
        """test error"""
        input = """
            ~a
        """
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 77))
    
    def test_78(self):
        """test error"""
        input = """
            &asaaa
        """
        expect = "Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 78))
    
    def test_79(self):
        """test error"""
        input = """
            >ssssss
        """
        expect = ">,ssssss,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 79))
    
    def test_80(self):
        """test error"""
        input = """
            ~~ssssss
        """
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 80))
    
    def test_81(self):
        """test error"""
        input = """
            / /
        """
        expect = "/,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 81))
    
    def test_82(self):
        """test error"""
        input = """
            / / >
        """
        expect = "/,/,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 82))

    def test_83(self):
        """test literal"""
        input = """
            15.
        """
        expect = "15.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 83))
    
    def test_84(self):
        """test literal"""
        input = """
            15e
        """
        expect = "15,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 84))
    
    def test_85(self):
        """test literal"""
        input = """
            15.1
        """
        expect = "15.1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 85))
    
    def test_86(self):
        """test literal"""
        input = """
            15.123_1
        """
        expect = "15.123,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 86))
    
    def test_87(self):
        """test literal"""
        input = """
            15.957___3
        """
        expect = "15.957,___3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 87))
    
    def test_88(self):
        """test literal"""
        input = """
            15.8 12
        """
        expect = "15.8,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 88))
    
    def test_89(self):
        """test literal"""
        input = """
            15. 1_ 11
        """
        expect = "15.,1,_,11,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 89))
    
    def test_90(self):
        """test literal"""
        input = """
            15. __ 1
        """
        expect = "15.,__,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 90))
    
    def test_91(self):
        """test literal"""
        input = """
            15. __ 1 22 _1
        """
        expect = "15.,__,1,22,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 91))
    
    def test_92(self):
        """test literal"""
        input = """
            15. __ 1 1e+10
        """
        expect = "15.,__,1,1e+10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 92))
    
    def test_93(self):
        """test literal"""
        input = """
            15. __ 1 .e10
        """
        expect = "15.,__,1,.e10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 93))
    
    def test_94(self):
        """test literal"""
        input = """
            15. __ 1 e
        """
        expect = "15.,__,1,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 94))
    
    def test_95(self):
        """test literal"""
        input = """
            15. __ 1 _4
        """
        expect = "15.,__,1,_4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 95))

    def test_96(self):
        """test literal"""
        input = """
            15. __ 1 _4_3
        """
        expect = "15.,__,1,_4_3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 96))
    
    def test_97(self):
        """test literal"""
        input = """
            15. __ 1 4__
        """
        expect = "15.,__,1,4,__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 97))
    
    def test_98(self):
        """test literal"""
        input = """
            15. __ 1__
        """
        expect = "15.,__,1,__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 98))
    
    def test_99(self):
        """test literal"""
        input = """
            15._ __ 1
        """
        expect = "15.,_,__,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 99))
    
    def test_100(self):
        """test literal"""
        input = """
            15. __ 1 .e12
        """
        expect = "15.,__,1,.e12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 100))

    
    

    
    

    
    
    
    
    

    
    
    
    
    
    
    

    