import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='')

st.header('CV-JAVIER HORACIO PÉREZ RICÁRDEZ')
#st.subheader('Nombre: JAVIER HORACIO PÉREZ RICÁRDEZ')
st.subheader('Estudios:')
st.subheader('Lic. en Matemáticas')
st.subheader('Maestría en Ciencias de la Computación')
st.subheader('Experiencia Laboral:')
st.subheader('Programador (Lenguajes): python, sql, VB, etc') 
st.subheader('manejo de bases de datos desde python, Excel desde python con visualizacion de datos y gráficos, creación de interfaces gráficas de usuarios; para insertar, actualizar, eliminar, desde python a Oracle y Excel')#', 49 años de edad, estudios de Lic. en matemáticas y Maestría en Ciencias de la Computación.')
st.subheader('Y mucho más: proyectos avanzados de programación') 

st.subheader('') 
st.subheader('') 
st.subheader('Dejo un ejemplo basico creado en python y utilizando Heroku') 
st.subheader('email: jahoperi@gmail.com') 

st.subheader('') 
st.subheader('') 
st.subheader('') 
st.subheader('') 

st.subheader('Puedes mover la barra que indica la edad de 23 a 33 años, puedes eliminar las ocupaciones; Matemático, Computólogo, Eléctrico y Mecánico; e ir observando como varía la gráfica de barras. Y puedes recuperar las ocupaciones eliminadas, haciendo clic en la flechita hacia abajo. Puedes pasar el ratón por encima de las barras')

st.subheader('') 
st.subheader('') 
st.subheader('En la gráfica circular, puedes igual pasar el ratón por encima. Puedes eliminar una porción, haciendo clic en las ocupaciones marcadas con cuadritos de colores y recuperar esas porciones dando nuevamente clic') 

#st.header('Survey Results 2021')
#st.subheader('Was the tutorial helpful?')

### --- LOAD DATAFRAME
excel_file = 'datos.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)
df_participants.dropna(inplace=True)

# --- STREAMLIT SELECTION
department = df['Ocupación'].unique().tolist()
ages = df['Edad'].unique().tolist()

age_selection = st.slider('Edad:',
                        min_value= min(ages),
                        max_value= max(ages),
                        value=(min(ages),max(ages)))

department_selection = st.multiselect('Ocupación:',
                                    department,
                                    default=department)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Edad'].between(*age_selection)) & (df['Ocupación'].isin(department_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Resultados disponibles: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Compañías']).count()[['Edad']]
df_grouped = df_grouped.rename(columns={'Edad': 'Frecuencia'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Compañías',
                   y='Frecuencia',
                   text='Frecuencia',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- DISPLAY IMAGE & DATAFRAME
col1, col2 = st.columns(2)
image = Image.open('python1.jpg')
print(image)
col1.image(image,
        caption='',
        use_column_width=True)
col2.dataframe(df[mask])

# --- PLOT PIE CHART
pie_chart = px.pie(df_participants,
                title='% del Total de Ocupación',
                values='Frecuencia',
                names='Profesión')

st.plotly_chart(pie_chart)

 

