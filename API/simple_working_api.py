from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
import os
import json

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    # Serve the working frontend
    frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "working.html")
    if os.path.exists(frontend_path):
        with open(frontend_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), media_type="text/html")
    
    return {"message": "Instagram Sentiment Analyzer - Simple Working Version", "status": "success"}

@app.post("/analyze/")
async def analyze_sentiment(data: dict):
    try:
        print(f"=== REQUEST RECEIVED ===")
        print(f"Request data: {data}")
        
        url = data.get('url', '')
        print(f"URL: {url}")
        
        if not url:
            return JSONResponse(
                {"error": "URL is required"}, 
                status_code=400
            )
        
        # Simple mock sentiment analysis
        if "p/" in url:
            # Post URL - positive sentiment
            mock_comments = [
                "Amazing post! Love the content",
                "Great work! Really impressive", 
                "Fantastic quality! Best content ever",
                "Wonderful! Amazing job done here"
            ]
            positive_ratio = 0.8
            negative_ratio = 0.2
        else:
            # Profile URL - mixed sentiment
            mock_comments = [
                "Good profile! Nice content",
                "Not bad but could be better",
                "Some great posts, some okay ones"
            ]
            positive_ratio = 0.6
            negative_ratio = 0.4
        
        total_comments = len(mock_comments)
        positive_count = int(total_comments * positive_ratio)
        negative_count = int(total_comments * negative_ratio)
        
        print(f"Analysis complete: {positive_count} positive, {negative_count} negative")
        
        return JSONResponse({
            "url": url,
            "total_comments": total_comments,
            "positive_count": positive_count,
            "negative_count": negative_count,
            "positive": round(positive_ratio, 2),
            "negative": round(negative_ratio, 2),
            "message": "Analysis completed successfully",
            "results": [
                {"comment": comment, "sentiment": "positive" if i < positive_count else "negative"} 
                for i, comment in enumerate(mock_comments)
            ]
        })
        
    except Exception as e:
        print(f"Error in analysis: {e}")
        return JSONResponse(
            {"error": str(e)}, 
            status_code=500
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)
