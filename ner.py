import spacy

def nermodule(text):
    try:
        model_path = r"C:\Users\anils\Downloads\wellfound asstment 1\xlm-roberta-large"
        nlp = spacy.util.load_model_from_path(model_path)
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
    except Exception as e:
        print(f"Error in NER module: {e}")
        return None
