from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.spam import check_spam

# FastAPI 기반 웹 앱 생성
app = FastAPI(title="SpamCheck Web")

# 정적 HTML 서빙
app.mount("/static", StaticFiles(directory="static"), name="static")

# 메인 페이지 (/) 처리
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

# classify 요청이 올 때 비동기 처리
@app.post("/classify")
async def classify(
    payload: dict = Body(..., example={"text": "Win a FREE prize now, click!"})
):
    text = payload["text"]
    label, score = check_spam(text)
    return {
        "label": label, "score": score
    }

    # feature-A: 첫 번째 작업
    # feature-A: 두 번째 작업
