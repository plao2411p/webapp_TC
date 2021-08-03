
from pandas.core.frame import DataFrame
import TCVar  # Teoría de conjuntos variables
import DS  # Depurador de String
import OperadorS
import streamlit as st


def Info():
    st.write(
        """
        * Número de uniones: {}
        * Numero de intersecciones: {}
        * Numero de diferencias: {}
        * Numero de diferencias simétricas: {}
        * Pares de parentesis: {}    
        * Numero de operaciones: {}
        """.format(
            TCVar.N_Un, TCVar.N_I, TCVar.N_D, TCVar.N_DS,
            TCVar.N_PP, TCVar.N_Total
        )
    )


def Inicio():
    st.write(
        """
        Operaciones entre conjuntos:
        * Unión -> un
        * Intersección -> in
        * Diferencia -> di
        * Complemento -> UdiA
        * Diferencia simétrica -> ds

        Para realizar varias operaciones debes usar parentesis.
        
        Ejemplo:

        * (AunB)diC
        * Ain(CdsB)
        * ((AunB)in(CinB))un(AdiB)
        ## Conjuntos: 
        ### U = {}
        ### A = {}
        ### B = {}
        ### C = {}
        """.format(TCVar.U, TCVar.A, TCVar.B, TCVar.C)
    )


def VaciarVariables():
    TCVar.N_Un = 0  # uniones
    TCVar.N_I = 0  # intersecciones
    TCVar.N_D = 0  # diferencias
    TCVar.N_DS = 0  # diferencias simétricas
    TCVar.N_Total = 0  # total de operaciones
    TCVar.N_PP = 0  # Numero de pares de parentesis


st.title('Teoría de Conjuntos')

Inicio()

tex_input = st.text_input('Ingrese la operación:')

if len(tex_input) != 0:
    # Return Bool, String
    verificadorS, operación = DS.DepuradorString(tex_input)
    if verificadorS:
        if len(operación) == 1:
            st.write('Operación: ')
            st.write(
                """
                ## {} = {}
                """.format(operación, TCVar.SolicitarConjunto(operación))
            )
            VaciarVariables()
        else:
            S, V, Data = OperadorS.SeparadorOperaciones(operación)
            st.write(
                """
                ### Operación: 
                ## {} = {}
                """.format(S, V)
            )
            st.markdown(Data.to_markdown())
            VaciarVariables()
            OperadorS.Data = None
    else:
        st.write(operación)
        VaciarVariables()
        OperadorS.Data = None
else:
    VaciarVariables()
    OperadorS.Data = None
