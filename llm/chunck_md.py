import re

def split_by_h2(txt: str) -> list[str]:
    """
    Teilt einen Markdown-Text und gibt nur die Abschnitte zurück,
    die mit '## ' beginnen.
    """
    parts = re.split(r"(?=^##\s+)", txt, flags=re.M)
    # nur behalten, wenn Abschnitt auch wirklich mit ## anfängt
    return [p.strip() for p in parts if p.strip().startswith("##")]