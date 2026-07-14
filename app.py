import streamlit as st 
from utils.parser import parse_file

st.set_page_config(
    page_title="Influencer Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Influencer Discovery Dashboard")
st.write("Upload an Excel or CSV file and classify influencers using AI")

# sidebar
with st.sidebar:
    st.header("Search criteria")

    language = st.multiselect(
        "Language",
        ["Hindi", "English"],
        default=["Hindi", "English"],
    )

    orientation = st.selectbox(
        "Orientation",
        ["Pro Government", "Neutral", "Anti Government"],
    )

    niche = st.text_input(
        "Content Niche",
        value="Governemt Schemes, National Development",
    )

    keywords = st.text_area(
        "Keywords",
        value="Digital India, UPI, Startup India, Ayushman Bharat",
    )

uploaded_file = st.file_uploader(
    "Upload CSV/Excel",
    type=["csv", "xlsx"]
)

analyze = st.button("Analyze Influencers")

if analyze: 
    if uploaded_file is None:
        st.warning("Please upload a CSV or Excel file")

    else: 
        done = parse_file(uploaded_file)
        st.success("File upload successfully")
        st.dataframe(done)



# Render UI

# ↓

# Collect Inputs

# ↓

# Call Services

# ↓

# Show Results