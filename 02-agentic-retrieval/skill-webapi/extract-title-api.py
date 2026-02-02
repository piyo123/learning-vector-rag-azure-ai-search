# $ uvicorn extract-title-api:app --host 0.0.0.0 --port 8000 --reload

from fastapi import FastAPI
from typing import Any

app = FastAPI()

@app.get("/")
def handler():
    return "Running"

@app.post("/extractTitle")
def extract_title(payload: dict[str, Any]):
    values = payload.get("values", [])
    out = []

    for v in values:
        record_id = v.get("recordId")
        text = ((v.get("data") or {}).get("text")) or ""

        title = ""
        for line in text.splitlines():
            s = line.strip()
            if s:
                title = s
                break

        out.append({
            "recordId": record_id,
            "data": {"title": title}
        })

    return {"values": out}


