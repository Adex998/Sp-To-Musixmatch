from flask import Flask, request, render_template
from mxm import MXM
from spotify import Spotify

app = Flask(__name__)
sp = Spotify()
mxm = MXM()

@app.route('/', methods=['GET'])
def index():
    link = request.args.get('link')
    if link:
        try:
            if(len(link) < 12): return render_template('index.html', tracks_data= ["Wrong Spotify Link Or Wrong ISRC"])
            isrcs = sp.get_isrc(link) if len(link) > 12 else [{"isrc": link, "image": None}]
            #if isinstance(mxmLinks, list):
                #return "Fetching data failed!"
        except Exception as e:
            return render_template('index.html', tracks_data= [str(e)])
            
        mxmLinks = mxm.Tracks_Data(isrcs)
        if isinstance(mxmLinks, str):
            return mxmLinks

        return render_template('index.html', tracks_data= mxmLinks)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)