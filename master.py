from cldx import CausalLoopDiagram
import streamlit as st
import pandas as pd
import io
import networkx as nx
import pygraphviz as pgv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import FancyArrow, Arc

st.title('Causal loop diagrammer')
st.sidebar.title("Add causality - WIP")
source = st.sidebar.text_input('Source')
target = st.sidebar.text_input('Target')
polarity = st.sidebar.text_input('Polarity')

st.sidebar.button("Add to the data table")
#st.sidebar.title('Sidebar')

data = pd.read_excel('taulukko.xlsx')

with st.beta_expander('Show data'):
    data

cld = CausalLoopDiagram()


#parsitaan arvot dataframesta
df = pd.read_excel("taulukko.xlsx")
mylist = list(map(tuple, df.to_numpy()))
with st.beta_expander('Show mylist'):
    mylist

cld.add_causal_links(mylist)
cld.draw(filename='pussa.png')
st.image("pussa.png")


lista = cld.find_loops()
with st.beta_expander("Show the loops"):
    st.write(lista)

with st.beta_expander("Loop analysis"):
    #st.write(type(lista))
    df = pd.DataFrame(lista)
    df

