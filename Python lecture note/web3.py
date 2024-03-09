from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

기상청_주소 = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
데이터 = request.urlopen(기상청_주소)

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>안녕하세요<h1>"

@app.route("/introduce")
def introduce():
    return "<h1>저를 소개합니다.<h1>" 

# 인공지능이나 웹 개발과 같은 분야는 관련 지식이 많이 필요함. 

@app.route("/weather")
def weather():
    output = ""
    soup = BeautifulSoup(데이터, "html.parser")
    for location in soup.select("location"):
        도시 = location.select_one("city").string
        for data in location.select("data"):
            시간 = (data.select_one("tmEf").string)
            기상상태 = (data.select_one("wf").string)
            최저기온 = (data.select_one("tmn").string)
            최고기온 = (data.select_one("tmx").string)
            output += f"<h1>{도시} {시간} {기상상태} {최저기온} {최고기온}<h1>"
    return output