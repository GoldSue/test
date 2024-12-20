import os
from concurrent.futures import ThreadPoolExecutor

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
# 从环境变量中获取 OpenWeather API Key
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# 使用线程池来处理 API 请求
executor = ThreadPoolExecutor(max_workers=5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    # 获取前端传来的城市名称
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    # 使用线程池异步调用 API
    future = executor.submit(fetch_weather, city)
    weather = future.result()

    return jsonify(weather)

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)  # 设置请求超时
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }
        return weather
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}, response.status_code
    except requests.exceptions.RequestException as req_err:
        return {'error': f'Request error occurred: {req_err}'}, 500

if __name__ == '__main__':
    app.run(debug=True)
