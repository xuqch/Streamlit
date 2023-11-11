from geo_classification import initial_setting
import time
import subprocess
import pandas as pd
import numpy as np
import streamlit as st
from st_pages import add_page_title, hide_pages


def set_General(General):
    st.subheader('General setting ....')
    col1, col2, col3 = st.columns(3)
    with col1:
        General["casename"] = st.text_input('casename: ', placeholder="Set your casename...")
        General["casedir"] = st.text_input('casedir: ', placeholder="Set your case directory...")
        General["compare_Tres"] = st.text_input('compare Tres: ', placeholder="Set your casename...")
        General["compare_Gres"] = st.text_input('compare Gres: ', placeholder="Set your casename...")

    with col2:
        General["Max_lat"] = st.number_input("Max latitude: ", value=General["Max_lat"])
        General["Min_lat"] = st.number_input("Min latitude: ", value=General["Min_lat"])
        General["Max_lon"] = st.number_input("Max Logitude: ", value=General["Max_lon"])
        General["Min_lon"] = st.number_input("Min Logitude: ", value=General["Min_lon"])

    with col3:
        General["Syear"] = st.number_input("Syear: ", format='%04d', value=General["Syear"], step=int(1), placeholder="Start year...")
        General["Eyear"] = st.number_input("Eyear: ", format='%04d', value=General["Eyear"], step=int(1), placeholder="End year...")
        General["Min_year"] = st.number_input("Min year: ", value=General["Min_year"], placeholder="Min year...")
        General["num_cores"] = st.number_input("num cores: ", value=General["num_cores"],
                                               placeholder="how many core will be used in Parallel computing...", format='%d')
        st.write('How many core will be used in Parallel computing')


def set_metrics(metrics):
    st.subheader('Metrics setting ....')
    col1, col2, = st.columns(2)
    with col1:
        metrics["pc_bias"] = st.checkbox('Percent Bias', value=metrics[f"pc_bias"])
        metrics["apb"] = st.checkbox('Absolute Percent Bias', value=metrics["apb"])
        metrics["RMSE"] = st.checkbox('Root Mean Squared Error', value=metrics["RMSE"])
        metrics["ubRMSE"] = st.checkbox('Unbiased Root Mean Squared Error', value=metrics["ubRMSE"])

    with col2:
        metrics["mae"] = st.checkbox('Mean Absolute Error', value=metrics["mae"])
        metrics["bias"] = st.checkbox('Bias', value=metrics["bias"])
        metrics["L"] = st.checkbox('Likelihood', value=metrics["L"])
        metrics["correlation"] = st.checkbox('correlation coefficient', value=metrics["correlation"])

    col1, col2, = st.columns(2)
    with col1:
        metrics["correlation_R2"] = st.checkbox('correlation coefficient R2', value=metrics["correlation_R2"])
        metrics["NSE"] = st.checkbox('Nash Sutcliffe efficiency coefficient', value=metrics["NSE"])
        metrics["KGE"] = st.checkbox('Kling-Gupta Efficiency', value=metrics["KGE"])
        metrics["KGESS"] = st.checkbox('Normalized Kling-Gupta Efficiency', value=metrics["KGESS"])

    with col2:
        metrics["index_agreement"] = st.checkbox('Index of agreement', value=metrics["index_agreement"])
        metrics["kappa_coeff"] = st.checkbox('Kappa coefficient', value=metrics["kappa_coeff"])
        metrics["nBiasScore"] = st.checkbox('Bias Score from ILAMB', value=metrics["nBiasScore"])
        metrics["nRMSEScore"] = st.checkbox('RMSE Score from ILAMB', value=metrics["nRMSEScore"])


