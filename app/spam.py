def check_spam(text: str) -> str:
    text = text.lower().strip()
    
    # 텍스트가 비어있을 경우
    if text == "":
        return "ham", 0
    
    spam_keywords = [
        "free", "win", "winner", "prize", "click",
        "buy now", "urgent", "cash", "money", "offer", "deal"
    ]
    
    hit = 0
    for kw in spam_keywords:
        print(kw, text)
        if kw in text:
            hit += 1
            
    return ("spam" if hit >= 2 else "ham"), hit