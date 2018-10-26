#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from slimit import minify
from slimit.lexer import Lexer
from slimit.parser import Parser
from slimit.visitors.nodevisitor import ASTVisitor

text = """
 var a = function( obj ) {
       for ( var name in obj ) {
               return false;
         }
         return true;
 };
"""
# print(text)

# 1 Let’s minify some code
print("1 Let’s minify some code")
print(minify(text, mangle=True, mangle_toplevel=True))

# 2 Iterate over, modify a JavaScript AST and pretty print it
parser = Parser()
tree = parser.parse('for(var i=0; i<10; i++) {var x=5+i;}')
print("2 Iterate over, modify a JavaScript AST and pretty print it")
print(tree.to_ecma())

# 3 Writing custom node visitor
text = """
 var x = {
    "key1": "value1",
    "key2": "value2"
 };
 """


class MyVisitor(ASTVisitor):
    def visit(self, node):
        for prop in node:
            left, right = prop.left, prop.right
            print('Property key=%s, value=%s' % (left.value, right.value))
            self.visit(prop)


try:
    parser = Parser()
    tree = parser.parser(text)

    visitor = MyVisitor()
    visitor.visit(tree)
except Exception as e:
    logging.exception(e)

# 4 Using lexer in your project
print('4 Using lexer in your project')
lexer = Lexer()
lexer.input('a=1;x=1+3;')
for token in lexer:
    print(token)


