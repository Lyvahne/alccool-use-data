import streamlit as st
import pandas as pd
import plotly as px
#import plotly.express as px
import altair as alt
from datetime import datetime, timedelta
import numpy as np



st.title("La consommation de spiritueux, vins et bières par pays, de 1890 à 2014.")



alcool = pd.read_csv('alcool-type.csv')




#Selectionner date
#'''df = pd.DataFrame([['1890-01-01'], ['2014-12-31']], columns=['Year'])
#df['Year'] = pd.to_datetime(df['Year'])

#start_range = df['Year'][0].to_pydatetime()
#end_range = df['Year'][1].to_pydatetime()

#date_range = st.slider(
    #'Date',
    #min_value = start_range,
    #value=(start_range, end_range),
    #max_value = end_range,
  #format = 'YYYY')

#start_date, end_date = date_range
#st.write(start_date, end_date)'''

# Jeu découverte
st.subheader("Où si situaient les plus grands consommateurs d'alcools ? ⬇️")


pays = st.sidebar.multiselect(
    label = "Filtrer les résultats par pays",
    options = alcool['Entity'].unique(),
    default =['United States', 'United Kingdom', 'Switzerland', 'Sweden', 'Norway', 'New Zealand', 'Netherlands', 'Japan', 'Italy', 'France', 'Finland', 'Denmark', 'Canada', 'Belgium', 'Austria', 'Australia']
)
#Consommation de bières par pays
beer_par_pays= alcool[['Entity', 'Beer ']].groupby(['Entity']) \
                      .agg('sum') \
                      .sort_values(by='Entity', ascending=False)
beer_par_pays.reset_index(inplace=True)

beer_par_pays = beer_par_pays.query('Entity in @pays')

couleurs_jaune = ['#F7C623', '#E0A52B', '#F79923', '#ED7521']


fig2 = px.bar(beer_par_pays, \
             x='Entity', \
             y='Beer ', \
             text='Beer ', \
             color='Beer ', \
             color_discrete_sequence=couleurs_jaune)

#Consommation de vins par pays
wine_par_pays= alcool[['Entity', 'Wine ']].groupby(['Entity']) \
                      .agg('sum') \
                      .sort_values(by='Entity', ascending=False)
wine_par_pays.reset_index(inplace=True)

wine_par_pays = wine_par_pays.query('Entity in @pays')

couleurs_orange = ['#EB722F', '#DF4438', '#F53166', '#EB2FC0']

fig3 = px.bar(wine_par_pays, \
             x='Entity', \
             y='Wine ', \
             text='Wine ', \
             color='Wine ', \
             color_discrete_sequence=couleurs_orange)

#Graphiques à barres - Consommation alcool par pays et par type
option1 = st.selectbox(
    'Selon vous, quel pays à été le plus grand consommateur de spiriteux ?',
     ('Etats-Unis', 'Royaume-Uni', 'Suisse', 'Suède', 'Norvège', 'Nouvelle-Zélande', 'Pays-Bas', 'Japon', 'Italie', 'France', 'Finlande', 'Danemark', 'Canada', 'Belgique', 'Autriche', 'Australie'))

st.write('Vous avez choisi : ', option1)

#button = st.button('Cliquer ici')

if option1 == 'Japon':
    st.balloons()

#Consommation de spiritueux par pays

spirit_par_pays= alcool[['Entity', 'Spirits ']].groupby(['Entity']) \
                      .agg('sum') \
                      .sort_values(by='Entity', ascending=False)
spirit_par_pays.reset_index(inplace=True)

spirit_par_pays = spirit_par_pays.query('Entity in @pays')

couleurs_rouge = ['#ED58CA', '#AA5DE0', '#8C5CF7', '#5D58ED']

fig = px.bar(spirit_par_pays, \
             x='Entity', \
             y='Spirits ', \
             text='Spirits ', \
             color='Spirits ', \
             color_discrete_sequence=couleurs_rouge)


with st.expander("👀 Voir les chiffres - Spiritueux 🥃"):
    st.subheader("Consommation de spiritueux par pays")
    st.plotly_chart(fig, use_container_width=True)
    st.write('Le **Japon** suivi des **Pays-Bas** ont été les plus grands consommateurs de spiritueux. _*Pourcentage calculé : consommation totale de spiritueux par pays/consommation de spiritueux globale_')

option2 = st.selectbox(
    'Selon vous, quel pays à été le plus grand consommateur de bières ?',
     ('Etats-Unis', 'Royaume-Uni', 'Suisse', 'Suède', 'Norvège', 'Nouvelle-Zélande', 'Pays-Bas', 'Japon', 'Italie', 'France', 'Finlande', 'Danemark', 'Canada', 'Belgique', 'Autriche', 'Australie'))

