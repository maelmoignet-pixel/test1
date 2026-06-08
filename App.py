import streamlit as st
import streamlit.components.v1 as components
import base64

st.title("test")

# --- INITIALISATION DE L'ÉTAT DE NAVIGATION ---
# On utilise le session_state pour suivre le dossier et le sous-dossier actifs
if "current_folder" not in st.session_state:
    st.session_state.current_folder = None
if "current_subfolder" not in st.session_state:
    st.session_state.current_subfolder = None

# --- FONCTIONS DE NAVIGATION ---
def go_to_folder(folder_name):
    st.session_state.current_folder = folder_name
    st.session_state.current_subfolder = None  # Réinitialise le sous-dossier si on change de thème

def go_to_subfolder(subfolder_name):
    st.session_state.current_subfolder = subfolder_name

def reset_navigation():
    st.session_state.current_folder = None
    st.session_state.current_subfolder = None

def back_to_folder():
    st.session_state.current_subfolder = None

#Lecture et affichage de pdf

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()

    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}#toolbar=0&navpanes=0&scrollbar=0"
            width="100%"
            height="800px"
            style="border: none;"
            type="application/pdf"
        ></iframe>
    """

    components.html(pdf_display, height=820, scrolling=False)

# FIL D'ARIANE (Pour savoir où l'on se trouve et revenir en arrière facilement)
if st.session_state.current_folder is not None:
    path = f"📂 **Accueil**"
    path += f"  >  📁 {st.session_state.current_folder}"
    if st.session_state.current_subfolder is not None:
        path += f"  >  📄 {st.session_state.current_subfolder}"
    st.markdown(path)
    st.write("---")


# NIVEAU 1 : Accueil (Liste des thèmes principaux)
if st.session_state.current_folder is None:
    st.subheader("Sélectionnez un thème :")
    
    # Bouton pour le premier répertoire
    if st.button("🔢 Suites numériques", use_container_width=True):
        go_to_folder("Suites numériques")
        st.rerun()
        
    # Vous pourrez ajouter d'autres dossiers ici
    if st.button("📈 Fonctions (Exemple)", use_container_width=True):
        go_to_folder("Fonctions")
        st.rerun()


# NIVEAU 2 : Dans un dossier principal (Sélection des sous-dossiers)
elif st.session_state.current_folder == "Suites numériques" and st.session_state.current_subfolder is None:
    st.subheader("Suites numériques : Choisissez un chapitre")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔗 Démonstration par récurrence", use_container_width=True):
            go_to_subfolder("Démonstration par récurrence")
            st.rerun()
    with col2:
        if st.button("🛑 Opérations sur les limites", use_container_width=True):
            go_to_subfolder("Opérations sur les limites")
            st.rerun()
            
    # Bouton Retour au menu principal
    st.write("---")
    if st.button("⬅️ Retour à l'accueil"):
        reset_navigation()
        st.rerun()


# NIVEAU 3 : Contenu du sous-dossier sélectionné
elif st.session_state.current_subfolder == "Démonstration par récurrence":
    st.subheader("Cours & Exercices : Démonstration par récurrence")
    st.write("Ici, insérez votre contenu, vos scripts Python ou vos exercices sur la récurrence.")
    display_pdf("cours_term_2025_Suites_cours_VP.pdf")
    # Bouton Retour au dossier "Suites"
    st.write("---")
    if st.button("⬅️ Retour aux sous-dossiers"):
        back_to_folder()
        st.rerun()


elif st.session_state.current_subfolder == "Opérations sur les limites":
    st.subheader("Cours & Exercices : Opérations sur les limites")
    st.write("Ici, insérez les tableaux de limites (somme, produit, quotient) et les formes indéterminées.")
    
    # Bouton Retour au dossier "Suites"
    st.write("---")
    if st.button("⬅️ Retour aux sous-dossiers"):
        back_to_folder()
        st.rerun()

# Gestion générique pour les autres dossiers non encore configurés
else:
    st.info(f"Le contenu pour '{st.session_state.current_folder}' est en cours de développement.")
    if st.button("⬅️ Retour à l'accueil"):
        reset_navigation()
        st.rerun()
        


