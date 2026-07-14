import streamlit as st 
from utils.parser import parse_file
from utils.validator import validate_frames
from services.classifier import Classifier

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
        
        valid, missing = validate_frames(done)
        if not valid: 
            st.error(f"missing required columns: {', '.join(missing)}")
            st.stop()

        st.success("CSV validated successfully")

        st.subheader("📊 Dataset Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Influencers",
            len(done)
        )

        col2.metric(
            "Platforms",
            done["platform"].nunique()
        )

        col3.metric(
            "Total Followers",
            f"{done['followers'].sum():,}"
        )

        st.subheader("📄 Uploaded Dataset")
        st.dataframe(done)


        classifier = Classifier()

        with st.spinner("Analyzing influencers using Claude AI..."):
            result_df = classifier.classify_dataframe(
                dataframe=done,
                language=language,
                orientation=orientation,
                niche=niche,
                keywords=keywords,
            )

        result_df = result_df.sort_values(
            by="score",
            ascending=False
        )

        st.subheader("📈 Classification Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Matched",
            int(result_df["match"].sum())
        )

        col2.metric(
            "Average Score",
            f"{result_df['score'].mean():.0f}"
        )

        col3.metric(
            "Highest Score",
            int(result_df["score"].max())
        )

        col4.metric(
            "Average Confidence",
            f"{result_df['confidence'].mean():.0f}%"
        )

        st.subheader("🤖 Classification Results")

        st.dataframe(result_df)