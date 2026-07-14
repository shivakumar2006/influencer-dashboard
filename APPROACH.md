# Influencer Discovery Dashboard – Approach

## Approach

For this assignment, I implemented the **File-Based Analysis** approach, as the assignment allowed either a real-time search solution or a file-based solution.

The application allows users to upload a CSV or Excel file containing influencer information. Once the file is uploaded, it is parsed using Pandas and validated to ensure all required columns are present. After successful validation, each influencer is analyzed individually using Anthropic Claude AI.

The AI receives the user-defined search criteria (language, orientation, content niche, and keywords) along with the influencer's profile information (bio and recent posts). Based on this information, the AI evaluates how closely the influencer matches the provided criteria and returns a structured JSON response.

The dashboard then ranks all influencers according to their relevance score and displays the results along with confidence score, matched keywords, content niche, and reasoning.

---

## Assumptions

- Since no sample dataset was provided with the assignment, I created a representative dataset for demonstration purposes.
- The uploaded dataset is expected to contain the following columns:
  - name
  - handle
  - platform
  - followers
  - bio
  - recent_posts

- The influencer's bio and recent posts provide sufficient context for AI-based classification.
- The Anthropic Claude API returns a structured JSON response for every influencer.

---

## Classification Logic

Each influencer is processed independently.

For every influencer, the application combines:

- User-selected language
- Orientation
- Content niche
- Keywords
- Influencer bio
- Recent posts

These details are passed to Anthropic Claude through a carefully designed prompt.

Claude evaluates:

- Language match
- Content orientation
- Niche relevance
- Keyword relevance
- Overall contextual similarity

The AI then returns:

- Match (True/False)
- Relevance Score (0–100)
- Confidence Score (0–100)
- Detected Language
- Detected Orientation
- Content Niche
- Matched Keywords
- Summary
- Reasoning

Finally, the application sorts the influencers based on their relevance score and presents the results in an interactive Streamlit dashboard.

---

## Future Improvements

The current implementation focuses on the file-based workflow, which satisfies the assignment requirements. The architecture is modular, making it straightforward to replace the CSV input layer with a real-time data source such as the YouTube Data API or other social media APIs in future iterations without changing the AI classification pipeline.
