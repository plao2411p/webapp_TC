#Pedro Luis
from sys import flags, float_repr_style

from numpy.lib.twodim_base import triu_indices_from
import TCVar

n = int(len(TCVar.U)+1)  # filas
m = int(len(TCVar.Conjuntos))  # colúmnas


def SeparadorOperaciones(cadena):  # return String,Array,Dataframe

    def CreadorEstados():
        contador = 0
        for i in range(1, len(cadena), 1):
            if cadena[i:i+2] in TCVar.Operadores:
                DataO.loc[contador, 'Posición'] = i
                contador += 1

    def Izquierda(i):
        for j in range(i-1, -1, -1):
            for k in Data.columns.to_numpy():
                if cadena[j:i] == k:
                    # print('Izquierda')
                    # print(cadena[j:i])
                    return cadena[j:i]

    def Derecha(i):
        for j in range(i+2, len(cadena)+1):
            for k in Data.columns.to_numpy():
                if len(cadena) == j:
                    if cadena[-1] == k:
                        # print('Derecha')
                        # print(cadena[-1])
                        return cadena[-1]
                if cadena[i+2:j] == k:
                    # print('Derecha')
                    # print(cadena[i+2:j])
                    return cadena[i+2:j]

    def Operadora(i, o, d):
        vector = []
        p = Data.loc[:, i].to_numpy()
        q = Data.loc[:, d].to_numpy()
        if o == 'un':
            for j in ind[0:-1]:
                j -= 1
                if p[j] or q[j]:
                    vector.append(True)
                else:
                    vector.append(False)
        elif o == 'in':
            for j in ind[0:-1]:
                j -= 1
                if p[j] and q[j]:
                    vector.append(True)
                else:
                    vector.append(False)
        elif o == 'di':
            for j in ind[0:-1]:
                j -= 1
                if p[j] and not q[j]:
                    vector.append(True)
                else:
                    vector.append(False)
        elif o == 'ds':
            for j in ind[0:-1]:
                j -= 1
                if (p[j] or q[j]) and not (p[j] and q[j]):
                    vector.append(True)
                else:
                    vector.append(False)
        vector.append(None)
        return vector

    col = []  # Nombre Columnas
    ind = []  # Nombre Filas
    for i in TCVar.Conjuntos:
        col.append(i)
    for i in TCVar.U:
        ind.append(i)
    ind.append('Orden:')
    global Data
    Data = TCVar.pd.DataFrame(
        TCVar.np.full([n, m], 0, 'bool'),
        index=ind, columns=col
    )
    for j in col:
        Data.loc['Orden:', j] = 0
        for i in TCVar.U:
            if i in TCVar.SolicitarConjunto(j):
                Data.loc[i, j] = True
            else:
                Data.loc[i, j] = False

    copiaN_Total = TCVar.N_Total
    DataO = TCVar.pd.DataFrame(
        TCVar.np.full([TCVar.N_Total, 2], False, 'bool'),
        columns=['Posición', 'Estado']
    )
    CreadorEstados()
    #TCVar.N_PP = 2
    copiaN_PP = TCVar.N_PP

    # El moustruo buscador de operaciones
    for v in range(1, TCVar.N_Total+1):
        for l, i in enumerate(DataO.loc[:, 'Posición'].to_numpy()):
            if DataO.loc[:, 'Estado'].to_numpy()[l]:
                pass
            else:
                izquierda = Izquierda(i)
                derecha = Derecha(i)
                if izquierda is not None and derecha is not None:
                    #print(izquierda, cadena[i:i+2], derecha)
                    resul = Operadora(izquierda, cadena[i:i+2], derecha)

                    # and i != DataO.loc[:,'Posición'].to_numpy()[-1]:
                    if copiaN_PP == 0 and copiaN_Total == 1:
                        DataO.loc[l, 'Estado'] = True
                        Data.loc[:, izquierda+cadena[i:i+2]+derecha] = resul
                        copiaN_PP -= 1
                        copiaN_Total -= 1

                    elif copiaN_PP > 0:
                        DataO.loc[l, 'Estado'] = True
                        Data.loc[:, '('+izquierda+cadena[i:i+2] +
                                 derecha+')'] = resul
                        copiaN_PP -= 1
                        copiaN_Total -= 1
                    else:
                        DataO.loc[l, 'Estado'] = True
                        Data.loc[:, izquierda+cadena[i:i+2]+derecha] = resul
                        copiaN_PP -= 1
                        copiaN_Total -= 1

    Data.loc[:, 'Valores'] = None
    ordenes = len(Data.columns)-len(TCVar.Conjuntos)
    for i in range(1, ordenes+1):
        Data.iloc[-1, 3+i] = i
        pass
    for i, j in enumerate(Data.iloc[:, -2].to_numpy()):
        if j is True:
            Data.iloc[i, -1] = TCVar.U[i]
    conjuntov = []
    for i in Data.iloc[0:-1, -1].to_numpy():
        if i != None:
            conjuntov.append(i)
    return Data.columns[-2], conjuntov, Data
