import streamlit as st
import pandas as pd
from cl_model_app import CL

config = {
    "claim_sz_shape": 0.99264,
    "claim_sz_scale": 30774,
    "claim_rate_lambd": 74,
    "u": 10_000_000,
    "c": 2259838.120730937,
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
    zeros = [0]*config['time_steps']
    arrays.append(zeros)

    df = pd.DataFrame(arrays).T
    return df


def main():

    ### MAIN ###
    st.title('Modelo Cramer-Lundberg')
    st.subheader('Simulaciones')

    #u = 10_000_000.0
    chart = st.empty()
    chart.line_chart([10_000_000.0])

    ### SIDE BAR ###
    st.sidebar.title("Valores Iniciales")
    n_simulations = st.sidebar.slider('Número de simulaciones', 1,25,1)
    u = st.sidebar.number_input('Capital Inicial', min_value=0, value=10_000_000)
    c = st.sidebar.number_input('Primas Diarias', value=2259838)
    time_steps = st.sidebar.number_input('Días', value=1000, min_value=1,max_value=10000)
    
    config_sliders = {'u': u, 'c':c, 'time_steps':time_steps}
    
    ### BUTTON LOGIC ###
    if st.button('Simular'):
        # Loading Spinner
        with st.spinner('Simulando'):
            df = generate_simulations_data(n_simulations, config_sliders)

            chart.line_chart(df)

        st.success('Simulación terminada!')

    
if __name__ == "__main__":
    main()