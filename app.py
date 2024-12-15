from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 替换为你的 OpenWeather API Key
API_KEY = 'f5ac8f4f4225fbe65c676761cdbbe1eb'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    # 获取前端传来的城市名称
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'City is required'})

    # 调用 OpenWeather API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    # 检查API返回状态
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }
        return jsonify(weather)
    else:
        return jsonify({'error': 'City not found'})

if __name__ == '__main__':
    app.run(debug=True)
