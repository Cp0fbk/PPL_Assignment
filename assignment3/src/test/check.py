#2212631

import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_001(self):
        input = """  
            main : function void() {
                a : array [1] of string;
                b : array [2,2] of integer;
                c : float = a[0];
            }
            
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", FloatType(), ArrayCell("a", [IntegerLit(0)]))"""
        self.assertTrue(TestChecker.test(input, expect,1))

    def test_002(self):
        input = """
            a, b, a : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect,2))
    
    def test_003(self):
        input = """
            foo : function void() {
                return 1;
            }
            func1 : function auto() {
                // return foo();
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect,3))

    def test_004(self):
        input = """
            a : function void () {}
            a : function void (a : string) {}
            main : function void(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect,4))

    def test_005(self):
        input = """
            readInteger : function integer (e : integer){ 
                return 1;
            }
            main : function void(){}
        """
        expect = "Redeclared Function: readInteger"
        self.assertTrue(TestChecker.test(input, expect,5))

    def test_006(self):
        input = """
            readInteger : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input, expect,6))

    def test_007(self):
        input = """
            a : integer;
            a : function void (){}
            main : function void(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect,7))

    def test_008(self):
        input = """
            a : function void (){}
            a : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect,8))

    def test_009(self):
        input = """
            a : function void (a : integer) inherit b{preventDefault();}
            main : function void(){}
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect,9))

    def test_010(self):
        input = """
            a : function void (a : integer) inherit c{preventDefault();}
            b : function void (b : integer){}
            c : function void () inherit b{}
            d : function void () inherit e{}
            main : function void(){}
        """
        expect = "Undeclared Function: e"
        self.assertTrue(TestChecker.test(input, expect,10))

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
        self.assertTrue(TestChecker.test(input, expect,11))

    def test_012(self):
        input = """
            a : function void(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect,12))

    def test_013(self):
        input = """
            main : function string(){
                return "votien";
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect,13))

    def test_014(self):
        input = """
            main : function void(a : auto){
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect,14))

    def test_015(self):
        input = """
            func1: function void(){}
            main : function auto() inherit func1{}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect,15))

    def test_016(self):
        input = """
            main : integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect,16))

    def test_017(self):
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
        self.assertTrue(TestChecker.test(input, expect,17))

    def test_018(self):
        input = """
            a : integer;
            func1 : function void (a : integer, b : string) {
                a : integer;
                {
                    a : integer;
                }
                a : string;
            }

            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect,18))

    def test_019(self):
        input = """
            a : integer;
            func1 : function void (c : integer, b : string) {
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
        self.assertTrue(TestChecker.test(input, expect,19))

    def test_020(self):
        input = """
            a : auto;
            main : function void(){}
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect,20))

    def test_021(self):
        input = """
            main : function void(){
                b : auto;
            }
        """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect,21))

    def test_022(self):
        input = """  
            main : function void() {
                a : auto = {{1,1},{2 + 2,3}, {"1"}};
            }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([BinExpr("+", IntegerLit(2), IntegerLit(2)), IntegerLit(3)]), ArrayLit([StringLit("1")])])"""
        self.assertTrue(TestChecker.test(input, expect,22))

    def test_023(self):
        input = """
            a : integer = 1;
            b : string = true;
            main : function void(){}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect,23))

    def test_024(self):
        input = """
            a : string; 
            b : string = a; 
            func2: function void(inherit b : integer){}
            func3: function void() inherit func2{
                preventDefault();
                c : string = b; // inherit b : integer
            }            

            main : function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", StringType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect,24))

    def test_025(self):
        input = """
            func1: function void(inherit b : auto){}
            func2: function void(b : auto) inherit func1{preventDefault();}

            main : function auto() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect,25))

    def test_026(self):
        input = """
            func1: function void() inherit func2{preventDefault();}
            func2: function void(inherit b : auto){}
            func3: function void(inherit b : auto) inherit func1{preventDefault();}            

            main : function void() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect,26))

    def test_027(self):
        input = """
            func1: function void(inherit b : integer) inherit func2{preventDefault();}
            func2: function void(b : integer){}
            func3: function void(b : integer) inherit func1{preventDefault();}            

            main : function void() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect,27))

    def test_028(self):
        input = """
            func1: function void(){}
            func2: function void(a : auto)  inherit func1{}
            func3: function void() inherit func2{}            

            main : function void() {}
        """
        expect = "Invalid statement in function: func3"
        self.assertTrue(TestChecker.test(input, expect,28))

    def test_029(self):
        input = """
            func1: function void(){}
            func2: function void(a : auto)  inherit func1{}
            func3: function void() inherit func2{ super(1); }
            foo_d: function void()  inherit func1{preventDefault();}              
            foo_e: function void(a : auto)  inherit foo_d{super();} 
            main : function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect,29))
    
    def test_030(self):
        input = """
            func1: function void(){}
            func2: function void(a : auto)  inherit func1{}
            func3: function void() inherit func2{ a, b : string; }            

            main : function void() {}
        """
        expect = "Invalid statement in function: func3"
        self.assertTrue(TestChecker.test(input, expect,30))

    def test_031(self):
        input = """
            func1: function void(){}
            func2: function void(a : auto)  inherit func1{}
            func3: function void() inherit func2{}            

            main : function void() {}
        """
        expect = "Invalid statement in function: func3"
        self.assertTrue(TestChecker.test(input, expect,31))

    def test_032(self):
        input = """
            func1: function void(){}
            func2: function void(a : integer)  inherit func1{
                preventDefault(1, 2);
            }          

            main : function void() {}
        """
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect,32))

    def test_033(self):
        input = """  
            main : function void() {
                a : integer = 1.0;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("a", IntegerType(), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect,33))

    def test_034(self):
        input = """
            func1: function void(a : integer){}
            func2: function void()  inherit func1{
                super();
            }          

            main : function void() {}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect,34))

    def test_035(self):
        input = """
            func1: function void(b : float, a : float){}
            func2: function void()  inherit func1{
                super(1, 2.0);
            }          
            func3: function void()  inherit func1{
                super(1,true);
            }       
            main : function void() {}
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect,35))

    def test_036(self):
        input = """
            a : integer = 1;
            b : integer = c;
            main : function void(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect,36))

    def test_037(self):
        input = """
            a : integer = 1;
            func1 : function void (e : integer){
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
        self.assertTrue(TestChecker.test(input, expect,37))

    def test_038(self):
        input = """
            a : integer = 1;
            func1 : function void (e : integer){
                {
                    b : integer = d;
                }
                d : integer = c;
            }
            d : integer = a;
            main : function void(){}
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect,38))

    def test_039(self):
        input = """
            func1: function void(inherit c : integer) inherit func2{preventDefault();}
            func2: function void(inherit b : integer){}
            func3: function integer() inherit func1{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect,39))

    def test_040(self):
        input = """
            func1: function void(inherit c : integer) inherit func2{preventDefault();}
            func2: function void( b : integer){}
            func3: function integer() inherit func1{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect,40))


    def test_041(self):
        input = """
            func1: function void(inherit c : integer, inherit b : integer) inherit func2{preventDefault();}
            func2: function void( b : integer){}
            func3: function integer() inherit func1{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect,41))

    def test_042(self):
        input = """
            func1: function void(inherit c : integer, inherit b : integer) inherit func2{preventDefault();}
            func2: function void( b : integer){
                a, d : integer = b, c;
            }
            func3: function integer() inherit func1{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect,42))

    def test_043(self):
        input = """
            func1: function void(b : auto) {
                a : integer = b;
                d : integer = b;
                c : string = b;
            }
                   
            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", StringType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect,43))

    def test_044(self):
        input = """
            func1: function void(inherit c : auto) inherit func2{preventDefault();}
            func2: function void(inherit b : auto){}
            func3: function integer() inherit func1{
                preventDefault();
                a, d : integer = b, c;
                e : boolean = b;
            }            

            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("e", BooleanType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect,44))

    def test_045(self):
        input = """
            func1: function void(inherit c : auto) inherit func2{preventDefault();}
            func2: function void(inherit b : auto){}
            func3: function integer() inherit func1{
                preventDefault();
                a : float = b;
                d : integer = d;
                e : float = d;
                k : string = d;
            }            

            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("k", StringType(), Id("d"))"""
        self.assertTrue(TestChecker.test(input, expect,45))

    def test_046(self):
        input = """
            func1: function void(inherit c : integer) {}
            func2: function integer(inherit b : float){return 1;}
            func3: function integer(){return 1;}            

            main : function auto() {
                a : integer = func3();
                b : integer = func2(1.0);
                d : integer = foo_d();
            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect,46))


    def test_047(self):
        input = """
            a : integer = func3();
            b : integer = func2(1.0);
            func1: function void(inherit c : integer) {}
            func2: function integer(inherit b : float){return 1;}
            func3: function integer(){return 1;}  
            d : integer = foo_d();   

            main : function auto() {

            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect,47))


    def test_048(self):
        input = """
            func1: function integer(inherit c : integer) {return 1;}
            func2: function void(inherit b : integer){}
            func3: function integer(){return 1;}  

            main : function auto() {
                a : integer = func3(1);
            }
        """
        expect = """Type mismatch in expression: FuncCall("func3", [IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect,48))

    def test_049(self):
        input = """
            func1: function integer(inherit c : integer) {return 1;}
            func2: function void(inherit b : integer){}
            func3: function integer(){return 1;}  

            main : function auto() {
                a : integer = func1();
            }
        """
        expect = """Type mismatch in expression: FuncCall("func1", [])"""
        self.assertTrue(TestChecker.test(input, expect,49))

    def test_050(self):
        input = """
            func1: function integer(inherit c : integer) {return 1;}
            func2: function void(inherit b : integer){}
            func3: function integer(){return 1;}  

            main : function auto() {
                a : integer = func3("a");
            }
        """
        expect = """Type mismatch in expression: FuncCall("func3", [StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect,50))

    def test_051(self):
        input = """
            func1: function integer(inherit c : integer) {return 1;}
            func2: function void(inherit b : integer){}
            func3: function integer(){return 1;}  

            main : function auto() {
                a : integer = func2(1);
            }
        """
        expect = """Type mismatch in expression: FuncCall("func2", [IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect,51))

    def test_052(self):
        input = """
            func1: function integer(c : auto) {
                b : string = c;
            }

            main : function auto() {
                a : integer = func1(2);
            }
        """
        expect = """Type mismatch in expression: FuncCall("func1", [IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect,52))

    def test_053(self):
        input = """
            main : function auto() {
                a : integer = func1(2);
            }

            func1: function integer(c : auto) {
                b : string = c;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), Id("c"))"""
        self.assertTrue(TestChecker.test(input, expect,53))

    def test_054(self):
        input = """
            main : function auto() {
                a : integer = func1(2);
            }

            func1: function auto(c : auto) {
                a : string = func1(2);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("a", StringType(), FuncCall("func1", [IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect,54))

    def test_055(self):
        input = """
            func1: function integer(inherit c : float) {return 1;}
            func2: function void(inherit b : float){}
            func3: function void(){}            

            main : function auto() {
                func1(1.0);
                func2(1.0);
                func3();
                foo_d();
            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect,55))


    def test_056(self):
        input = """
            func1: function void(inherit c : integer) {
                func3();
                foo_d();
            }
            func2: function integer(inherit b : integer){return 1;}
            func3: function integer(){return 1;}   

            main : function auto() {

            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect,56))

    def test_057(self):
        input = """
            func1: function void(){preventDefault();}      

            main : function void() {}
        """
        expect = "Undeclared Function: preventDefault"
        self.assertTrue(TestChecker.test(input, expect,57))

    def test_058(self):
        input = """
            func1: function void(){}

            func2: function void(a : auto)  inherit func1{}

            func3: function void() inherit func2{
                preventDefault();
                super(1);
            }            

            main : function void() {}
        """
        expect = "Undeclared Function: super"
        self.assertTrue(TestChecker.test(input, expect,58))
   
    def test_059(self):
        input = """
            func1: function integer(inherit c : integer) {return 1;}
            func2: function void(inherit b : integer){}
            func3: function integer(){return 1;}  

            main : function auto() {
                func3(1);
            }
        """
        expect = """Type mismatch in statement: CallStmt("func3",[IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect,59))

    def test_060(self):
        input = """
            func1: function integer(inherit c : integer) {return 1;}
            func2: function void(inherit b : integer){}
            func3: function integer(){return 1;}  

            main : function auto() {
                func1();
            }
        """
        expect = """Type mismatch in statement: CallStmt("func1",[])"""
        self.assertTrue(TestChecker.test(input, expect,60))

    def test_061(self):
        input = """
            func1: function integer(inherit c : integer) {return 1;}
            func2: function void(inherit b : integer){}
            func3: function integer(){return 1;}  

            main : function auto() {
                func3("a");
            }
        """
        expect = """Type mismatch in statement: CallStmt("func3",[StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect,61))

    def test_062(self):
        input = """
            func1: function integer(c : auto) {
                b : string = c;
            }

            main : function auto() {
                func1(2);
            }
        """
        expect = """Type mismatch in statement: CallStmt("func1",[IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect,62))

    def test_063(self):
        input = """
            main : function auto() {
                a : integer = func1(2);
            }
            func1: function integer(c : auto) {
                b : string = c;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), Id("c"))"""
        self.assertTrue(TestChecker.test(input, expect,63))

    def test_064(self):
        input = """
            foo : function auto() {

            }
            func1 : function string() {
                return foo();
            }
            main : function void() {}
        """
        expect = """Type mismatch in expression: FuncCall("foo", [])"""
        self.assertTrue(TestChecker.test(input, expect,64))

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
        self.assertTrue(TestChecker.test(input, expect,65))

    def test_066(self):
        input = """  
            main : function void(){
                a : array [1] of float;
                b : array [2,2] of float;
                c : float = a[0] + b[0,0];
                d : array [2] of float = b[func1()];
            }

            func1 : function auto(){return "string";}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("string"))"""
        self.assertTrue(TestChecker.test(input, expect,66))

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
        self.assertTrue(TestChecker.test(input, expect,67))

    def test_068(self):
        input = """
            func1 : function integer (a : auto) {
                b : integer = a;
                return a;
                c : string = a + 1.0;
            }
            
            main : function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", StringType(), BinExpr("+", Id("a"), FloatLit(1.0)))"""
        self.assertTrue(TestChecker.test(input, expect,68))

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
        self.assertTrue(TestChecker.test(input, expect,69))

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
        self.assertTrue(TestChecker.test(input, expect,70))

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
        self.assertTrue(TestChecker.test(input, expect,71))

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
        self.assertTrue(TestChecker.test(input, expect,72))


    def test_073(self):
        input = """
            func1 : function integer (e : auto){
                e = 2.0;
                e = 2;
                e = "@";
            }

            main : function void() {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id("e"), StringLit("@"))"""
        self.assertTrue(TestChecker.test(input, expect,73))

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
        self.assertTrue(TestChecker.test(input, expect,74))

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
        self.assertTrue(TestChecker.test(input, expect,75))

    def test_076(self):
        input = """
            main : function void() {
                if(func1()){
                    a : auto = 1;
                } 
                else {
                    a : auto = 1;
                }
            }

            func1 : function void(){
            }
        """
        expect = """Type mismatch in expression: FuncCall("func1", [])"""
        self.assertTrue(TestChecker.test(input, expect,76))

    def test_077(self):
        input = """
            main : function void() {
                if(func1()){
                    a : auto = 1;
                } 
                else {
                    a : auto = 1;
                }
            }

            func1 : function auto(){
                return;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect,77))

    def test_078(self):
        input = """
            main : function void() {
                if(func1()){
                    a : auto = 1;
                } 
            }

            func1 : function auto(){
                return true;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect,78))

    def test_079(self):
        input = """
            main : function void() {}

            func1 : function auto(a : auto){
                if(func1(1)){
                    
                }
                c : boolean = func1(1);
                b : string = func1(1);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), FuncCall("func1", [IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect,79))

    def test_080(self):
        input = """
            main : function void() {
                id : auto = 8;
                for(id = 1, true, id)
                {
                    return;
                }
            }

            func1 : function auto(){
                return 1;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect,80))

    def test_081(self):
        input = """
            main : function void() {
                id : auto = "0";
                for(id = 1, true, id)
                {
                    return;
                }
            }

            func1 : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect,81))

    def test_082(self):
        input = """
            main : function void() {
                id : auto = 1.0;
                for(id = 1, true, id)
                {
                    return;
                }
            }

            func1 : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect,82))


    def test_083(self):
        input = """  
            main : function void() {
                a : auto = {{1,1},{"2",3}};
            }
        """
        expect = """Illegal array literal: ArrayLit([StringLit("2"), IntegerLit(3)])"""
        self.assertTrue(TestChecker.test(input, expect,83))

    def test_084(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 2, func1(), id)
                {
                    return;
                }
            }

            func1 : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect,84))

    def test_085(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 1, func1(), id)
                {
                    return;
                }
            }

            func1 : function integer(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), FuncCall("func1", []), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect,85))

    def test_086(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 1, true, true)
                {
                    return;
                }
            }

            func1 : function integer(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), BooleanLit(True), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect,86))

    def test_087(self):
        input = """
            foo_a : function float (a : auto) {
                b : auto = foo_a(1.0) + foo_b();
                return a;
            }
            
            main : function void() {}
            foo_b : function auto (){return "String";}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("String"))"""
        self.assertTrue(TestChecker.test(input, expect,87))

    def test_088(self):
        input = """
            main : function void() {

            }

            func1 : function auto(id : auto){
                for(id = 1, true, 1)
                {
                    return;
                }
                func1("a");
            }
        """
        expect = """Type mismatch in statement: CallStmt("func1",[StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect,88))

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

            func1 : function auto(){
                return true;
            }
        """
        expect = """Type mismatch in statement: WhileStmt(IntegerLit(1), ReturnStmt())"""
        self.assertTrue(TestChecker.test(input, expect,89))


    def test_090(self):
        input = """
            main : function void() {
                while(func1()) return;
            }

            func1 : function auto(){
                return true;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect,90))

    def test_091(self):
        input = """
            main : function void() {
                while(func1()) return;
            }

            func1 : function string(){
                return "2";
            }
        """
        expect = """Type mismatch in statement: WhileStmt(FuncCall("func1", []), ReturnStmt())"""
        self.assertTrue(TestChecker.test(input, expect,91))

    def test_092(self):
        input = """
            main : function void() {
                while(func1()) return;
            }

            func1 : function auto(){
                return true;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect,92))

    def test_093(self):
        input = """  
            main : function void() {
                a : array [1] of string;
                b : array [2,2] of integer;
                c : float = b[1, "string"];
            }
            
        """
        expect = """Type mismatch in expression: ArrayCell("b", [IntegerLit(1), StringLit("string")])"""
        self.assertTrue(TestChecker.test(input, expect,93))

    def test_094(self):
        input = """
            main : function void() {
                continue;
            }
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect,94))

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
        self.assertTrue(TestChecker.test(input, expect,95))

        
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
        self.assertTrue(TestChecker.test(input, expect,96))

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
        self.assertTrue(TestChecker.test(input, expect,97))

    def test_098(self):
        input = """
            foo : function float() {
                return 1;
                return "a";
            }
            main : function auto() {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect,98))

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
        self.assertTrue(TestChecker.test(input, expect,99))

    def test_100(self):
        input = """
            foo : function integer() {
                return func1();
            }
            func1 : function auto() {
                return "string";
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("string"))"""
        self.assertTrue(TestChecker.test(input, expect, 100))

    def test_101(self):
        input = """
            a : integer;
            foo_c : function void(a : integer) inherit foo_b{preventDefault();}
            foo_b : function void (a : integer, foo_b : string) {}
            foo_a : function void (a : integer, a : string) {}
            main : function void(){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 101))

