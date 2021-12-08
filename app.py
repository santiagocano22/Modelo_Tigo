import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st


# Path del modelo preentrenado
MODEL_PATH = 'pickle_model.pkl'


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)
    
    if preds==1:
        return "VISITAR"
    else:
        return "NO VISITAR"


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE RECOMENDACIÓN PARA VISITA DE NODOS </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    ANT = st.text_input("Antiguedad nodo:")
    EST = st.text_input("Estrato nodo:")
    INS = st.text_input("Instalaciones RGU:")
    CAL = st.text_input("Calidad Q:")
    INP = st.text_input("Infracciones performance:")
    INU = st.text_input("Infracciones utilización:")
    OCU = st.text_input("Tasa de ocupación:")
    IND = st.text_input("Tasa indisponibilidad:")
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(ANT.title()),
                    np.float_(EST.title()),
                    np.float_(INS.title()),
                    np.float_(CAL.title()),
                    np.float_(INP.title()),
                    np.float_(INU.title()),
                    np.float_(OCU.title()),
                    np.float_(IND.title())]
        predictS = model_prediction(x_in, model)
        st.success('LA RECOMENDACIÓN ES: {}'.format(predictS).upper())

if __name__ == '__main__':
    main()