st.write('Vous avez choisi : ', option2)

if option2 =='Royaume-Uni':
    st.balloons()

with st.expander("👀 Voir les chiffres - Bières 🍺"):
    st.subheader("Consommation de bières par pays")
    st.plotly_chart(fig2, use_container_width=True)
    st.write('Le **Royaume-Uni** suivi de la **Belgique** ont été les plus grands consommateurs de bières. _*Pourcentage calculé : consommation totale de bières par pays/consommation de bières globale_')

option3 = st.selectbox(
    'Selon vous, quel pays à été le plus grand consommateur de vins ?',
     ('Etats-Unis', 'Royaume-Uni', 'Suisse', 'Suède', 'Norvège', 'Nouvelle-Zélande', 'Pays-Bas', 'Japon', 'Italie', 'France', 'Finlande', 'Danemark', 'Canada', 'Belgique', 'Autriche', 'Australie'))

st.write('Vous avez choisi : ', option3)

if option3 =='Italie':
    st.balloons()

with st.expander("👀 Voir la réponse - Vins 🍷"):
    st.subheader("Consommation de vins par pays")
    st.plotly_chart(fig3, use_container_width=True)
    st.write("L'**Italie** suivie de la **France** ont été les plus grands consommateurs de vins. _*Pourcentage calculé : consommation totale de vins par pays/consommation de vins globale_")

#Consommation moyenne d'alcool par type
mean1 = alcool['Spirits '].mean()
print(mean1)
mean2 = alcool['Beer '].mean()
print(mean2)
mean3 = alcool['Wine '].mean()
print(mean3)

st.subheader("Consommation moyenne d'alcool par type (%)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Spiritueux 🥃", value=(round(mean1,2)))
    toggle_block1 = st.expander("Plus d'infos")
    with toggle_block1:
        st.write('La consommation moyenne de spiritueux était de **28,53%**. _Tous pays confondus, de 1820 à 2014_')

with col2:
    st.metric(label="Bières 🍺", value=(round(mean2,2)))
    toggle_block2 = st.expander("Plus d'infos")
    with toggle_block2:
        st.write('La consommation moyenne de bières était de **41,95%**. _Tous pays confondus, de 1820 à 2014_')

with col3:
    st.metric(label="Vins 🍷", value=(round(mean3,2)))
    toggle_block3 = st.expander("Plus d'infos")
    with toggle_block3:
        st.write('La consommation moyenne de vins était de **28,15%**. _Tous pays confondus, de 1820 à 2014_')

st.info("ℹ️ Avec une consommation moyenne de **41,95%**, la bière était l'alcool le plus consommé au monde de 1820 à 2014.")

#Visualisation consommation par pays 

st.subheader("Consommation de spiritueux par pays et années (1890 - 2014)")


fig4 = px.choropleth(alcool, 
             locations ="Code", 
             color ="Spirits ",
             hover_name ="Code", 
             scope ="world", 
             animation_frame ="Year")   
             #scolor_discrete_sequence=couleurs_rouge)

st.plotly_chart(fig4, use_container_width=True)




st.subheader("Consommation de bières par pays et années (1890 - 2014)")


fig8 = px.choropleth(alcool, 
             locations ="Code", 
             color ="Beer ",
             hover_name ="Code", 
             scope ="world", 
             animation_frame ="Year")   
             #scolor_discrete_sequence=couleurs_rouge)

st.plotly_chart(fig8, use_container_width=True)

st.subheader("Consommation de vins par pays et années (1890 - 2014)")


fig9 = px.choropleth(alcool, 
             locations ="Code", 
             color ="Wine ",
             hover_name ="Code", 
             scope ="world", 
             animation_frame ="Year")   
             #scolor_discrete_sequence=couleurs_rouge)

st.plotly_chart(fig9, use_container_width=True)

toggle_block4 = st.expander("En savoir plus")

with toggle_block4:
        st.write("En **1929**, on observe une chutte de consommation d'alcool. Aux Etats-Unis, on constate que la consommation d'alcool passe à **0%** l'année de la crise de 1929, marquant le début de la **grande dépression**. ")
        
#Vu sur la consommation dans le temps
st.subheader("Evolution des consommations des 3 types d'alcools dans le temps")
import plotly.graph_objects as go
from plotly.validators.scatter.marker import SymbolValidator
import plotly.io as pio

#Prévention sur les limites de la datavisualisation
st.warning("⚠️  Il n'y a pas de données sur toutes les années de 1890 à 2014.")

