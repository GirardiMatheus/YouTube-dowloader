from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

def download_video(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            return f'Video "{title}" baixado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro: {str(e)}'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    message = download_video(url)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
