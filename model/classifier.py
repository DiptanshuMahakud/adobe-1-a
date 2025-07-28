from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

model_dir = Path(__file__).resolve().parent / "bin"

tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(model_dir, local_files_only=True)

classifier = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    top_k=None,
    device=-1,
    truncation=True,  
    max_length=512,   
    padding=True 
)

def classify(inp:str):
    text = [inp]
    predictions = classifier(text)
    result = [int(max(item, key=lambda x: x['score'])['label'].split('_')[1]) for item in predictions]
    return result[0]