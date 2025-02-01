import unittest
import inspect
from TestUtils import TestChecker
from AST import *

#* python3 run.py test CheckerSuite
#* python3 run.py test CheckerSuite name_test
class CheckerSuite(unittest.TestCase):

    def test_001(self):
        input = """
            a : integer;
            b : float;
            a : string;

            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_002(self):
        input = """
            a, b, a : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
    
    def test_003(self):
        input = """
            a : function void () {}
            a : function void () {}
            main : function void(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_004(self):
        input = """
            a : function void () {}
            a : function void (a : string) {}
            main : function void(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_005(self):
        input = """
            readInteger : function integer (e : integer){ 
                return 1;
            }
            main : function void(){}
        """
        expect = "Redeclared Function: readInteger"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_006(self):
        input = """
            readInteger : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_007(self):
        input = """
            a : integer;
            a : function void (){}
            main : function void(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_008(self):
        input = """
            a : function void (){}
            a : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_009(self):
        input = """
            a : function void (a : integer) inherit b{preventDefault();}
            main : function void(){}
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_010(self):
        input = """
            a : function void (a : integer) inherit c{preventDefault();}
            b : function void (b : integer){}
            c : function void () inherit b{}
            d : function void () inherit e{}
            main : function void(){}
        """
        expect = "Undeclared Function: e"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_011(self):
        input = """
            var_a : integer;
            a : function void (a : integer) inherit printInteger{preventDefault();}
            b : function void (b : integer){}
            c : function void () inherit main{}
            d : function void () inherit var_a{}
            main : function void(){}
        """
        expect = "Undeclared Function: var_a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_012(self):
        input = """
            a : function void(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_013(self):
        input = """
            main : function string(){
                return "votien";
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_014(self):
        input = """
            main : function void(a : auto){
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_015(self):
        input = """
            foo_a: function void(){}
            main : function auto() inherit foo_a{}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_016(self):
        input = """
            main : integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_017(self):
        input = """
/*
printListFunctionMT22 :[
	FuncMT22(#0, readInteger, IntegerType(), [])
	FuncMT22(#1, readFloat, FloatType(), [])
	FuncMT22(#2, readBoolean, BooleanType(), [])
	FuncMT22(#3, readString, StringType(), [])
	FuncMT22(#5, printInteger, VoidType(), [ParamMT22(#4, printInteger, IntegerType(), False, inherit=False)])
	FuncMT22(#7, printFloat, VoidType(), [ParamMT22(#6, printFloat, FloatType(), False, inherit=False)])
	FuncMT22(#9, printBoolean, VoidType(), [ParamMT22(#8, printBoolean, BooleanType(), False, inherit=False)])
	FuncMT22(#11, printString, VoidType(), [ParamMT22(#10, printString, StringType(), False, inherit=False)])
	FuncMT22(#12, foo_a, AutoType(), [], inherit=#13)
	FuncMT22(#13, foo_b, VoidType(), [])
	FuncMT22(#14, foo_c, VoidType(), [], inherit=#13)
	FuncMT22(#15, foo_d, VoidType(), [], inherit=#14)
	FuncMT22(#16, main, VoidType(), [])
]
*/
        // readInteger, readFloat, readBoolean, readString, printInteger, printFloat, printBoolean, printString
            var_a : integer;
        // readInteger, readFloat, readBoolean, readString, printInteger, printFloat, printBoolean, printString, var_a
            foo_a : function auto() inherit foo_b{}
        // readInteger, readFloat, readBoolean, readString, printInteger, printFloat, printBoolean, printString, var_a, foo_a
            var_b : string;
        // readInteger, readFloat, readBoolean, readString, printInteger, printFloat, printBoolean, printString, var_a, foo_a, var_b
            foo_b : function void(){}
        // readInteger, readFloat, readBoolean, readString, printInteger, printFloat, printBoolean, printString, var_a, foo_a, var_b, foo_b
            foo_c : function void() inherit foo_b{}
        // readInteger, readFloat, readBoolean, readString, printInteger, printFloat, printBoolean, printString, var_a, foo_a, var_b, foo_b, foo_c
            foo_d : function void() inherit foo_c{}
        // readInteger, readFloat, readBoolean, readString, printInteger, printFloat, printBoolean, printString, var_a, foo_a, var_b, foo_b, foo_c, foo_d
            main : function void(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_018(self):
        input = """
            a : integer;
            foo_c : function void(a : integer) inherit foo_b{preventDefault();}
            foo_b : function void (a : integer, foo_b : string) {}
            foo_a : function void (a : integer, a : string) {}
            main : function void(){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_019(self):
        input = """
            a : integer;
            foo_a : function void (c : integer, b : string) {
                {
                    a : integer;
                }
                a : integer;
                {
                    b, a, b : integer;
                }
            }

            main : function void(){}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_020(self):
        input = """
            a : auto;
            main : function void(){}
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_021(self):
        input = """
            main : function void(){
                b : auto;
            }
        """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_022(self):
        input = """
            a : auto = 1;
            main : function void(){
                b : string = 1;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_023(self):
        input = """
            a : integer = 1;
            b : string = true;
            main : function void(){}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_024(self):
        input = """
        /*
            Access Access(
            typeLeft = AutoType()
            symbol = [
                [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()) ]
            ])
        */
            a, b : integer;

        /*
            Access Access(
            typeLeft = AutoType()
            symbol = [
                [ ParamMT22(#12, a, IntegerType(), False, inherit=False), ParamMT22(#13, c, StringType(), False, inherit=False) ]
                [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()) ]
            ])
        */
        foo_a : function void(a : integer, c : string){
            /*
                Access Access(
                typeLeft = AutoType()
                symbol = [
                    [ VarMT22(#18, a, BooleanType()), VarMT22(#19, d, BooleanType()) ]
                    [ ParamMT22(#12, a, IntegerType(), False, inherit=False), ParamMT22(#13, c, StringType(), False, inherit=False) ]
                    [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()) ]
                ])
            */
            e, d : boolean;

            {
                /*
                    Access Access(
                    typeLeft = AutoType()
                    symbol = [
                        [ VarMT22(#20, a, BooleanType()), VarMT22(#21, e, BooleanType()) ]
                        [ VarMT22(#18, e, BooleanType()), VarMT22(#19, d, BooleanType()) ]
                        [ ParamMT22(#12, a, IntegerType(), False, inherit=False), ParamMT22(#13, c, StringType(), False, inherit=False) ]
                        [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()) ]
                    ])
                */
                a, e : boolean;
            }

            /*
                Access Access(
                typeLeft = AutoType()
                symbol = [
                    [ VarMT22(#18, a, BooleanType()), VarMT22(#19, d, BooleanType()), VarMT22(#22, k, BooleanType()) ]
                    [ ParamMT22(#12, a, IntegerType(), False, inherit=False), ParamMT22(#13, c, StringType(), False, inherit=False) ]
                    [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()) ]
                ])
            */            
            k : auto = true;
        }            



        /*
            Access Access(
            typeLeft = AutoType()
            symbol = [
                [ ]
                [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()) ]
            ])
        */                
        main : function void(){
            /*
                Access Access(
                typeLeft = AutoType()
                symbol = [
                    [ VarMT22(#23, j, AutoType()) ]
                    [  ]
                    [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()) ]
                ])
            */    
            j : auto = true;
        }

        /*
            Access Access(
            typeLeft = AutoType()
            symbol = [
                [ VarMT22(#16, a, IntegerType()), VarMT22(#17, b, IntegerType()), VarMT22(#24, c, BooleanType()) ]
            ])
        */ 
            c : auto = true;
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_025(self):
        input = """
            foo_a: function void(inherit b : auto){}
            foo_b: function void(b : auto) inherit foo_a{preventDefault();}

            main : function auto() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_026(self):
        input = """
            foo_a: function void() inherit foo_b{preventDefault();}
            foo_b: function void(inherit b : auto){}
            foo_c: function void(inherit b : auto) inherit foo_a{preventDefault();}            

            main : function void() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_027(self):
        input = """
            foo_a: function void(inherit b : integer) inherit foo_b{preventDefault();}
            foo_b: function void(b : integer){}
            foo_c: function void(b : integer) inherit foo_a{preventDefault();}            

            main : function void() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_028(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : auto)  inherit foo_a{}
            foo_c: function void() inherit foo_b{}            

            main : function void() {}
        """
        expect = "Invalid statement in function: foo_c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_029(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : auto)  inherit foo_a{}
            foo_c: function void() inherit foo_b{ super(1); }
            foo_d: function void()  inherit foo_a{preventDefault();}              
            foo_e: function void(a : auto)  inherit foo_d{super();} 
            main : function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
    
    def test_030(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : auto)  inherit foo_a{}
            foo_c: function void() inherit foo_b{ a, b : string; }            

            main : function void() {}
        """
        expect = "Invalid statement in function: foo_c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_031(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : auto)  inherit foo_a{}
            foo_c: function void() inherit foo_b{}            

            main : function void() {}
        """
        expect = "Invalid statement in function: foo_c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_032(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : integer)  inherit foo_a{
                preventDefault(1, 2);
            }          

            main : function void() {}
        """
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_033(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : integer)  inherit foo_a{
                super("A");
            }          

            main : function void() {}
        """
        expect = """Type mismatch in expression: StringLit("A")"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_034(self):
        input = """
            foo_a: function void(a : integer){}
            foo_b: function void()  inherit foo_a{
                super();
            }          

            main : function void() {}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_035(self):
        input = """
            foo_a: function void(b : float, a : float){}
            foo_b: function void()  inherit foo_a{
                super(1, 2.0);
            }          
            foo_c: function void()  inherit foo_a{
                super(1,true);
            }       
            main : function void() {}
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_036(self):
        input = """
            a : integer = 1;
            b : integer = c;
            main : function void(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_037(self):
        input = """
            a : integer = 1;
            foo_a : function void (e : integer){
                b : integer = a;
                {
                    c : integer = b;
                    b : integer = a;
                    e : integer = e;
                }
                d : integer = c;
            }

            main : function void(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_038(self):
        input = """
            a : integer = 1;
            foo_a : function void (e : integer){
                {
                    b : integer = d;
                }
                d : integer = c;
            }
            d : integer = a;
            main : function void(){}
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_039(self):
        input = """
            foo_a: function void(inherit c : integer) inherit foo_b{preventDefault();}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer() inherit foo_a{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_040(self):
        input = """
            foo_a: function void(inherit c : integer) inherit foo_b{preventDefault();}
            foo_b: function void( b : integer){}
            foo_c: function integer() inherit foo_a{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_041(self):
        input = """
            foo_a: function void(inherit c : integer, inherit b : integer) inherit foo_b{preventDefault();}
            foo_b: function void( b : integer){}
            foo_c: function integer() inherit foo_a{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_042(self):
        input = """
            foo_a: function void(inherit c : integer, inherit b : integer) inherit foo_b{preventDefault();}
            foo_b: function void( b : integer){
                a, d : integer = b, c;
            }
            foo_c: function integer() inherit foo_a{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_043(self):
        input = """
            foo_a: function void(b : auto) {
                a : integer = b;
                d : integer = b;
                c : string = b;
            }
                   
            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", StringType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_044(self):
        input = """
            foo_a: function void(inherit c : auto) inherit foo_b{preventDefault();}
            foo_b: function void(inherit b : auto){}
            foo_c: function integer() inherit foo_a{
                preventDefault();
                a, d : integer = b, c;
                e : boolean = b;
            }            

            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("e", BooleanType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_045(self):
        input = """
            foo_a: function void(inherit c : auto) inherit foo_b{preventDefault();}
            foo_b: function void(inherit b : auto){}
            foo_c: function integer() inherit foo_a{
                preventDefault();
                a : float = b;
                d : integer = d;
                e : float = d;
                k : string = d;
            }            

            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("k", StringType(), Id("d"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_046(self):
        input = """
            foo_a: function void(inherit c : integer) {}
            foo_b: function integer(inherit b : float){return 1;}
            foo_c: function integer(){return 1;}            

            main : function auto() {
                a : integer = foo_c();
                b : integer = foo_b(1.0);
                d : integer = foo_d();
            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_047(self):
        input = """
            a : integer = foo_c();
            b : integer = foo_b(1.0);
            foo_a: function void(inherit c : integer) {}
            foo_b: function integer(inherit b : float){return 1;}
            foo_c: function integer(){return 1;}  
            d : integer = foo_d();   

            main : function auto() {

            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_048(self):
        input = """
            foo_a: function integer(inherit c : integer) {return 1;}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer(){return 1;}  

            main : function auto() {
                a : integer = foo_c(1);
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_c", [IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_049(self):
        input = """
            foo_a: function integer(inherit c : integer) {return 1;}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer(){return 1;}  

            main : function auto() {
                a : integer = foo_a();
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_a", [])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_050(self):
        input = """
            foo_a: function integer(inherit c : integer) {return 1;}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer(){return 1;}  

            main : function auto() {
                a : integer = foo_c("a");
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_c", [StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_051(self):
        input = """
            foo_a: function integer(inherit c : integer) {return 1;}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer(){return 1;}  

            main : function auto() {
                a : integer = foo_b(1);
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_b", [IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_052(self):
        input = """
            foo_a: function integer(c : auto) {
                b : string = c;
            }

            main : function auto() {
                a : integer = foo_a(2);
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_a", [IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_053(self):
        input = """
            main : function auto() {
                a : integer = foo_a(2);
            }

            foo_a: function integer(c : auto) {
                b : string = c;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), Id("c"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_054(self):
        input = """
            main : function auto() {
                a : integer = foo_a(2);
            }

            foo_a: function auto(c : auto) {
                a : string = foo_a(2);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("a", StringType(), FuncCall("foo_a", [IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_055(self):
        input = """
            foo_a: function integer(inherit c : float) {return 1;}
            foo_b: function void(inherit b : float){}
            foo_c: function void(){}            

            main : function auto() {
                foo_a(1.0);
                foo_b(1.0);
                foo_c();
                foo_d();
            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_056(self):
        input = """
            foo_a: function void(inherit c : integer) {
                foo_c();
                foo_d();
            }
            foo_b: function integer(inherit b : integer){return 1;}
            foo_c: function integer(){return 1;}   

            main : function auto() {

            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_057(self):
        input = """
            foo_a: function void(){preventDefault();}      

            main : function void() {}
        """
        expect = "Undeclared Function: preventDefault"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_058(self):
        input = """
            foo_a: function void(){}

            foo_b: function void(a : auto)  inherit foo_a{}

            foo_c: function void() inherit foo_b{
                preventDefault();
                super(1);
            }            

            main : function void() {}
        """
        expect = "Undeclared Function: super"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
   
    def test_059(self):
        input = """
            foo_a: function integer(inherit c : integer) {return 1;}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer(){return 1;}  

            main : function auto() {
                foo_c(1);
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_c",[IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_060(self):
        input = """
            foo_a: function integer(inherit c : integer) {return 1;}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer(){return 1;}  

            main : function auto() {
                foo_a();
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_a",[])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_061(self):
        input = """
            foo_a: function integer(inherit c : integer) {return 1;}
            foo_b: function void(inherit b : integer){}
            foo_c: function integer(){return 1;}  

            main : function auto() {
                foo_c("a");
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_c",[StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_062(self):
        input = """
            foo_a: function integer(c : auto) {
                b : string = c;
            }

            main : function auto() {
                foo_a(2);
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_a",[IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_063(self):
        input = """
            main : function auto() {
                a : integer = foo_a(2);
            }
            foo_a: function integer(c : auto) {
                b : string = c;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), Id("c"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_064(self):
        input = """
            main : function auto() {
                foo_a(2);
            }

            foo_a: function auto(c : auto) {
                foo_a(2);
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_065(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                b = a;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_066(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                a = c;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("a"), Id("c"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_067(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                b = d;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("b"), Id("d"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_068(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                a = e;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("a"), Id("e"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_069(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                e = j;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("e"), Id("j"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_070(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                e = k;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("e"), Id("k"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_071(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                k = h;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("k"), Id("h"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_072(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                a = a;
                b = b;
                c = c;
                d = d;
                e = e;
                f = f;
                j = j;
                k = k;
                h = h;
                e = f;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("e"), Id("f"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_073(self):
        input = """
            foo_a : function integer (e : auto){
                e = 2.0;
                e = 2;
                e = "@";
            }

            main : function void() {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id("e"), StringLit("@"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_074(self):
        input = """
            main : function void() {
                if(true){
                    a : auto = 1;
                } 
                else {
                    a : auto = 1;
                }
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_075(self):
        input = """
            main : function void() {
                if(1){
                    a : auto = 1;
                } 
                else {
                    a : auto = 1;
                }
            }
        """
        expect = """Type mismatch in statement: IfStmt(IntegerLit(1), BlockStmt([VarDecl("a", AutoType(), IntegerLit(1))]), BlockStmt([VarDecl("a", AutoType(), IntegerLit(1))]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_076(self):
        input = """
            main : function void() {
                if(foo_a()){
                    a : auto = 1;
                } 
                else {
                    a : auto = 1;
                }
            }

            foo_a : function void(){
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_a", [])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_077(self):
        input = """
            main : function void() {
                if(foo_a()){
                    a : auto = 1;
                } 
                else {
                    a : auto = 1;
                }
            }

            foo_a : function auto(){
                return;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_078(self):
        input = """
            main : function void() {
                if(foo_a()){
                    a : auto = 1;
                } 
            }

            foo_a : function auto(){
                return true;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_079(self):
        input = """
            main : function void() {}

            foo_a : function auto(a : auto){
                if(foo_a(1)){
                    
                }
                c : boolean = foo_a(1);
                b : string = foo_a(1);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), FuncCall("foo_a", [IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_080(self):
        input = """
            main : function void() {
                id : auto = 0;
                for(id = 1, true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_081(self):
        input = """
            main : function void() {
                id : auto = "0";
                for(id = 1, true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_082(self):
        input = """
            main : function void() {
                id : auto = 1.0;
                for(id = 1, true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_083(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = "1", true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), StringLit("1")), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_084(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 2, foo_a(), id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_085(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 1, foo_a(), id)
                {
                    return;
                }
            }

            foo_a : function integer(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), FuncCall("foo_a", []), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_086(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 1, true, true)
                {
                    return;
                }
            }

            foo_a : function integer(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), BooleanLit(True), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_087(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = foo_a(), true, 1)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return true;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_088(self):
        input = """
            main : function void() {

            }

            foo_a : function auto(id : auto){
                for(id = 1, true, 1)
                {
                    return;
                }
                foo_a("a");
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_a",[StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_089(self):
        input = """
            main : function void() {
                a : auto = 1;
                while(true){
                    a : auto = 1;
                    return;
                }
                while(true) return;
                while(1) return;
            }

            foo_a : function auto(){
                return true;
            }
        """
        expect = """Type mismatch in statement: WhileStmt(IntegerLit(1), ReturnStmt())"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_090(self):
        input = """
            main : function void() {
                while(foo_a()) return;
            }

            foo_a : function auto(){
                return true;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_091(self):
        input = """
            main : function void() {
                while(foo_a()) return;
            }

            foo_a : function string(){
                return "2";
            }
        """
        expect = """Type mismatch in statement: WhileStmt(FuncCall("foo_a", []), ReturnStmt())"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_092(self):
        input = """
            main : function void() {
                while(foo_a()) return;
            }

            foo_a : function auto(){
                return true;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_093(self):
        input = """
            main : function void() {
                break;
            }
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_094(self):
        input = """
            main : function void() {
                continue;
            }
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_095(self):
        input = """
            main : function void() {
                while(true)
                {
                    a : auto = 1;
                    for (a=1,true,1) break;
                    break;
                    continue;
                    do{
                        {
                            break;
                            continue;
                        }
                    }while(true);
                    break;
                    continue;
                    for (a=1,true,1) continue;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

        
    def test_096(self):
        input = """
            main : function void() {
                while(true)
                {
                    a : auto = 1;
                    for (a=1,true,1) break;
                    break;
                    continue;
                    do{
                        {
                            break;
                            continue;
                        }
                    }while(true);
                    break;
                    continue;
                    for (a=1,true,1) continue;
                }
                break;
            }
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_097(self):
        input = """
            main : function void() {
                while(true)
                {
                    a : auto = 1;
                    for (a=1,true,1) break;
                    break;
                    continue;
                    do{
                        {
                            break;
                            continue;
                        }
                    }while(true);
                    break;
                    continue;
                    for (a=1,true,1) continue;
                }
                continue;
            }
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_098(self):
        input = """
            foo : function float() {
                return 1;
                return "a";
            }
            main : function auto() {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_099(self):
        input = """
            foo : function float() {
                return 1.1;
                return "a";
                {
                    return "a";
                }
            }
            main : function void() {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_100(self):
        input = """
            foo : function integer() {
                return foo_a();
            }
            foo_a : function auto() {
                return "string";
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("string"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_101(self):
        input = """
            foo : function auto() {
                return 1;
            }
            foo_a : function string() {
                return foo();
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: ReturnStmt(FuncCall("foo", []))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_102(self):
        input = """
            foo : function auto() {

            }
            foo_a : function string() {
                return foo();
            }
            main : function void() {}
        """
        expect = """Type mismatch in expression: FuncCall("foo", [])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_103(self):
        input = """
            foo : function void() {
                return 1;
            }
            foo_a : function auto() {
                // return foo();
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_104(self):
        input = """
            foo : function string() {
                return 1;
            }
            foo_a : function auto() {
                // return foo();
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_105(self):
        input = """
            foo : function string(a : auto) {
                a = foo("a");
                return a;
                a = 1;
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id("a"), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_106(self):
        input = """
            a : integer = 1 + 2.3 * 3 / 4.0;
            b : float = 1.0 + a;
            
            main : function void() {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_107(self):
        input = """
            a : integer = 1 + "a";
            
            main : function void() {}
        """
        expect = """Type mismatch in expression: BinExpr("+", IntegerLit(1), StringLit("a"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_108(self):
        input = """
            a : integer = main() + 1;
            
            main : function void() {}
        """
        expect = """Type mismatch in expression: FuncCall("main", [])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_109(self):
        input = """
            foo_a : function integer (a : auto) {
                b : integer = a;
                return a;
                c : string = a + 1.0;
            }
            
            main : function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", StringType(), BinExpr("+", Id("a"), FloatLit(1.0)))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_110(self):
        input = """
            foo_a : function integer (a : auto) {
                b : integer = a + foo_b();
                return a;
            }
            
            main : function void() {}
            foo_b : function auto (){return "String";}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("String"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_111(self):
        input = """
            foo_a : function float (a : auto) {
                b : auto = foo_a(1.0) + foo_b();
                return a;
            }
            
            main : function void() {}
            foo_b : function auto (){return "String";}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("String"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_112(self):
        input = """
            foo_a : function integer (a : auto) {
                b : float = a % foo_b();
                c : float = 1.0 % 2;
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return 1;}
        """
        expect = """Type mismatch in expression: BinExpr("%", FloatLit(1.0), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_113(self):
        input = """
            foo_a : function integer (a : auto) {
                b : boolean = a && true || foo_b();
                c : boolean = 1.0 && true;
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return true;}
        """
        expect = """Type mismatch in expression: BinExpr("&&", FloatLit(1.0), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_114(self):
        input = """
            foo_a : function integer (a : auto) {
                b : boolean = a == foo_b();
                c : boolean = 1 != true;
                d : boolean = 1.0 == true;
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return true;}
        """
        expect = """Type mismatch in expression: BinExpr("==", FloatLit(1.0), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_115(self):
        input = """
            foo_a : function integer (a : auto) {
                b : boolean = a > foo_b();
                c : boolean = 1 < 1.2;
                d : boolean = 1.0 >= a;
                e : boolean = 1 <= 2.3*a;
                f : boolean = true >= "string";
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return 1;}
        """
        expect = """Type mismatch in expression: BinExpr(">=", BooleanLit(True), StringLit("string"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_116(self):
        input = """
            foo_a : function integer (a : auto) {
                b : string = a :: foo_b();
                c : string = a :: 1;
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return "string";}
        """
        expect = """Type mismatch in expression: BinExpr("::", Id("a"), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_117(self):
        input = """
            foo_a : function integer (a : auto) {
                b : string = a :: foo_b();
                c : string = a :: 1;
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return "string";}
        """
        expect = """Type mismatch in expression: BinExpr("::", Id("a"), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_118(self):
        input = """
            foo_a : function integer (a : auto) {
                b : boolean = ! foo_b() && ! a;
                c : boolean = ! true && !1;
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return true;}
        """
        expect = """Type mismatch in expression: UnExpr("!", IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_119(self):
        input = """
            foo_a : function integer (a : auto) {
                b : boolean = - foo_b() > - a;
                c : boolean = - 1.0 < - "a";
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return true;}
        """
        expect = """Type mismatch in expression: UnExpr("-", StringLit("a"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_119(self):
        input = """
            foo_a : function integer (a : auto) {
                b : boolean = - foo_b() > - a;
                c : boolean = - 1.0 < - "a";
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return true;}
        """
        expect = """Type mismatch in expression: UnExpr("-", StringLit("a"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_120(self):
        input = """  
            main : function void(){
                a : array [1] of float;
                b : array [2,2] of float;
                c : float = a[0] + b[0,0];
                d : array [2] of float = b[foo_a()];
            }

            foo_a : function auto(){return "string";}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("string"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_121(self):
        input = """  
            main : function void() {
                a : array [1] of string;
                b : array [2,2] of integer;
                c : float = a[0];
            }
            
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", FloatType(), ArrayCell("a", [IntegerLit(0)]))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
    
    def test_122(self):
        input = """  
            main : function void() {
                a : array [1] of string;
                b : array [2,2] of integer;
                c : float = b[1, "string"];
            }
            
        """
        expect = """Type mismatch in expression: ArrayCell("b", [IntegerLit(1), StringLit("string")])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_123(self):
        input = """  
            main : function void() {
                a : auto = {{1,1},{2,3}};
                a[0,0] = 1;
                a[0] = {2, 3};
                b : array [3,2,2] of integer = {{{1,1},{2,3}}, a, a};
                b[0,0] = {1,2};
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_124(self):
        input = """  
            main : function void() {
                a : auto = {{1,1},{"2",3}};
            }
        """
        expect = """Illegal array literal: ArrayLit([StringLit("2"), IntegerLit(3)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_125(self):
        input = """  
            main : function void() {
                a : auto = {{1,1},{2 + 2,3}, {"1"}};
            }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([BinExpr("+", IntegerLit(2), IntegerLit(2)), IntegerLit(3)]), ArrayLit([StringLit("1")])])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_126(self):
        input = """  
            main : function void() {
                a : auto = {{1,1},{2 + 2,3.0}};
            }
        """
        expect = """Illegal array literal: ArrayLit([BinExpr("+", IntegerLit(2), IntegerLit(2)), FloatLit(3.0)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_127(self):
        input = """  
            main : function void() {
                a : integer = 1.0;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("a", IntegerType(), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_128(self):
        input = """  
            foo : function float (a : integer) {return 1;}
            main : function void() {
                foo(1.0);
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo",[FloatLit(1.0)])"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_129(self):
        input = """  
            foo : function float (a : integer) {
                {  
                    return 2;
                    return "B";
                }
                return "A";
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("A"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_130(self):
        input = """  
            foo : function auto (a : integer) {
                {  
                    return 1;
                    {
                        return "B";
                    }
                    return "B";
                }
                return "A";
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("A"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_131(self):
        input = """  
            foo : function auto (a : integer) {
                a : string;
            }
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_132(self):
        input = """
            a : string; 
            b : string = a; 
            foo_b: function void(inherit b : integer){}
            foo_c: function void() inherit foo_b{
                preventDefault();
                c : string = b; // inherit b : integer
            }            

            main : function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", StringType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
