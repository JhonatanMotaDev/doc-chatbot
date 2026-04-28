from pathlib import Path


def read_file(path: str) -> str:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")

    if file_path.suffix.lower() not in {".txt", ".md"}:
        raise ValueError("Formato invalido. Use apenas arquivos .txt ou .md")

    return file_path.read_text(encoding="utf-8")
