import json


def build_prompt(language, orientation, niche, keywords, influencer):

    if isinstance(keywords, str):
        keywords = [k.strip() for k in keywords.split(",") if k.strip()]

    criteria = {
        "language": language,
        "orientation": orientation,
        "content_niche": niche,
        "keywords": keywords,
    }

    influencer_data = {
        "name": influencer["name"],
        "handle": influencer["handle"],
        "platform": influencer["platform"],
        "followers": influencer["followers"],
        "bio": influencer["bio"],
        "recent_posts": influencer["recent_posts"],
    }

    prompt = f"""
You are an AI system that classifies social media influencers.

Your task is to determine how well an influencer matches the provided search criteria.

========================
SEARCH CRITERIA
========================

{json.dumps(criteria, indent=2)}

========================
INFLUENCER INFORMATION
========================

{json.dumps(influencer_data, indent=2)}

========================
CLASSIFICATION GUIDELINES
========================

Analyze the influencer using BOTH:
- Bio
- Recent Posts

Evaluate:

1. Language
2. Content Orientation
3. Content Niche
4. Keyword Relevance
5. Overall Match

Important Rules:

- Do NOT rely only on keyword matching.
- Understand the overall context.
- Focus on the dominant theme of the content.
- Ignore isolated keyword mentions.
- If the creator has mixed content, classify based on the majority of the content.
- Be conservative while assigning high scores.
- Give scores above 80 only if the influencer strongly matches all criteria.

For this assignment:

Supportive Government Content includes topics like:

- Government Schemes
- National Development
- Infrastructure
- Public Welfare
- Digital India
- Startup India
- Skill India
- Make in India
- Ayushman Bharat
- PM Kisan
- UPI
- Viksit Bharat
- Economic Development

Do NOT classify someone as Pro Government solely because they mention a government keyword once.

========================
OUTPUT FORMAT
========================

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT wrap the JSON inside ```.

Return exactly this structure:

{{
    "match": true,
    "score": 92,
    "confidence": 95,
    "language": "Hindi",
    "orientation": "Pro Government",
    "content_niche": "Government Schemes",
    "matched_keywords": [
        "Digital India",
        "UPI"
    ],
    "summary": "Creates educational content explaining government initiatives and national development.",
    "reason": "Most recent posts consistently discuss Digital India, UPI and other government initiatives in a supportive manner."
}}

Rules:

- match must be true or false
- score must be an integer between 0 and 100
- confidence must be an integer between 0 and 100
- matched_keywords must always be a list
- summary should contain one short sentence
- reason should explain the classification
"""

    return prompt