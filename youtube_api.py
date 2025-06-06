from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download')
def download_video():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No url parameter provided'}), 400

    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'skip_download': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # For demo, just return title and duration
            return jsonify({
                'title': info.get('title'),
                'duration': info.get('duration'),
                'url': url
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