code_pays = st.sidebar.multiselect(
    label = "Voir l'évolution des consommation d'un pays",
    options = alcool['Code'].unique(),
    default =['AUS', 'AUT', 'BEL', 'CAN', 'FIN', 'DNK', 'FRA', 'ITA', 'JPN', 'NLD', 'NZL', 'NOR', 'SWE', 'CHE', 'GBR', 'USA']
)

#Focus spiritueux
spiritueux_par_pays_an = alcool[['Code', 'Spirits ', 'Year']].groupby(by=['Code', 'Spirits ']).max()
                      #.agg('max') \
                      #.sort_values(by='Spirits ', ascending=False)
spiritueux_par_pays_an.reset_index(inplace=True)

spiritueux_par_pays_an = spiritueux_par_pays_an.query('Code in @code_pays')

fig5 = px.scatter(
    spiritueux_par_pays_an,
    x='Code',
    y='Year',
    size="Spirits ",
    color="Code",
    title = "Consommation de spiritueux par pays et par ans",
    symbol='Code',
    symbol_sequence=['circle-open', 'x-open', 'square-open', 'triangle-up-open', 'star-open', 'pentagon-open', 'star-square-open', 'star-diamond-open', 'diamond-tall-open', 'diamond-wide-open', 'hourglass-open', 'bowtie-open', 'asterisk-open', 'circle-x-open', 'square-x-open', 'diamond-open']
)
fig5.update_layout(template = 'ggplot2')
st.plotly_chart(fig5, use_container_width=True)

st.info("ℹ️  Mise à part au **Japon**, la consommation de spiritueux à diminué dans le temps dans tous les pays.")

#Focus bière
biere_par_pays_an = alcool[['Code', 'Beer ', 'Year']].groupby(by=['Code', 'Beer ']).max()
                      #.agg('max') \
                      #.sort_values(by='Spirits ', ascending=False)
biere_par_pays_an.reset_index(inplace=True)

biere_par_pays_an = biere_par_pays_an.query('Code in @code_pays')

fig6 = px.scatter(
    biere_par_pays_an,
    x='Code',
    y='Year',
    size="Beer ",
    color="Code",
    title = "Consommation de bières par pays et par ans",
    symbol='Code',
    symbol_sequence=['circle-open', 'x-open', 'square-open', 'triangle-up-open', 'star-open', 'pentagon-open', 'star-square-open', 'star-diamond-open', 'diamond-tall-open', 'diamond-wide-open', 'hourglass-open', 'bowtie-open', 'asterisk-open', 'circle-x-open', 'square-x-open', 'diamond-open']
)
fig6.update_layout(template = 'gridon')
st.plotly_chart(fig6, use_container_width=True)
st.info("ℹ️  On observe en **Italy** et en **France**, un augmentation de consommation de bières dans le temps. Malgré quelques variances, les autres pays restent de bons consommateurs de bières dans le temps.")

#Focus vins
vins_par_pays_an = alcool[['Code', 'Wine ', 'Year']].groupby(by=['Code', 'Wine ']).max()
                      #.agg('max') \
                      #.sort_values(by='Spirits ', ascending=False)
vins_par_pays_an.reset_index(inplace=True)

vins_par_pays_an = vins_par_pays_an.query('Code in @code_pays')

fig7 = px.scatter(
    vins_par_pays_an,
    x='Code',
    y='Year',
    size="Wine ",
    color="Code",
    title = "Consommation de vins par pays et par ans",
    symbol='Code',
    symbol_sequence=['circle-open', 'x-open', 'square-open', 'triangle-up-open', 'star-open', 'pentagon-open', 'star-square-open', 'star-diamond-open', 'diamond-tall-open', 'diamond-wide-open', 'hourglass-open', 'bowtie-open', 'asterisk-open', 'circle-x-open', 'square-x-open', 'diamond-open']
)
fig7.update_layout(template = 'seaborn')
st.plotly_chart(fig7, use_container_width=True)
st.info("ℹ️  La **France** est le plus grand consommateur de vins sur le long terme. On observe une augmentation de consommation du vin au fil du temps.")



#st.plotly_chart(fig)



# last 30 days and exclude regional aggregations

#st.subheader("Consommation de spiritueux par pays")
#spirit_par_pays= alcool[['Entity', 'Spirits ']].groupby(['Entity']) \
                      #.agg('sum') \
                      #.sort_values(by='Entity', ascending=False)
#spirit_par_pays.reset_index(inplace=True)
#couleurs_rouge = ['#ED58CA', '#AA5DE0', '#8C5CF7', '#5D58ED']

#fig = px.bar(spirit_par_pays, \
             #x='Entity', \
             #y='Spirits ', \
             #text='Spirits ', \
             #color='Spirits ', \
             #color_discrete_sequence=couleurs_rouge)

#st.plotly_chart(fig)





