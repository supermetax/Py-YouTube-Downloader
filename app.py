from flask import Flask, request, jsonify, render_template
from pytube import YouTube

app = Flask(__name__)

'''
@app.route('/')
def hello_world():
    return 'Hello, World!'
'''
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.json.get('video_url')
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download('downloads')
        return jsonify({'message': 'Video downloaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
