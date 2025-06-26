import pandas as pd

class LoaderAgent:
    def load_knowledge_base(self, csv_path="kb.csv"):
        df = pd.read_csv(csv_path)
        kb_df = df[['flags', 'instruction', 'category', 'intent', 'response']].dropna()
        return kb_df.to_dict(orient='records')
