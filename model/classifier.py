from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

model_dir = "./bin"  

tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)

classifier = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    top_k=None,
    device=-1
)

def classify(inp:str):
    text = [inp]
    predictions = classifier(text)
    result = [int(max(item, key=lambda x: x['score'])['label'].split('_')[1]) for item in predictions]
    return result[0]