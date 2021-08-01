#Pedro Luis
from numpy import False_, fabs, true_divide
import TCVar  # Teoría de conjuntos variables
#import TeoriaConjuntos as tc


def DepuradorString(operation):  # retunr bool, String

    def SinNúmeros(cadena):  # return bool
        for i in TCVar.U:
            if str(i) in cadena:
                return False
        if str(0) in cadena:
            return False
        return True

    def ConOperaciones(cadena):  # return false or Strig
        # Quita espacios al inicio y final
        cadena = cadena.strip()
        cadena = cadena.upper()
        if cadena[0] in '(' and cadena[-1] in ')' and len(cadena) == 6:
            cadena = cadena.replace('(', ' ')
            cadena = cadena.replace(')', ' ')
            cadena = cadena.strip()
        if len(cadena) == 1 and cadena in TCVar.Conjuntos:
            TCVar.N_Total += 1
            return cadena
        if len(cadena) >= 4:
            if "UN" in cadena:
                TCVar.N_Un = cadena.count("UN")
                cadena = cadena.replace("UN", "un")
            if "IN" in cadena:
                TCVar.N_I = cadena.count("IN")
                cadena = cadena.replace("IN", "in")
            if "DS" in cadena:
                TCVar.N_DS = cadena.count("DS")
                cadena = cadena.replace("DS", "ds")
            if "DI" in cadena:
                TCVar.N_D = cadena.count("DI")
                cadena = cadena.replace("DI", "di")
            TCVar.N_Total = TCVar.N_Un + TCVar.N_I + TCVar.N_DS + TCVar.N_D
            if TCVar.N_Total != 0:
                return cadena
            else:
                return False
        else:
            return False

    def VerificadorParentesis(cadena):  # return bool

        contadord = 0
        contadori = 0

        TCVar.N_PP = cadena.count('(') + cadena.count(')')

        if TCVar.N_PP == 0 and TCVar.N_Total == 1:
            return True
        elif TCVar.N_PP % 2 == 0:
            TCVar.N_PP = int(TCVar.N_PP / 2)
            if TCVar.N_PP + 1 != TCVar.N_Total:
                return False
        else:
            return False

        if cadena[0] in '(':
            if cadena[1] in TCVar.Conjuntos or cadena[1] in '(':
                contadord += 1
            else:
                return False
        if cadena[1] in '(':
            if cadena[0] in '(':
                contadord += 1
            else:
                return False
        if cadena[-1] in ')':
            if cadena[-1] in TCVar.Conjuntos or cadena[-1] in ')':
                contadori += 1
            else:
                return False
        if cadena[-2] in ')':
            if cadena[-1] in ')':
                contadori += 1
            else:
                return False

        for i in range(2, len(cadena)-2):
            if cadena[i] in '(':
                if cadena[i+1] in '(' or cadena[i+1] in TCVar.Conjuntos:
                    pass
                else:
                    return False
                if cadena[i-1] in '(' or cadena[i-2:i] in TCVar.Operadores:
                    pass
                else:
                    return False
                contadord += 1
            elif cadena[i] in ')':
                if cadena[i+1] in ')' or cadena[i+1:i+3] in TCVar.Operadores:
                    pass
                else:
                    False
                if cadena[i-1] in ')' or cadena[i-1] in TCVar.Conjuntos:
                    pass
                else:
                    return False
                contadori += 1
        if contadord + contadori == 2*TCVar.N_PP:
            return True
        else:
            return False

    def VerificadorOperacioens(cadena):  # return bool
        if cadena[0:2] in TCVar.Operadores:
            return False
        if cadena[-2:len(cadena)] in TCVar.Operadores:
            return False
        for i in range(0, len(cadena)-1):
            if cadena[i] in TCVar.Conjuntos and cadena[i+1] in TCVar.Conjuntos:
                return False
        if len(cadena) == 4:
            return True
        for i in range(1, len(cadena)-1):
            if cadena[i:i+2] in TCVar.Operadores:
                if cadena[i-1] in TCVar.Conjuntos or cadena[i-1] in '(' or cadena[i-1] in ')':
                    pass
                else:
                    return False
                if cadena[i+2] in TCVar.Conjuntos or cadena[i+2] in '(' or cadena[i+2] in ')':
                    pass
                else:
                    return False
        return True

    if SinNúmeros(operation):
        operation = ConOperaciones(operation)
        if operation is False:
            return False, 'No ingresó una operación válida'
        else:
            if len(operation) != 1:
                if VerificadorOperacioens(operation):
                    if VerificadorParentesis(operation):
                        return True, operation
                    else:
                        return False, 'Mal ingreso en los parentesisi'
                else:
                    operation = None
                    return False, 'Mal ingreso de conjunto o parentesis'
            else:
                return True, operation
    else:
        operation = None
        return False, 'La operación no puede contener números'
