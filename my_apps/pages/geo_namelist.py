from geo_classification import initial_setting
import time
import subprocess
import pandas as pd
import numpy as np
import streamlit as st
from st_pages import add_page_title, hide_pages


def set_expander(info, i):
    with st.expander(f"{module}"):
        st.subheader('General setting ....')
        for key in info:
            info[f"{key}"] = st.text_input(f'{i}. {key}: ', value=info[f"{key}"], placeholder=f"Set your {key}...")

    # key_list = list(options.keys())
    # print(options[f'{key_list[-1]}'])
    return info


if __name__ == "__main__":
    print('Create geo validation namelist -------------------')

    add_page_title()
    initial_information = initial_setting()

    # st.header("------------------------General---------------------------\n")
    st.subheader('General setting ....')
    col1, col2, col3 = st.columns(3)
    with col1:
        casename = st.text_input('casename: ', placeholder="Set your casename...")
        casedir = st.text_input('casedir: ', placeholder="Set your case directory...")
        compare_Tres = st.text_input('compare Tres: ', placeholder="Set your casename...")
        compare_Gres = st.text_input('compare Gres: ', placeholder="Set your casename...")

    with col2:
        Max_lat = st.number_input("Max latitude: ", value=90.0)
        Min_lat = st.number_input("Min latitude: ", value=-90.0)
        Max_lon = st.number_input("Max Logitude: ", value=180.0)
        Min_lon = st.number_input("Min Logitude: ", value=-180.0)

    with col3:
        Syear = st.number_input("Syear: ", format='%04d', value=int(2000), step=int(1), placeholder="Start year...")
        Eyear = st.number_input("Eyear: ", format='%04d', step=int(1), value=int(2005), placeholder="End year...")
        Min_year = st.number_input("Min year: ", value=1.0, placeholder="Min year...")
        num_cores = st.number_input("num cores: ", placeholder="how many core will be used in Parallel computing...", format='%d', value=int(10))
        st.write('How many core will be used in Parallel computing')

    st.divider()
    # st.header("------------------------metrics---------------------------\n")
    st.subheader('Metrics setting ....')
    col1, col2, = st.columns(2)
    with col1:
        pc_bias = st.checkbox('Percent Bias', value=False)
        apb = st.checkbox('Absolute Percent Bias', value=False)
        RMSE = st.checkbox('Root Mean Squared Error', value=False)
        ubRMSE = st.checkbox('Unbiased Root Mean Squared Error', value=False)

    with col2:
        mae = st.checkbox('Mean Absolute Error', value=False)
        bias = st.checkbox('Bias', value=False)
        L = st.checkbox('Likelihood', value=False)
        correlation = st.checkbox('correlation coefficient', value=False)

    col1, col2, = st.columns(2)
    with col1:
        correlation_R2 = st.checkbox('correlation coefficient R2', value=False)
        NSE = st.checkbox('Nash Sutcliffe efficiency coefficient', value=False)
        KGE = st.checkbox('Kling-Gupta Efficiency', value=True)
        KGESS = st.checkbox('Normalized Kling-Gupta Efficiency', value=False)

    with col2:
        index_agreement = st.checkbox('Index of agreement', value=False)
        kappa_coeff = st.checkbox('Kappa coefficient', value=False)
        nBiasScore = st.checkbox('Bias Score from ILAMB', value=False)
        nRMSEScore = st.checkbox('RMSE Score from ILAMB', value=False)

    st.divider()
    st.subheader("Evaluation Items ....")
    col1, col2 = st.columns(2)
    with col1:
        st.write(':blue[Ecosystem and Carbon Cycle]')
        Biomass = st.checkbox('Biomass', value=False)
        LAI = st.checkbox('LAI', value=False)
        BurnedArea = st.checkbox('BurnedArea', value=False)
        Global_Net_Ecosystem_Carbon_Balance = st.checkbox('Global Net Ecosystem Carbon Balance', value=False)
        Gross_Primary_Productivity = st.checkbox('Gross Primary Productivity', value=False)
        Ecosystem_Respiration = st.checkbox('Ecosystem Respiration', value=False)
        Soil_Carbon = st.checkbox('Soil Carbon', value=False)
        Nitrogen_Fixation = st.checkbox('Nitrogen Fixation', value=False)

    # st.divider()


    with col2:
        st.write(':blue[Forcings]')
        Diurnal_Temperature_Range = st.checkbox('Diurnal Temperature Range', value=False)
        Diurnal_Max_Temperature = st.checkbox('Diurnal Max Temperature', value=False)
        Diurnal_Min_Temperature = st.checkbox('Diurnal Min Temperature', value=False)
        Surface_Downward_SW_Radiation = st.checkbox('Surface Downward SW Radiation', value=False)
        Surface_Downward_LW_Radiation = st.checkbox('Surface Downward LW Radiation', value=False)
        Surface_Relative_Humidity = st.checkbox('Surface Relative Humidity', value=False)
        Precipitation = st.checkbox('Precipitation', value=False)
        Surface_Air_Temperature = st.checkbox('Surface Air Temperature', value=False)


    col1, col2 = st.columns(2)
    with col1:
        st.write(':blue[Radiation and Energy Cycle]')
        Albedo = st.checkbox('Albedo', value=False)
        Surface_Upward_SW_Radiation = st.checkbox('Surface Upward SW Radiation', value=False)
        Surface_Upward_LW_Radiation = st.checkbox('Surface Upward LW Radiation', value=False)
        Surface_Net_SW_Radiation = st.checkbox('Surface Net SW Radiation', value=False)
        Surface_Net_LW_Radiation = st.checkbox('Surface Net LW Radiation', value=False)
        Surface_Net_Radiation = st.checkbox('Surface Net Radiation', value=False)
        Ground_Heat_Flux = st.checkbox('Ground Heat Flux', value=False)
        Latent_Heat = st.checkbox('Latent Heat', value=False)
        Sensible_Heat = st.checkbox('Sensible Heat', value=False)
    with col2:
        st.write(':blue[Hydrology Cycle]')
        Evapotranspiration = st.checkbox('Evapotranspiration', value=False)
        Transpiration = st.checkbox('Transpiration', value=False)
        Interception = st.checkbox('Interception', value=False)
        Soil_Evaporation = st.checkbox('Soil Evaporation', value=False)
        Soil_Moisture = st.checkbox('Soil Moisture', value=False)
        Runoff = st.checkbox('Runoff', value=False)
        Inundation = st.checkbox('Inundation', value=False)
        Terrestrial_Water_Storage_Anomaly = st.checkbox('Terrestrial Water Storage Anomaly', value=False)
        Snow_Water_Equivalent = st.checkbox('Snow Water Equivalent', value=False)
        Permafrost = st.checkbox('Permafrost', value=False)


    options = {'Biomass': Biomass,
               'LAI': LAI,
               'BurnedArea': BurnedArea,
               'Global_Net_Ecosystem_Carbon_Balance': Global_Net_Ecosystem_Carbon_Balance,
               'Gross_Primary_Productivity': Gross_Primary_Productivity,
               'Ecosystem_Respiration': Ecosystem_Respiration,
               'Soil_Carbon': Soil_Carbon,
               'Nitrogen_Fixation': Nitrogen_Fixation,

               'Evapotranspiration': Evapotranspiration,
               'Transpiration': Transpiration,
               'Interception': Interception,
               'Soil_Evaporation': Soil_Evaporation,
               'Soil_Moisture': Soil_Moisture,
               'Runoff': Runoff,
               'Inundation': Inundation,
               'Terrestrial_Water_Storage_Anomaly': Terrestrial_Water_Storage_Anomaly,
               'Snow_Water_Equivalent': Snow_Water_Equivalent,
               'Permafrost': Permafrost,

               'Albedo': Albedo,
               'Surface_Upward_SW_Radiation': Surface_Upward_SW_Radiation,
               'Surface_Upward_LW_Radiation': Surface_Upward_LW_Radiation,
               'Surface_Net_SW_Radiation': Surface_Net_SW_Radiation,
               'Surface_Net_LW_Radiation': Surface_Net_LW_Radiation,
               'Surface_Net_Radiation': Surface_Net_Radiation,
               'Ground_Heat_Flux': Ground_Heat_Flux,
               'Latent_Heat': Latent_Heat,
               'Sensible_Heat': Sensible_Heat,

               'Diurnal_Temperature_Range': Diurnal_Temperature_Range,
               'Diurnal_Max_Temperature': Diurnal_Max_Temperature,
               'Diurnal_Min_Temperature': Diurnal_Min_Temperature,
               'Surface_Downward_SW_Radiation': Surface_Downward_SW_Radiation,
               'Surface_Downward_LW_Radiation': Surface_Downward_LW_Radiation,
               'Surface_Relative_Humidity': Surface_Relative_Humidity,
               'Precipitation': Precipitation,
               'Surface_Air_Temperature': Surface_Air_Temperature}


    st.subheader("Add Validation info...")

    modules = initial_information.modules()
    information = initial_information.initial_information()
    module_info = {}
    i = 1
    for module in modules:
        if options[f"{module}"] == True:
            module_info[f"{module}_LIST"] = set_expander(information[f"{module}_LIST"], i)
            i = i + 1

    st.divider()
    if st.button('Run', type="primary"):
        with st.spinner("Now initial..."):
            subprocess.run('echo "success"', shell=True)
            time.sleep(3)
        st.success("Done!")


    exit(0)
