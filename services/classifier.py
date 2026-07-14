import pandas as pd
from prompts.prompt import build_prompt
from services.anthropic_service import AnthropicService

class Classifier:
    def __init__(self): 
        self.ai = AnthropicService()

    def classify_dataframe(self, dataframe: pd.DataFrame, language, orientation, niche, keywords):
        results = []

        for _, row in dataframe.iterrows():
            prompt = build_prompt(
                language=language,
                orientation=orientation,
                niche=niche,
                keywords=keywords,
                influencer=row.to_dict(),
            )

            response = self.ai.classify(prompt)

            result={
                "name": row["name"],
                "handle": row["handle"],
                "platform": row["platform"],
                "followers": row["followers"],
                "score": response.get("score", 0),
                "confidence": response.get("confidence", 0),
                "match": response.get("match", False),
                "language": response.get("language", "Unknown"),
                "orientation": response.get("orientation", "Unknown"),
                "content_niche": response.get("content_niche", "Unknown"),
                "matched_keywords": ", ".join(response.get("matched_keywords", [])),
                "summary": response.get("summary", ""),
                "reason": response.get("reason", "")
            }

            results.append(result)
        return pd.DataFrame(results)
    
    result_df = result_df.sort_values(
    by="score",
    ascending=False
)