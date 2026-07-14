# 📊 Influencer Discovery Dashboard

An AI-powered dashboard that identifies and ranks influencers based on user-defined criteria such as language, content orientation, niche, and keywords.

This project was developed as part of a technical assignment using a **file-based analysis** approach. Users can upload an Excel or CSV file containing influencer information, and the application classifies each influencer using Anthropic Claude AI.

---

# Features

- 📂 Upload CSV or Excel files
- ✅ Automatic file validation
- 🤖 AI-powered influencer classification using Anthropic Claude
- 🌐 Language detection
- 🎯 Content niche matching
- 📈 Relevance score (0–100)
- 📊 Confidence score
- 💬 AI-generated reasoning for every classification
- 📋 Interactive results table
- 🔍 Built-in search, sorting, fullscreen view and CSV download (Streamlit DataFrame)

---

# Tech Stack

- Python
- Streamlit
- Pandas
- Anthropic Claude API
- python-dotenv

---

# Project Structure

```
influencer-discovery-dashboard/

│── app.py
│
├── config/
│   └── config.py
│
├── services/
│   ├── anthropic_service.py
│   └── classifier.py
│
├── prompts/
│   └── prompt.py
│
├── utils/
│   ├── parser.py
│   └── validator.py
│
├── data/
│   └── sample.csv
│
├── requirements.txt
├── .env
└── README.md
```

---

# How It Works

1. Upload a CSV or Excel file containing influencer information.
2. The application validates the uploaded file.
3. Each influencer is sent to Anthropic Claude along with the selected search criteria.
4. Claude analyzes the influencer's bio and recent posts.
5. A relevance score, confidence score, language, orientation, niche match and reasoning are generated.
6. Results are displayed in an interactive dashboard.

---

# Required CSV Columns

The uploaded dataset should contain the following columns:

| Column       | Description             |
| ------------ | ----------------------- |
| name         | Influencer Name         |
| handle       | Social Media Handle     |
| platform     | Instagram / YouTube / X |
| followers    | Follower Count          |
| bio          | Influencer Bio          |
| recent_posts | Recent Posts or Content |

---

# Running the Project

## Clone Repository

```bash
git clone <repository-url>
cd influencer-discovery-dashboard
```

## Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file.

```env
ANTHROPIC_API_KEY=your_api_key
```

## Start Application

```bash
streamlit run app.py
```

---

# Sample Classification Criteria

Language

- Hindi
- English

Orientation

- Pro Government

Content Niche

- Government Schemes
- National Development
- Progress Related Themes

Keywords

- Digital India
- UPI
- Startup India
- Ayushman Bharat

---

# Future Improvements

- Batch LLM processing for faster analysis
- Support for real-time YouTube search
- Additional filtering options
- Export reports in PDF format
- Multiple LLM provider support
- Analytics dashboard with charts

---

# Author

Shiva Kumar
