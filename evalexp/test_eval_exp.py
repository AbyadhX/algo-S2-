# -*- coding: utf-8 -*-
"""
Sept. 2019
@author: nathalie
S2# tutorial: examples to tests yours functions
"""

import evalexp

# from files/binTree_exp1.png

rpn_1 = '3 5 1 + * 3 2 - 7 * +'
pn_1 = '+ * 3 + 5 1 * - 3 2 7'
expPar_1 = '( ( 3 * ( 5 + 1 ) ) + ( ( 3 - 2 ) * 7 ) )'
exp_1 = '3 * ( 5 + 1 ) + ( 3 - 2 ) * 7'

# from files/binTree_exp2.png

rpn_2 = '4 5 * 10 4 - 2 1 + / +'
pn_2 = '+ * 4 5 / - 10 4 + 2 1'
expPar_2 = '( ( 4 * 5 ) + ( ( 10 - 4 ) / ( 2 + 1 ) ) )'
exp_2 = '4 * 5 + ( 10 - 4 ) / ( 2 + 1 )'

rpn_3 = '12 40 + 5 7 - * 4 -1 11 // + *'
# TODO: write the other versions of the above expression!
