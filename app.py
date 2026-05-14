import plotly.express as px
import pandas as pd

# Charger les données
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# -----------------------------
# 1. VENTES PAR RÉGION (existant)
# -----------------------------
figure_region = px.pie(
    données,
    values='qte',
    names='region',
    title='Quantité vendue par région'
)

figure_region.write_html('ventes-par-region.html')

print('ventes-par-region.html généré avec succès !')

# -----------------------------
# 2. VENTES PAR PRODUIT
# -----------------------------

ventes_produit = données.groupby('produit')['qte'].sum().reset_index()

figure_produit = px.bar(
    ventes_produit,
    x='produit',
    y='qte',
    title='Ventes par produit',
    color='produit'
)

figure_produit.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')

# -----------------------------
# 3. CHIFFRE D'AFFAIRES PAR PRODUIT
# -----------------------------

# calcul du CA
données['chiffre_affaires'] = données['prix'] * données['qte']

ca_produit = données.groupby('produit')['chiffre_affaires'].sum().reset_index()

figure_ca = px.bar(
    ca_produit,
    x='produit',
    y='chiffre_affaires',
    title="Chiffre d'affaires par produit",
    color='produit'
)

figure_ca.write_html('ca-par-produit.html')

print("ca-par-produit.html généré avec succès !")