def set_Evaluation_Items(Evaluation_Items):
    st.subheader("Evaluation Items ....")
    col1, col2 = st.columns(2)
    with col1:
        st.write(':blue[Ecosystem and Carbon Cycle]')
        Evaluation_Items['Biomass'] = st.checkbox('Biomass', value=Evaluation_Items['Biomass'])
        Evaluation_Items['LAI'] = st.checkbox('LAI', value=Evaluation_Items['LAI'])
        Evaluation_Items['BurnedArea'] = st.checkbox('BurnedArea', value=Evaluation_Items['BurnedArea'])
        Evaluation_Items['Global_Net_Ecosystem_Carbon_Balance'] = st.checkbox('Global Net Ecosystem Carbon Balance',
                                                                              value=Evaluation_Items['Global_Net_Ecosystem_Carbon_Balance'])
        Evaluation_Items['Gross_Primary_Productivity'] = st.checkbox('Gross Primary Productivity',
                                                                     value=Evaluation_Items['Gross_Primary_Productivity'])
        Evaluation_Items['Ecosystem_Respiration'] = st.checkbox('Ecosystem Respiration', value=Evaluation_Items['Ecosystem_Respiration'])
        Evaluation_Items['Soil_Carbon'] = st.checkbox('Soil Carbon', value=Evaluation_Items['Soil_Carbon'])
        Evaluation_Items['Nitrogen_Fixation'] = st.checkbox('Nitrogen Fixation', value=Evaluation_Items['Nitrogen_Fixation'])

    # st.divider()

    with col2:
        st.write(':blue[Forcings]')
        Evaluation_Items['Diurnal_Temperature_Range'] = st.checkbox('Diurnal Temperature Range', value=Evaluation_Items['Diurnal_Temperature_Range'])
        Evaluation_Items['Diurnal_Max_Temperature'] = st.checkbox('Diurnal Max Temperature', value=Evaluation_Items['Diurnal_Max_Temperature'])
        Evaluation_Items['Diurnal_Min_Temperature'] = st.checkbox('Diurnal Min Temperature', value=Evaluation_Items['Diurnal_Min_Temperature'])
        Evaluation_Items['Surface_Downward_SW_Radiation'] = st.checkbox('Surface Downward SW Radiation',
                                                                        value=Evaluation_Items['Surface_Downward_SW_Radiation'])
        Evaluation_Items['Surface_Downward_LW_Radiation'] = st.checkbox('Surface Downward LW Radiation',
                                                                        value=Evaluation_Items['Surface_Downward_LW_Radiation'])
        Evaluation_Items['Surface_Relative_Humidity'] = st.checkbox('Surface Relative Humidity', value=Evaluation_Items['Surface_Relative_Humidity'])
        Evaluation_Items['Precipitation'] = st.checkbox('Precipitation', value=Evaluation_Items['Precipitation'])
        Evaluation_Items['Surface_Air_Temperature'] = st.checkbox('Surface Air Temperature', value=Evaluation_Items['Surface_Air_Temperature'])

    col1, col2 = st.columns(2)
    with col1:
        st.write(':blue[Radiation and Energy Cycle]')
        Evaluation_Items['Albedo'] = st.checkbox('Albedo', value=Evaluation_Items['Albedo'])
        Evaluation_Items['Surface_Upward_SW_Radiation'] = st.checkbox('Surface Upward SW Radiation',
                                                                      value=Evaluation_Items['Surface_Upward_SW_Radiation'])
        Evaluation_Items['Surface_Upward_LW_Radiation'] = st.checkbox('Surface Upward LW Radiation',
                                                                      value=Evaluation_Items['Surface_Upward_LW_Radiation'])
        Evaluation_Items['Surface_Net_SW_Radiation'] = st.checkbox('Surface Net SW Radiation', value=Evaluation_Items['Surface_Net_SW_Radiation'])
        Evaluation_Items['Surface_Net_LW_Radiation'] = st.checkbox('Surface Net LW Radiation', value=Evaluation_Items['Surface_Net_LW_Radiation'])
        Evaluation_Items['Surface_Net_Radiation'] = st.checkbox('Surface Net Radiation', value=Evaluation_Items['Surface_Net_Radiation'])
        Evaluation_Items['Ground_Heat_Flux'] = st.checkbox('Ground Heat Flux', value=Evaluation_Items['Ground_Heat_Flux'])
        Evaluation_Items['Latent_Heat'] = st.checkbox('Latent Heat', value=Evaluation_Items['Latent_Heat'])
        Evaluation_Items['Sensible_Heat'] = st.checkbox('Sensible Heat', value=Evaluation_Items['Sensible_Heat'])
    with col2:
        st.write(':blue[Hydrology Cycle]')
        Evaluation_Items['Evapotranspiration'] = st.checkbox('Evapotranspiration', value=Evaluation_Items['Evapotranspiration'])
        Evaluation_Items['Transpiration'] = st.checkbox('Transpiration', value=Evaluation_Items['Transpiration'])
        Evaluation_Items['Interception'] = st.checkbox('Interception', value=Evaluation_Items['Interception'])
        Evaluation_Items['Soil_Evaporation'] = st.checkbox('Soil Evaporation', value=Evaluation_Items['Soil_Evaporation'])
        Evaluation_Items['Soil_Moisture'] = st.checkbox('Soil Moisture', value=Evaluation_Items['Soil_Moisture'])
        Evaluation_Items['Runoff'] = st.checkbox('Runoff', value=Evaluation_Items['Runoff'])
        Evaluation_Items['Inundation'] = st.checkbox('Inundation', value=Evaluation_Items['Inundation'])
        Evaluation_Items['Terrestrial_Water_Storage_Anomaly'] = st.checkbox('Terrestrial Water Storage Anomaly',
                                                                            value=Evaluation_Items['Terrestrial_Water_Storage_Anomaly'])
        Evaluation_Items['Snow_Water_Equivalent'] = st.checkbox('Snow Water Equivalent', value=Evaluation_Items['Snow_Water_Equivalent'])
        Evaluation_Items['Permafrost'] = st.checkbox('Permafrost', value=Evaluation_Items['Permafrost'])


