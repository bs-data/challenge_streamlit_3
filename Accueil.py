import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}


authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

#  Utiliser la méthode login pour afficher le formulaire de connexion et vérifier les informations d'identification de l'utilisateur

authenticator.login()


def accueil():
      st.title("Bienvenue sur ma page")
      
      
if st.session_state["authentication_status"]:
    accueil()
    

elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')
         

with st.sidebar:
    if st.session_state["authentication_status"]:
        st.write("Bienvenue", lesDonneesDesComptes["usernames"]["root"]["name"])
        authenticator.logout("Déconnexion")
# Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
                    menu_title=None,
                    options = ["Accueil", "Les photos des animaux"]
                )
            
            
if st.session_state["authentication_status"]:
    if selection == "Accueil":
        st.image("https://cdn.pixabay.com/photo/2019/06/23/10/50/child-4293384_1280.jpg")           
    elif selection == "Les photos des animaux":
        st.write("Voici vos animaux préférés") 
#  mettre des colonnes côte à côte ex: 3 photos de chat
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Wahou un chat!")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("J'aime pas les chiens!")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("Sacrée Chouette!")
            st.image("https://static.streamlit.io/examples/owl.jpg")
    
    




