import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from flask import Blueprint, render_template, request, session, send_file

link = Blueprint('link', __name__)

home = os.path.expanduser("~")
downloads = os.path.join(home, "Downloads")

@link.route('/download_video/<itag>')
def down_video(itag):
    yt = YouTube(session['link'], on_progress_callback=on_progress)
    video = yt.streams.get_by_itag(itag)
    return send_file(os.path.join(downloads, video.download()))

@link.route('/download_audio/<itag>')
def down_audio(itag):
    yt = YouTube(session['link'], on_progress_callback=on_progress)
    audio = yt.streams.get_by_itag(itag)
    return render_template('result.html', file=audio.download())

@link.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')
        session['link'] = link
        yt = YouTube(link, on_progress_callback=on_progress)
        try:
            yt.check_availability()
        except Exception as e:
            return render_template('error.html)', error=str(e))
        streams = yt.streams
        title = yt.title
        return render_template('index.html', link=link, streams=streams, title=title, thumbnail=yt.thumbnail_url)
    return render_template('index.html')