def set_expander(info, i):
    key_list = list(info.keys())
    with st.expander(f"{module}"):
        st.subheader('General setting ....')
        info["Obs_source"] = st.text_input(f'{i}. Obs_source: ', value=info[f"Obs_source"], placeholder=f"Set your Observation source...")
        info["Obs_Dir"] = st.text_input(f'{i}. Obs_Dir: ', value=info[f"Obs_Dir"], placeholder=f"Set your Observation Directory...")
        info["Obs_TimRes"] = st.selectbox(f'{i}. Obs_TimRes: ',
                                          options=('Hour', 'Day', 'Month', 'Year', 'Climatology'),
                                          index=None,
                                          placeholder=f"Set your Observation Time Resolution (default={info[f'Obs_TimRes']})...")
        info["Obs_GeoRes"] = st.text_input(f'{i}. Obs_GeoRes: ', value=info[f"Obs_GeoRes"], placeholder=f"Set your Observation Geo Resolution...")
        info["Obs_DataGroupby"] = st.selectbox(f'{i}. Obs_DataGroupby: ',
                                               options=('Hour', 'Day', 'Month', 'Year', 'Single'),
                                               index=None,
                                               placeholder=f"Set your Observation Time DataGroupby (default={info[f'Obs_DataGroupby']})...")
        info["Obs_Suffix"] = st.text_input(f'{i}. Obs_Suffix: ', value=info[f"Obs_Suffix"], placeholder=f"Set your Observation Suffix...")
        info["Obs_Prefix"] = st.text_input(f'{i}. Obs_Prefix: ', value=info[f"Obs_Prefix"], placeholder=f"Set your Observation Prefix...")
        info["Obs_Syear"] = st.number_input(f'{i}. Obs_Syear: ',
                                            value=int(info[f"Obs_Syear"]), min_value=100, max_value=3000, step=1, format="%d",
                                            placeholder="Set your Observation Start year...")
        info["Obs_Eyear"] = st.number_input(f'{i}. Obs_Eyear: ',
                                            value=int(info[f"Obs_Eyear"]), min_value=100, max_value=3000, step=1, format="%d",
                                            placeholder="Set your Observation End year...")
        st.divider()

        info["Sim_Dir"] = st.text_input(f'{i}. Sim_Dir: ', value=info[f"Sim_Dir"], placeholder=f"Set your Simulation Directory...")
        info["Sim_TimRes"] = st.selectbox(f'{i}. Sim_TimRes: ',
                                          options=('Hour', 'Day', 'Month', 'Year', 'Climatology'),
                                          index=None,
                                          placeholder=f"Set your Simulation Time Resolution (default={info[f'Sim_TimRes']})...")
        info["Sim_GeoRes"] = st.text_input(f'{i}. Sim_GeoRes: ', value=info[f"Sim_GeoRes"], placeholder=f"Set your Simulation Geo Resolution...")
        info["Sim_DataGroupby"] = st.selectbox(f'{i}. Sim_DataGroupby: ',
                                               options=('Hour', 'Day', 'Month', 'Year', 'Single'),
                                               index=None,
                                               placeholder=f"Set your Simulation Time DataGroupby (default={info[f'Sim_DataGroupby']})...")
        info["Sim_Suffix"] = st.text_input(f'{i}. Sim_Suffix: ', value=info[f"Sim_Suffix"], placeholder=f"Set your Simulation Suffix...")
        info["Sim_Prefix"] = st.text_input(f'{i}. Sim_Prefix: ', value=info[f"Sim_Prefix"], placeholder=f"Set your Simulation Prefix...")
        info["Sim_Syear"] = st.number_input(f'{i}. Sim_Syear: ',
                                            value=int(info[f"Sim_Syear"]), min_value=100, max_value=3000, step=1, format="%d",
                                            placeholder="Set your Simulation Start year...")
        info["Sim_Eyear"] = st.number_input(f'{i}. Sim_Eyear: ',
                                            value=int(info[f"Sim_Eyear"]), min_value=100, max_value=3000, step=1, format="%d",
                                            placeholder="Set your Simulation End year...")
        st.divider()
        info["figplot"] = st.checkbox(f'{i}. Figplot (Set ploting or not...) ', value=True)
        info[f"{key_list[-1]}"] = st.text_input(f'{i}. {key_list[-1]}: ', value=info[f"{key_list[-1]}"], placeholder=f"Set your {key_list[-1]}...")
    # return info


