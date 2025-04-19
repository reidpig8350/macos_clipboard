history = []

def add_to_history(content):
    if content not in history:  # 避免重複添加
        history.append(content)

def get_history():
    return history