
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightEXPONENTnonassocUMINUSLESS_THANGREATER_THANEQUALSASSIGN COLON DIVIDE EQUALS EXPONENT GREATER_THAN GREATER_THAN_EQUALS IDENTIFIER IF LESS_THAN LESS_THAN_EQUALS LPAREN MINUS NEWLINE NUMBER PLUS RPAREN TIMES WHILEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : assignment\n                 | expr\n                 | if_statement\n                 | while_statement\n                 | emptyassignment : IDENTIFIER ASSIGN exprexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr TIMES expr\n            | expr DIVIDE expr\n            | expr EXPONENT exprexpr : MINUS expr %prec UMINUSexpr : LPAREN expr RPARENexpr : NUMBERexpr : IDENTIFIERif_statement : IF expr COLON statement_listwhile_statement : WHILE expr COLON statement_listempty :expr : expr EQUALS expr\n            | expr LESS_THAN expr\n            | expr LESS_THAN_EQUALS expr\n            | expr GREATER_THAN expr\n            | expr GREATER_THAN_EQUALS expr'
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[9,9,-3,-4,-5,-6,-7,-8,-18,28,28,-17,28,28,-2,28,28,28,28,28,28,28,28,28,28,28,-15,-18,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-9,-16,9,9,9,9,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[10,10,-3,-4,17,-6,-7,-8,-18,10,10,-17,10,10,-2,10,10,10,10,10,10,10,10,10,10,10,-15,-18,17,17,17,-10,-11,-12,-13,-14,-22,-23,17,-25,17,17,-16,10,10,10,10,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[11,11,-3,-4,-5,-6,-7,-8,-18,11,11,-17,11,11,-2,11,11,11,11,11,11,11,11,11,11,11,-15,-18,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-9,-16,11,11,11,11,]),'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[12,12,-3,-4,-5,-6,-7,-8,-18,12,12,-17,12,12,-2,12,12,12,12,12,12,12,12,12,12,12,-15,-18,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-9,-16,12,12,12,12,]),'IF':([0,2,3,4,5,6,7,8,9,12,15,27,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[13,13,-3,-4,-5,-6,-7,-8,-18,-17,-2,-15,-18,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-9,-16,13,13,13,13,]),'WHILE':([0,2,3,4,5,6,7,8,9,12,15,27,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[14,14,-3,-4,-5,-6,-7,-8,-18,-17,-2,-15,-18,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-9,-16,14,14,14,14,]),'$end':([0,1,2,3,4,5,6,7,8,9,12,15,27,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-21,0,-1,-3,-4,-5,-6,-7,-8,-18,-17,-2,-15,-18,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-9,-16,-21,-21,-19,-20,]),'PLUS':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[16,-18,-17,-15,-18,16,16,16,-10,-11,-12,-13,-14,-22,-23,16,-25,16,16,-16,]),'TIMES':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[18,-18,-17,-15,-18,18,18,18,18,18,-12,-13,-14,-22,-23,18,-25,18,18,-16,]),'DIVIDE':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[19,-18,-17,-15,-18,19,19,19,19,19,-12,-13,-14,-22,-23,19,-25,19,19,-16,]),'EXPONENT':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[20,-18,-17,-15,-18,20,20,20,20,20,20,20,20,-22,-23,20,-25,20,20,-16,]),'EQUALS':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[21,-18,-17,None,-18,21,21,21,21,21,21,21,21,None,None,21,None,21,21,-16,]),'LESS_THAN':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[22,-18,-17,None,-18,22,22,22,22,22,22,22,22,None,None,22,None,22,22,-16,]),'LESS_THAN_EQUALS':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[23,-18,-17,-15,-18,23,23,23,-10,-11,-12,-13,-14,-22,-23,23,-25,23,23,-16,]),'GREATER_THAN':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[24,-18,-17,None,-18,24,24,24,24,24,24,24,24,None,None,24,None,24,24,-16,]),'GREATER_THAN_EQUALS':([5,9,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[25,-18,-17,-15,-18,25,25,25,-10,-11,-12,-13,-14,-22,-23,25,-25,25,25,-16,]),'ASSIGN':([9,],[26,]),'RPAREN':([12,27,28,29,32,33,34,35,36,37,38,39,40,41,43,],[-17,-15,-18,43,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-16,]),'COLON':([12,27,28,30,31,32,33,34,35,36,37,38,39,40,41,43,],[-17,-15,-18,44,45,-10,-11,-12,-13,-14,-22,-23,-24,-25,-26,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,44,45,],[2,46,47,]),'statement':([0,2,44,45,46,47,],[3,15,3,3,15,15,]),'assignment':([0,2,44,45,46,47,],[4,4,4,4,4,4,]),'expr':([0,2,10,11,13,14,16,17,18,19,20,21,22,23,24,25,26,44,45,46,47,],[5,5,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,5,5,5,5,]),'if_statement':([0,2,44,45,46,47,],[6,6,6,6,6,6,]),'while_statement':([0,2,44,45,46,47,],[7,7,7,7,7,7,]),'empty':([0,2,44,45,46,47,],[8,8,8,8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',17),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',21),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',22),
  ('statement -> assignment','statement',1,'p_statement','parser.py',29),
  ('statement -> expr','statement',1,'p_statement','parser.py',30),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',31),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',32),
  ('statement -> empty','statement',1,'p_statement','parser.py',33),
  ('assignment -> IDENTIFIER ASSIGN expr','assignment',3,'p_assignment','parser.py',37),
  ('expr -> expr PLUS expr','expr',3,'p_expr','parser.py',42),
  ('expr -> expr MINUS expr','expr',3,'p_expr','parser.py',43),
  ('expr -> expr TIMES expr','expr',3,'p_expr','parser.py',44),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr','parser.py',45),
  ('expr -> expr EXPONENT expr','expr',3,'p_expr','parser.py',46),
  ('expr -> MINUS expr','expr',2,'p_expr_uminus','parser.py',54),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr_group','parser.py',58),
  ('expr -> NUMBER','expr',1,'p_expr_number','parser.py',62),
  ('expr -> IDENTIFIER','expr',1,'p_expr_identifier','parser.py',66),
  ('if_statement -> IF expr COLON statement_list','if_statement',4,'p_if_statement','parser.py',74),
  ('while_statement -> WHILE expr COLON statement_list','while_statement',4,'p_while_statement','parser.py',79),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',84),
  ('expr -> expr EQUALS expr','expr',3,'p_expression_comparison','parser.py',88),
  ('expr -> expr LESS_THAN expr','expr',3,'p_expression_comparison','parser.py',89),
  ('expr -> expr LESS_THAN_EQUALS expr','expr',3,'p_expression_comparison','parser.py',90),
  ('expr -> expr GREATER_THAN expr','expr',3,'p_expression_comparison','parser.py',91),
  ('expr -> expr GREATER_THAN_EQUALS expr','expr',3,'p_expression_comparison','parser.py',92),
]
