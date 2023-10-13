from fastapi import FastAPI
from models import RequestItem
from html_parser import HTMLParser

app = FastAPI()


@app.post("/topics")
async def find__topics(request: RequestItem):
    html_parser = HTMLParser()
    html_text = html_parser.get_html_from_url(request.url)
    parsed_html = html_parser.parse_html(html_text)

    return html_parser.find_topics_from_parsed_html(parsed_html)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
