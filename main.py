import streamlit as st
import pandas as pd
from cl_model import CL

config = {
    "claim_sz_mu": 30774,
    "claim_rate_lambd": 74,
    "u": 10_000_000,
    "c": 2_309_004,
    "time_steps": 1000
}

def generate_simulations_data(n_simulations, config_sliders):

    ### UPDATE FROM SLIDERS INPUT ###
    for key, val in config_sliders.items():
        config[key] = val

    ### GENERATE SIMULATIONS ###
    cl = CL(config)
    arrays = cl.generate_simulations(n_simulations)

    ### ADD RUIN LINE THRESHOLD ####
    zeros = [0]*1000
    arrays.append(zeros)

    df = pd.DataFrame(arrays).T
    return df


def main():

    ### MAIN ###
    st.title('Modelo Cramer-Lundberg')
    st.subheader('Simulaciones')

    line_chart = st.line_chart([10_000_000.0])

    ### SIDE BAR ###
    st.sidebar.title("Valores Iniciales")
    n_simulations = st.sidebar.slider('Número de simulaciones', 1,15,1)
    u = st.sidebar.number_input('Capital Inicial', 10_000_000)
    c = st.sidebar.number_input('Primas Diarias', 2_309_004)

    config_sliders = {'u': u, 'c':c}

    ### BUTTON LOGIC ###
    if st.button('Run'):
        # Loading Spinner
        with st.spinner('Simulando'):
            df = generate_simulations_data(n_simulations, config_sliders)
            line_chart.add_rows(df)

        st.success('Simulación terminada!')

    
if __name__ == "__main__":
    main()