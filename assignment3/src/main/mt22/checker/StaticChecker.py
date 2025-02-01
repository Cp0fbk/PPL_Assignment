#2212631

from Utils import Utils
from StaticError import *
from functools import reduce
from AST import *
from Visitor import Visitor

class MT22Grammar:
    def __init__(self, name : str, typ ):
        self.name = name
        self.typ = typ
        
class Variable_ProtoType(MT22Grammar):
    def __init__(self, name : str, typ):
        super().__init__(name, typ)
        
class Param_ProtoType(MT22Grammar):
    def __init__(self, name : str, typ, out : bool = False, inherit : bool = False):
        super().__init__(name, typ)
        self.out = out
        self.inherit = inherit

class Function_ProtoType(MT22Grammar):
    def __init__(self, name, typ, param , parent = None):
        super().__init__(name, typ)
        self.param = param
        self.parent = parent     

class GetScope():
    def __init__(self, symbol, typL  = AutoType()):
        self.symbol = symbol 
        self.typL = typL
    
class StaticChecker(Visitor, Utils):
    def __init__(self,ast):
        self.ast = ast
        self.lfunc = [
                Function_ProtoType("readInteger", IntegerType(), []),
                Function_ProtoType("readFloat", FloatType(), []),
                Function_ProtoType("readBoolean", BooleanType(), []),
                Function_ProtoType("readString", StringType(), []),
                Function_ProtoType("printInteger", VoidType(), [Param_ProtoType("printInteger", IntegerType())]),
                Function_ProtoType("printFloat", VoidType(), [Param_ProtoType("printFloat", FloatType())]),
                Function_ProtoType("printBoolean", VoidType(), [Param_ProtoType("printBoolean", BooleanType())]),
                Function_ProtoType("printString", VoidType(), [Param_ProtoType("printString", StringType())]),
            ]
        self.using_func = None 
        self.putInLoop = 0
        self.returned = False

    def CheckType(self, lhs , rhs , isCheck : bool = True):
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            if len(lhs.dimensions) != len(rhs.dimensions) or not self.CheckType(rhs.typ, lhs.typ, False):
                return False
            for index in range(len(lhs.dimensions)):
                if lhs.dimensions[index] != rhs.dimensions[index]:
                    return False
            return True
        if isCheck and type(lhs) in [FloatType] and type(rhs) in [IntegerType, FloatType]:
            return True
        return type(lhs) == type(rhs)

    def checkInheritedParam(self, paramName : str, function):
        if function is None:
            return None
        
        for func in self.lfunc:
            if func.name == function.name:
                for param in func.param:
                    if param.inherit == True and param.name == paramName:
                        return param
        
        return self.checkInheritedParam(paramName, function.parent)

    def check(self):
        return self.visitProgram(self.ast,None)
    
    def visitProgram(self,ast : Program, param):
        globalname = ["readInteger", "readFloat", "readBoolean", "readString", 
                      "printInteger", "printFloat", "printBoolean", 
                      "printString", "super", "preventDefault"]
        names = []
        funcs = []
        hasReturn = False
        for decl in ast.decls:
            if isinstance(decl, FuncDecl):
                name = decl.name
                if name in names + globalname :
                    raise Redeclared(Function(), name)
                names.append(name)
                funcs.append(name)

                if name == 'main':
                    if type(decl.return_type) is AutoType and len(decl.body.body) == 0:
                        decl.return_type = VoidType()
                    if type(decl.return_type) is AutoType and len(decl.body.body) > 0:
                        lstmt = decl.body.body
                        for stmt in lstmt:
                            if isinstance(stmt, ReturnStmt): hasReturn = True
                        if not hasReturn: decl.return_type = VoidType()

                lparam = []
                parent_func = Function_ProtoType(decl.inherit, None, []) if decl.inherit else None
                self.lfunc.append(Function_ProtoType(name, decl.return_type, [self.visitParamDecl(p, lparam) for p in decl.params], parent = parent_func))

            elif isinstance(decl, VarDecl):
                name = decl.name
                if name in names + globalname:
                    raise Redeclared(Variable(), name)    
                names.append(name)
        
        for func in self.lfunc:
                if func.parent and func.parent.name not in funcs + globalname:
                    raise Undeclared(Function(), func.parent.name)
                if isinstance(func.typ, AutoType) and func.parent:
                    for f in self.lfunc:
                        if f.name == func.parent.name:
                            func.typ = f.typ
   
        param = GetScope([[]], AutoType())
        [self.visit(using, param) for using in ast.decls]

        has_main = False
        for func in self.lfunc:
            if func.name == "main":
                has_main = True
                if not isinstance(func.typ, VoidType) or len(func.param) > 0:
                    raise NoEntryPoint()

        if not has_main:
            raise NoEntryPoint()
        
    def visitParamDecl(self, ast : ParamDecl, lparam):
        for param in lparam:
            if param.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
        new_param = Param_ProtoType(ast.name, ast.typ, ast.out, ast.inherit)
        lparam.append(new_param)
        return new_param

    def visitVarDecl(self, ast : VarDecl, param : GetScope):
        for using in param.symbol[0]:
            if using.name == ast.name:
                raise Redeclared(Variable(), ast.name)

        param.symbol[0].append(Variable_ProtoType(ast.name, ast.typ))    

        if ast.init is None and type(ast.typ) is AutoType:
            raise Invalid (Variable(), ast.name)
        
        elif ast.init is None:
            return
        
        typlhs = ast.typ
        typrhs = self.visit(ast.init, GetScope(param.symbol, ast.typ))
        
        if isinstance(ast.typ, AutoType):
            param.symbol[0][-1].typ = typrhs
        elif not self.CheckType(typlhs,typrhs):
            raise TypeMismatchInVarDecl(ast)
        
    def visitFuncDecl(self, ast : FuncDecl, param : GetScope):
        for using in self.lfunc:
            if using.name == ast.name:
                self.using_func = using
                break  

        if self.using_func.param and self.using_func.parent:
            for p in self.using_func.param:  
                for fparent in self.lfunc:
                    if fparent.name == self.using_func.parent.name:
                        inheritedParam = self.checkInheritedParam(p.name, fparent)
                        if inheritedParam is not None:
                            raise Invalid(Parameter(), p.name)
                        
        lstmtInBlockFunc =  ast.body.body

        if self.using_func.parent:
            if len(ast.body.body) == 0:
                fn = self.using_func.parent.name
                for func in self.lfunc:
                    if func.name == fn:
                        if len(func.param) != 0:
                            raise InvalidStatementInFunction(ast.name)
                        
            else:
                block1 = lstmtInBlockFunc[0]
                lparam = []

                if type(block1) is CallStmt and block1.name == "preventDefault":
                    lstmtInBlockFunc = lstmtInBlockFunc[1:]
                elif type(block1) is CallStmt and block1.name == "super":
                    fn = self.using_func.parent.name
                    for func in self.lfunc:
                        if func.name == fn:
                            lparam = func.param
                    lstmtInBlockFunc = lstmtInBlockFunc[1:]  

                else:
                    raise InvalidStatementInFunction(ast.name)
                    
                if len(block1.args) > len(lparam):
                    raise TypeMismatchInExpression(block1.args[len(lparam)])
                elif len(block1.args) < len(lparam):
                    raise TypeMismatchInExpression(None)
                
                for idx in range(len(lparam)):
                    lhs = lparam[idx].typ
                    rhs = self.visit(block1.args[idx],GetScope([[]] + [self.using_func.param] + param.symbol, lhs))
                    if type(lhs) is AutoType:
                        lparam[idx].typ = rhs
                    elif not self.CheckType(lhs,rhs):
                        raise TypeMismatchInExpression(block1.args[idx])

        self.returned = False
        param = GetScope([[]] + [self.using_func.param] + param.symbol, AutoType())

        for stmt in lstmtInBlockFunc:
            self.visit(stmt, param)
            if isinstance(stmt, ReturnStmt): self.returned = True

        if self.returned is False:
            self.using_func.typ = VoidType()
     
    def visitId(self, ast : Id, param : GetScope):

        if param.symbol[-1]:
            for varbs in param.symbol[:-1]:
                for var in varbs:
                    if var.name == ast.name:
                        if type(var.typ) is AutoType:
                            var.typ = param.typL
                        return var.typ
                    
        else:
            for varbs in param.symbol:
                for var in varbs:
                    if var.name == ast.name:
                        if type(var.typ) is AutoType:
                            var.typ = param.typL
                        return var.typ

        if len(param.symbol) != 1:
            for func in self.lfunc:
                if self.using_func.parent:
                    if func.name == self.using_func.parent.name:
                        param_inherit = self.checkInheritedParam(ast.name, func)
                        if param_inherit is not None:
                            if type(param_inherit.typ) is AutoType:
                                param_inherit.typ = param.typL
                            return param_inherit.typ

        if param.symbol[-1]:
            varbs = param.symbol[-1]
            for var in varbs:
                if var.name == ast.name:
                    if type(var.typ) is AutoType:
                        var.typ = param.typL
                    return var.typ                
        raise Undeclared(Identifier(), ast.name)
    
    def visitFuncCall(self, ast : FuncCall, param : GetScope):
        for funcs in self.lfunc:
            if funcs.name == ast.name:
                lparam = funcs.param
                if len(ast.args) != len(lparam):
                    raise TypeMismatchInExpression(ast)
                
                for idx in range(len(lparam)): 
                    lhs = lparam[idx].typ 
                    rhs = self.visit(ast.args[idx], GetScope(param.symbol,lhs))
                    if isinstance(lhs,AutoType):
                        lparam[idx].typ = rhs

                    elif not self.CheckType(lhs,rhs):
                        raise TypeMismatchInExpression(ast)
                    
                if isinstance(funcs.typ, AutoType):
                    funcs.typ = param.typL

                elif self.CheckType(funcs.typ,VoidType()):
                    raise TypeMismatchInExpression(ast)
                
                return funcs.typ
            
        raise Undeclared(Function(), ast.name)

    def visitCallStmt(self, ast : CallStmt, param : GetScope): 
        func = None
        for function in self.lfunc:
            if function.name == ast.name:
                func = function
                break

        if func is None:
            raise Undeclared(Function(), ast.name)
        
        if len(ast.args) != len(func.param):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(ast.args)):
            arg = ast.args[i]
            param_type = func.param[i].typ
        
            if isinstance(param_type, AutoType):
                inferred_type = self.visit(arg, GetScope([[]], AutoType()))
                func.param[i].typ = inferred_type
                param_type = inferred_type

            else:
                arg_type = self.visit(arg, GetScope([[]], param_type))
                
                if not self.CheckType(param_type, arg_type):
                    raise TypeMismatchInStatement(ast)

    def visitAssignStmt(self,ast : AssignStmt, param : GetScope):
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, GetScope(param.symbol, lhs))
        
        inferlhs = self.visit(ast.lhs, GetScope(param.symbol, rhs))

        if isinstance(lhs, AutoType):
            lhs = inferlhs

        elif self.CheckType(lhs,rhs) is False:
            raise TypeMismatchInStatement(ast)

    def visitBlockStmt(self, ast : BlockStmt, param : GetScope):
        isReturn = self.returned
        newSym = [[]] + param.symbol
        for using in ast.body:
            self.visit(using, GetScope(newSym, AutoType()))
            if isinstance(using, ReturnStmt):
                self.returned = True
        if self.returned:
            isReturn = True           
        self.returned = isReturn

    def visitIfStmt(self, ast : IfStmt, param : GetScope):

        lhs = BooleanType()
        rhs = self.visit(ast.cond, GetScope(param.symbol, lhs))

        if not self.CheckType(lhs, rhs):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt,param)

        if ast.fstmt:
            self.visit(ast.fstmt,param)
        
    def visitForStmt(self, ast : ForStmt, param : GetScope):
        lhs = self.visit(ast.init.lhs, GetScope(param.symbol, IntegerType()))
        rhs = self.visit(ast.init.rhs, GetScope(param.symbol, IntegerType()))

        if not self.CheckType(lhs, rhs):
            raise TypeMismatchInStatement(ast)

        lhs = BooleanType()
        rhs = self.visit(ast.cond, GetScope(param.symbol, lhs))

        if not self.CheckType(lhs, rhs):
            raise TypeMismatchInStatement(ast)

        lhs = IntegerType()
        rhs = self.visit(ast.upd, GetScope(param.symbol, lhs))

        if not self.CheckType(lhs, rhs):
            raise TypeMismatchInStatement(ast)

        self.putInLoop += 1
        self.visit(ast.stmt, param)
        self.putInLoop -= 1

    def visitWhileStmt(self, ast : WhileStmt, param : GetScope):
        lhs = BooleanType()
        rhs = self.visit(ast.cond, GetScope(param.symbol, lhs))

        if not self.CheckType(lhs, rhs):
            raise TypeMismatchInStatement(ast)

        self.putInLoop += 1
        self.visit(ast.stmt, param)
        self.putInLoop -= 1        
    
    def visitDoWhileStmt(self, ast : DoWhileStmt, param : GetScope):
        lhs = BooleanType()
        rhs = self.visit(ast.cond, GetScope(param.symbol, lhs))

        if not self.CheckType(lhs, rhs):
            raise TypeMismatchInStatement(ast)

        self.putInLoop += 1
        self.visit(ast.stmt, param)
        self.putInLoop -= 1    

    def visitBreakStmt(self, ast : BreakStmt, param : GetScope):
        if self.putInLoop == 0: raise MustInLoop(ast)

    def visitContinueStmt(self, ast : ContinueStmt, param : GetScope):
        if self.putInLoop == 0: raise MustInLoop(ast)

    def visitReturnStmt(self, ast : ReturnStmt, param : GetScope):
        if self.returned is True: return

        lhs = self.using_func.typ
        rhs = self.visit(ast.expr, GetScope(param.symbol, lhs)) if ast.expr else VoidType()

        if isinstance(lhs, AutoType):
            lhs = rhs
            self.using_func.typ = rhs

        if isinstance(rhs, AutoType):
            rhs = lhs

        if not self.CheckType(lhs, rhs):
            raise TypeMismatchInStatement(ast)
    def visitBinExpr(self, ast : BinExpr, param : GetScope):
        if ast.op in ['-', '+', '*', '/']:
            typspread = IntegerType() if type(param.typL) is not FloatType else param.typL

            typL = self.visit(ast.left, GetScope(param.symbol, typspread))
            typR = self.visit(ast.right, GetScope(param.symbol, typspread))

            if type(typL) is not IntegerType and type(typL) is not FloatType:
                raise TypeMismatchInExpression(ast)
            if type(typR) is not IntegerType and type(typR) is not FloatType:
                raise TypeMismatchInExpression(ast)
            
            return IntegerType() if type(typL) is IntegerType or type(typR) is IntegerType else FloatType()
        
        if ast.op in ['==', '!=']:
            typspread = IntegerType() if type(param.typL) is not BooleanType else param.typL

            typL = self.visit(ast.left, GetScope(param.symbol, typspread))
            typR = self.visit(ast.right, GetScope(param.symbol, typspread))

            if type(typL) is not IntegerType and type(typL) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            if type(typR) is not IntegerType and type(typR) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            
            return BooleanType()
        
        if ast.op in ['<', '>', '<=', '>=']:
            typspread = IntegerType() if type(param.typL) is not FloatType else param.typL

            typL = self.visit(ast.left, GetScope(param.symbol, typspread))
            typR = self.visit(ast.right, GetScope(param.symbol, typspread))

            if type(typL) is not IntegerType and type(typL) is not FloatType:
                raise TypeMismatchInExpression(ast)
            if type(typR) is not IntegerType and type(typR) is not FloatType:
                raise TypeMismatchInExpression(ast)
            
            return BooleanType()
        
        if ast.op in ['&&', '||']:
            typL = self.visit(ast.left, GetScope(param.symbol, BooleanType()))
            typR = self.visit(ast.right, GetScope(param.symbol, BooleanType()))

            if type(typL) is not BooleanType or type(typR) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            
            return BooleanType()
        
        if ast.op in ['::']:
            typL = self.visit(ast.left, GetScope(param.symbol, StringType()))
            typR = self.visit(ast.right, GetScope(param.symbol, StringType()))

            if type(typL) is not StringType or type(typR) is not StringType:
                raise TypeMismatchInExpression(ast)
            
            return StringType()
        
        if ast.op in ['%']:
            typL = self.visit(ast.left, GetScope(param.symbol, IntegerType()))
            typR = self.visit(ast.right, GetScope(param.symbol, IntegerType()))

            if type(typL) is not IntegerType or type(typR) is not IntegerType:
                raise TypeMismatchInExpression(ast)
                       
            return IntegerType()

    def visitUnExpr(self, ast : UnExpr, param : GetScope):
        if ast.op == '!':
            typp = self.visit(ast.val, GetScope(param.symbol, BooleanType()))

            if type(typp) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            
            return BooleanType()
        
        if ast.op == '-':
            typ1 = self.visit(ast.val, GetScope(param.symbol, IntegerType()))
            typ2 = self.visit(ast.val, GetScope(param.symbol, FloatType()))

            if type(typ1) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            if type(typ2) is not FloatType:
                raise TypeMismatchInExpression(ast)
            
            return IntegerType() if type(typ1) is IntegerType else FloatType()
   
    def visitArrayCell(self, ast : ArrayCell, param : GetScope):
        type_E1 = self.visit(Id(ast.name), param)
        if type(type_E1) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        for index in ast.cell:
            type_index = self.visit(index, GetScope(param.symbol, IntegerType()))
            
            if not self.CheckType(type_index, IntegerType()):
                raise TypeMismatchInExpression(ast)
            
        if len(type_E1.dimensions) == len(ast.cell):
            return type_E1.typ
        
        return ArrayType(type_E1.dimensions[len(ast.cell):], type_E1.typ)

    def visitArrayLit(self, ast : ArrayLit, param : GetScope):
        typArrayEle = self.visit(ast.explist[0], param)

        for exp in ast.explist:
            type_element = self.visit(exp, param)
            if not self.CheckType(typArrayEle, type_element,False):
                raise IllegalArrayLiteral(ast)
            
        if type(typArrayEle) is not ArrayType:
            return ArrayType([len(ast.explist)], typArrayEle)
       
        return ArrayType([len(ast.explist)] + typArrayEle.dimensions, typArrayEle.typ)

    def visitIntegerLit(self, ast : IntegerLit, param : GetScope): 
        return IntegerType()
    def visitFloatLit(self, ast : FloatLit, param : GetScope): 
        return FloatType()
    def visitStringLit(self, ast : StringLit, param : GetScope): 
        return StringType()
    def visitBooleanLit(self, ast : BooleanLit, param : GetScope): 
        return BooleanType()