if __name__ == "__main__":
    print('Create geo validation namelist -------------------')

    add_page_title()
    initial_information = initial_setting()

    # st.header("------------------------General---------------------------\n")
    Generals = initial_information.Generals()
    set_General(Generals)
    st.divider()

    # st.header("------------------------metrics---------------------------\n")
    metrics = initial_information.metrics()
    set_metrics(metrics)
    st.divider()

    # st.header("------------------------Evaluation Items---------------------------\n")
    Evaluation_Items = initial_information.Evaluation_Items()
    set_Evaluation_Items(Evaluation_Items)
    st.divider()

    st.subheader("Add Validation info...")
    modules = initial_information.modules()
    information = initial_information.initial_information()
    module_info = {}
    i = 1
    for module in modules:
        if Evaluation_Items[f"{module}"]:
            set_expander(information[f"{module}_LIST"], i)
            # module_info[f"{module}_LIST"] = set_expander(information[f"{module}_LIST"], i)
            i = i + 1
    st.divider()

    namelist_path = st.text_input('namelist path: ', './nml/', placeholder="Set your namelist path...")
    if st.button('Run', type="primary"):
        with st.spinner("Now initial..."):
            subprocess.run('echo success', shell=True)
            time.sleep(3)
        st.success("Done!")

    exit(0)
