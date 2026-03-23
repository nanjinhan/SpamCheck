# feature-C: 첫번째 작업
# feature-C: 두번째 작업
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.spam import check_spam

# FastAPI 앱 생성
app = FastAPI(title="SpamCheck Web")

# 정적 HTML 파일
app.mount("/static", StaticFiles(directory="static"), name="static")

# 메인 페이지 (/) 처리
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

# classify 엔드포인트 처리
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
# feature-A: 세 번째 작업

# master: master쪽 수정

# feature-B: 첫 번째 작업
# feature-B: 두 번째 작업
# feature-B: 세 번째 작업
# 이건 실수 커밋입니다