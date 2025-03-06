import streamlit as st

# Page Config
st.set_page_config(page_title="Eyyüb Güven - Portfolio", page_icon="🧠", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #2C3E50; }
        .subtitle { font-size: 20px; font-weight: bold; color: #1ABC9C; }
        .stButton>button { background-color: #1ABC9C; color: white; border-radius: 12px; }
        .stButton>button:hover { background-color: #16A085; }
        .sidebar .block-container { padding-top: 20px; }
        
        /* Sidebar Navigation Styling */
        .nav-button {
            width: 100%;
            padding: 10px 15px;
            margin: 5px 0;
            border: none;
            border-radius: 5px;
            background-color: #f0f2f6;
            color: #2C3E50;
            text-align: left;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        .nav-button:hover {
            background-color: #1ABC9C;
            color: white;
        }
        
        .nav-button.active {
            background-color: #1ABC9C;
            color: white;
        }
        
        div[data-testid="stSidebarNav"] {
            background-color: transparent;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar - Language Selector
language_options = {"🇬🇧 English": "en", "🇹🇷 Türkçe": "tr"}
selected_language = st.sidebar.selectbox("🌍 Dil / Language", list(language_options.keys()))

# Translations
translations = {
    "tr": {
        "home": "🏠 Ana Sayfa",
        "blog": "✍️ Blog",
        "about": "👤 Hakkımda",
        "skills": "🚀 Yetenekler & Projeler",
        "services": "🎯 Hizmetler",
        "contact": "📬 İletişim",
        "welcome": "Hoş Geldiniz!",
        "intro": "Ben **Eyyüb Güven** - Bilişsel Sinirbilimci ve Yapay Zeka Meraklısı.",
        "blog_header": "✍️ Blog Yazıları",
        "about_header": "👤 Hakkımda",
        "skills_header": "🚀 Yetenekler & Projeler",
        "services_header": "🎯 Hizmetler",
        "contact_header": "📬 İletişim",
        "contact_text": "Benimle iletişime geçin ve iş birliği yapalım!",
        "send": "Gönder",
        "professional_summary": """Nörobilim, yapay zeka ve beyin-bilgisayar arayüzleri alanında deneyimli bir bilişsel sinirbilimci ve psikolog. 
        fMRI nörogörüntüleme teknikleri, EEG ve fNRIS analizi, programlama ve non-invaziv beyin stimülasyonu konularında uzman.""",
        "education": "Eğitim",
        "experience": "Deneyim",
        "skills": "Teknik Beceriler",
        "certifications": "Sertifikalar",
        "contact_email": "eyyub.gvn@gmail.com"
    },
    "en": {
        "home": "🏠 Home",
        "blog": "✍️ Blog",
        "about": "👤 About Me",
        "skills": "🚀 Skills & Projects",
        "services": "🎯 Services",
        "contact": "📬 Contact",
        "welcome": "Welcome!",
        "intro": "I'm **Eyyüb Güven** - a Cognitive Neuroscientist and AI Enthusiast.",
        "blog_header": "✍️ Blog Posts",
        "about_header": "👤 About Me",
        "skills_header": "🚀 Skills & Projects",
        "services_header": "🎯 Services",
        "contact_header": "📬 Contact",
        "contact_text": "Let’s collaborate and get in touch!",
        "send": "Send",
        "professional_summary": """Dedicated cognitive neuroscientist and psychologist with multidisciplinary experience in neuroimaging, 
        computational neuroscience, deep learning, and brain-computer interfaces (BCIs).""",
        "education": "Education",
        "experience": "Experience",
        "skills": "Technical Skills",
        "certifications": "Certifications",
        "contact_email": "eyyub.gvn@gmail.com"
    }
}

# Get selected language code
lang = language_options[selected_language]

# Initialize session state for selected tab if not exists
if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = translations[lang]["home"]

# Sidebar - Navigation Menu
st.sidebar.image("assets/picture.jpg", width=200)
st.sidebar.header("🔹 Menü")
tabs = {
    translations[lang]["home"]: "home",
    translations[lang]["blog"]: "blog",
    translations[lang]["about"]: "about",
    translations[lang]["skills"]: "skills",
    translations[lang]["services"]: "services",
    translations[lang]["contact"]: "contact"
}

# Navigation buttons using Streamlit buttons
for tab in tabs.keys():
    # Create a unique key for each button
    button_key = f"nav_button_{tabs[tab]}"
    
    # Style the button based on current selection
    is_active = st.session_state.selected_tab == tab
    button_style = "primary" if is_active else "secondary"
    
    # Create the button and handle click
    if st.sidebar.button(tab, key=button_key, type=button_style):
        st.session_state.selected_tab = tab
        # Use the new rerun method instead of experimental_rerun
        st.rerun()

# Use session state for tab selection
selected_tab = st.session_state.selected_tab

# --- PAGE CONTENT ---
st.markdown(f'<h1 class="title">{translations[lang]["welcome"]}</h1>', unsafe_allow_html=True)

if selected_tab == translations[lang]["home"]:
    st.image("assets/picture.jpg", width=200, caption="Eyyüb Güven")
    st.write(translations[lang]["intro"])
    st.write(translations[lang]["professional_summary"])

elif selected_tab == translations[lang]["blog"]:
    st.header(translations[lang]["blog_header"])
    st.write("🚀 **Yakında!** Yeni blog yazılarım için takipte kalın.") if lang == "tr" else st.write("🚀 **Coming Soon!** Stay tuned for my latest blog posts.")

elif selected_tab == translations[lang]["about"]:
    st.header(translations[lang]["about_header"])
    
    # Education Section
    st.subheader(translations[lang]["education"])
    st.write("""
    - **M.Sc. Cognitive Science** - Nicolaus Copernicus University, Poland (2022–2024)
    - **B.Sc. Psychology** - Istanbul Esenyurt University, Turkey (2018–2022)
    """)
    
    # Experience Section
    st.subheader(translations[lang]["experience"])
    st.write("""
    - **R&D Scientist Manager** - OpenBrain, Istanbul, Turkey (2023–Present)
    
    - **AI Engineer Intern** - 1001 Epochs, Switzerland (Jan 2025–April 2025)
    - **Research Assistant** - University of Oslo, Oslo, Norway (2023–2024)
    """)

elif selected_tab == translations[lang]["skills"]:
    st.header(translations[lang]["skills_header"])
    st.write("""
    - **Neuroimaging:** fMRI, EEG, fNIRS, neuromodulation
    - **Programming:** Python, MATLAB, R
    - **Software:** FSL, Slurm
    - **Languages:** English (Fluent), Turkish (Native), Polish (Intermediate)
    """)
    
    st.subheader("Research Projects")
    st.write("""
    - **Vavtra Project** (2024–2025)
    - **Gamified Polyrhythmic Training in VR** (2023–2024)
    """)

elif selected_tab == translations[lang]["services"]:
    st.header(translations[lang]["services_header"])
    st.write("""
    - 🔹 Neurofeedback Training
    - 🔹 Cognitive Behavioral Therapy
    - 🔹 AI-powered Mental Health Solutions
    - 🔹 Brain-Computer Interface Consulting
    """)

elif selected_tab == translations[lang]["contact"]:
    st.header(translations[lang]["contact_header"])
    st.write(translations[lang]["contact_text"])
    st.write(f"📧 Email: {translations[lang]['contact_email']}")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/eyyub-gvn) | [GitHub](https://github.com/curiousbrutus)")
    st.write("🎓 ORCID: 0009-0005-6017-8622")
    
    contact_form = f"""
    <form action="https://formspree.io/f/your-form-id" method="POST">
        <input type="text" name="name" placeholder="{'Adınız' if lang == 'tr' else 'Your name'}" required>
        <input type="email" name="email" placeholder="{'E-posta' if lang == 'tr' else 'Your email'}" required>
        <textarea name="message" placeholder="{'Mesajınız' if lang == 'tr' else 'Your message'}" required></textarea>
        <button type="submit">{translations[lang]["send"]}</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
