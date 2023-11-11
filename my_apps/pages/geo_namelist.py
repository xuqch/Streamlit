import streamlit as st
from st_pages import add_page_title, hide_pages
import time
import subprocess
import pandas as pd
import numpy as np

print('Create geo validation namelist -------------------')

add_page_title()

st.header("------------------------General-------------------------------\n")
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

st.divider()

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

col1, col2 = st.columns(2)
with col1:
    st.write(':blue[Radiation and Energy Cycle]')
    Albedo = st.checkbox('Albedo', value=False)
    Surface_Upward_SW_Radiation = st.checkbox('Surface Upward SW Radiation', value=False)
    Surface_Upward_LW_Radiation = st.checkbox('Surface Upward LW Radiation', value=False)
    Surface_Net_SW_Radiation = st.checkbox('Surface Net SW Radiation', value=False)
    Surface_Net_LW_Radiation = st.checkbox('Surface ppNet ppLW ppRadiation', value=False)
    Surface_Net_Radiation = st.checkbox('Surface ppNet ppRadiation', value=False)
    Ground_Heat_Flux = st.checkbox('Ground ppHeat ppFlux', value=False)
    Latent_Heat = st.checkbox('Latent ppHeat', value=False)
    Sensible_Heat = st.checkbox('Sensible ppHeat', value=False)

with col2:
    st.write(':blue[Forcings]')
    Diurnal_Temperature_Range = st.checkbox('Diurnal ppTemperature ppRange', value=False)
    Diurnal_Max_Temperature = st.checkbox('Diurnal ppMax ppTemperature', value=False)
    Diurnal_Min_Temperature = st.checkbox('Diurnal ppMin ppTemperature', value=False)
    Surface_Downward_SW_Radiation = st.checkbox('Surface ppDownward ppSW ppRadiation', value=False)
    Surface_Downward_LW_Radiation = st.checkbox('Surface ppDownward ppLW ppRadiation', value=False)
    Surface_Relative_Humidity = st.checkbox('Surface ppRelative ppHumidity', value=False)
    Precipitation = st.checkbox('Precipitation', value=False)
    Surface_Air_Temperature = st.checkbox('Surface ppAir ppTemperature', value=False)

