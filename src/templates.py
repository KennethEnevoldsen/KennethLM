"""
This include templates for seq2seq Danish NLP.
"""

def sentiment(target, examples: list[tuple[str, str]], labels: list[str] = ["positiv", "negativ", "neutral"]) -> str:
    labels_str = ", ".join(labels[:-1]) + " eller " +  labels[-1]
    template = f"""For hver af de følgende sætninger bestem dets sentiment eller valens. Sentiment er om en tekst er positivt ladet elle ej. De mulige
    kategorier en tekst kan høre til er: {labels_str}."""
    example_splitter = "\n\n"

    for example, label in examples:
        template += example_splitter +  f"{example}\nkategori: {label}"
    template += example_splitter + f"{example}\nkategori: "

    return template

def question_answering(target, examples: list[tuple[str, str]]) -> str:
    template = """Her er svarende på dine spørgsmål:"""

    example_splitter = "\n\n"
    
    for i, (question, answer) in examples:
        template += example_splitter + f"Spørgsmål {i}: {question}\nsvar: {answer}"
    template += example_splitter + f"Spørgsmål {i+1}: {target}\nsvar: "
    return template

def lexical_acceptability(target, examples: list[tuple[str, str]]) -> str:
    template = """Bestem om de følgende sætninger er grammatisk korrekte"""

    example_splitter = "\n\n"
    
    for i, (sentence, label) in examples:
        template += example_splitter + f"Sætning: \n{sentence}\Grammatisk acceptabel: {label}"
    template += example_splitter + f"Sætning {i+1}: {target}\nGrammatisk acceptabel:"
    return template