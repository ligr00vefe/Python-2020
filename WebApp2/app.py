"""
    날짜 : 2020/06/25
    이름 : 권기민
    내용 : 파이썬 웹 프로그래밍 조건문, 반복문
"""
from flask import Flask, render_template
# File > Setting > Project: Python > Project Interpreter > Flask 설치

app = Flask(__name__)

@app.route('/')
def index():
    
    title = '파이썬 Flask 제어문 실습'
    content = ''
    dataset = {
        'title': '대한민국 도시',
        'cities': ['서울', '대전', '대구', '부산', '광주']
    }
        
    return render_template('/index.html', tit=title, cont=content, data=dataset)


@app.route('/main')
def main():
    return render_template('/main.html')
        

if __name__ == '__main__':
    app.run()