options = {'Biomass': Biomass,
           'LAI': LAI,
           'BurnedArea':BurnedArea,
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

st.header("------------------------metrics-------------------------------\n")

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

st.header("Validation -----------------------------------------------------")
Ecosystem_arbon_Cycle_modules = [
    'Biomass',
    'LAI',
    'BurnedArea',
    'Global_Net_Ecosystem_Carbon_Balance',
    'Gross_Primary_Productivity',
    'Ecosystem_Respiration',
    'Soil_Carbon',
    'Nitrogen_Fixation'
]
Ecosystem_arbon_Cycle_options = []
for module in Ecosystem_arbon_Cycle_modules:
    if options[f'{module}'] == True:
        Ecosystem_arbon_Cycle_options.append(module)

Hydrology_Cycle_modules = [
    'Evapotranspiration',
    'Transpiration',
    'Interception',
    'Soil_Evaporation',
    'Soil_Moisture',
    'Runoff',
    'Inundation',
    'Latent_Heat',
    'Sensible_Heat',
    'Terrestrial_Water_Storage_Anomaly',
    'Snow_Water_Equivalent',
    'Permafrost'
]
Hydrology_Cycle_options = []
for module in Hydrology_Cycle_modules:
    if options[f'{module}'] == True:
        Hydrology_Cycle_options.append(module)

Radiation_Energy_Cycle_modules = [
    'Albedo',
    'Surface_Upward_SW_Radiation',
    'Surface_Upward_LW_Radiation',
    'Surface_Net_SW_Radiation',
    'Surface_Net_LW_Radiation',
    'Surface_Net_Radiation',
    'Ground_Heat_Flux'
]
Radiation_Energy_Cycle_options = []
for module in Radiation_Energy_Cycle_modules:
    if options[f'{module}'] == True:
        Radiation_Energy_Cycle_options.append(module)

Forcings_modules = [
    'Diurnal_Temperature_Range',
    'Diurnal_Max_Temperature',
    'Diurnal_Min_Temperature',
    'Surface_Downward_SW_Radiation',
    'Surface_Downward_LW_Radiation',
    'Surface_Relative_Humidity',
    'Precipitation',
    'Surface_Air_Temperature'
]
Forcings_options = []
for module in Forcings_modules:
    if options[f'{module}'] == True:
        Forcings_options.append(module)
print(Forcings_options)
# Ecosystem_arbon_Cycle_options = st.multiselect(
#     "",
#     Ecosystem_arbon_Cycle_modules,
#     placeholder="Select Ecosystem and Carbon Cycle Validation...",
# )


exit(0)
sim_df = pd.DataFrame(index=options,
                      columns=['Sim_Dir', 'Sim_TimRes', 'Sim_DataGroupby', 'Sim_Suffix',
                               'Sim_Prefix', 'Sim_GeoRes', 'Sim_Syear', 'Sim_Eyear']
                      )
sim_df.index.name = 'options'

edited_sim = st.data_editor(
    sim_df,
    column_config={
        "Sim_Dir": st.column_config.TextColumn(
            "Simulation Directory",
        ),
        "Sim_TimRes": st.column_config.SelectboxColumn(
            "Simulation Time Resolution",
            options=["Month", "Day"],
            required=True,
        ),
        "Sim_DataGroupby": st.column_config.SelectboxColumn(
            "Simulation DataGroupby",
            options=["Month", "Year"],
            required=True,
        ),
        "Sim_Suffix": st.column_config.TextColumn("Simulation Suffix", ),
        "Sim_Prefix": st.column_config.TextColumn("Simulation Prefix", default=""),
        "Sim_GeoRes": st.column_config.TextColumn("Simulation Geo Resolution", ),
        "Sim_Syear": st.column_config.NumberColumn("Simulation Start year",
                                                   min_value=100,
                                                   max_value=3000,
                                                   step=1,
                                                   format="%d", ),
        "Sim_Eyear": st.column_config.NumberColumn("Simulation End year",
                                                   min_value=100,
                                                   max_value=3000,
                                                   step=1,
                                                   format="%d", ),
    },
    disabled=["options"],
    hide_index=False,
)

obs_df = pd.DataFrame(index=options,
                      columns=['Obs_source', 'Obs_Dir', 'Obs_TimRes', 'Obs_GeoRes', 'Obs_DataGroupby',
                               'Obs_Suffix', 'Obs_Prefix', 'Obs_Syear', 'Obs_Eyear']
                      )

#
#  figplot         =  True
#  fldfrc          =  fldfrc

edited_obs = st.data_editor(
    obs_df,
    column_config={
        "Obs_source": st.column_config.TextColumn(
            "Observation Directory",
        ),
        "Obs_Dir": st.column_config.TextColumn(
            "Observation Directory",
        ),
        "Obs_TimRes": st.column_config.SelectboxColumn(
            "Observation Time Resolution",
            options=["Month", "Day"],
            required=True,
        ),
        "Obs_GeoRes": st.column_config.TextColumn("Observation Geo Resolution", ),
        "Obs_DataGroupby": st.column_config.SelectboxColumn(
            "Observation DataGroupby",
            options=["Month", "Year"],
            required=True,
        ),
        "Obs_Suffix": st.column_config.TextColumn("Observation Suffix", ),
        "Obs_Prefix": st.column_config.TextColumn("Observation Prefix", default=""),
        "Obs_Syear": st.column_config.NumberColumn("Observation Start year",
                                                   min_value=100,
                                                   max_value=3000,
                                                   step=1,
                                                   format="%d", ),
        "Obs_Eyear": st.column_config.NumberColumn("Observation End year",
                                                   min_value=100,
                                                   max_value=3000,
                                                   step=1,
                                                   format="%d", ),
    },
    disabled=["options"],
    hide_index=False,
)

fig_df = pd.DataFrame(index=options,
                      columns=['figplot', 'fldfrc']
                      )
edited_fig = st.data_editor(
    fig_df,
    column_config={
        "figplot": st.column_config.CheckboxColumn(
            "Observation Directory",
            help="Select whether plot your validation",
            default=True,
        ),
        "fldfrc": st.column_config.TextColumn(
            "fldfrc",
        ),
    },
    disabled=["options"],
    hide_index=False,
)
#
#  figplot         =  True
#  fldfrc          =  fldfrc

# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )
# edited_df = st.data_editor(
#     df,
#     column_config={
#         "command": "Streamlit Command",
#         "rating": st.column_config.NumberColumn(
#             "Your rating",
#             help="How much do you like this command (1-5)?",
#             min_value=1,
#             max_value=5,
#             step=1,
#             format="%d ⭐",
#         ),
#         "is_widget": "Widget ?",
#     },
#     disabled=["command", "is_widget"],
#     hide_index=True,
# )
#
# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
