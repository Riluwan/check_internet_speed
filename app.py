from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

@app.route('/speedtest', methods=['GET'])
def run_speedtest():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()
    return jsonify({
        'download_speed': results['download'],
        'upload_speed': results['upload'],
        'ping': results['ping']
    })

if __name__ == '__main__':
    app.run(debug=True)
