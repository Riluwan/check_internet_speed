from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

@app.route('/speedtest', methods=['GET'])
def run_speedtest():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()
    download_speed_mbps = results['download'] / 1_000_000  # Convert to Mbps
    upload_speed_mbps = results['upload'] / 1_000_000  # Convert to Mbps
    ping_ms = results['ping']  # Ping is already in ms
    return jsonify({
        'download_speed_mbps': download_speed_mbps,
        'upload_speed_mbps': upload_speed_mbps,
        'ping_ms': ping_ms
    })

if __name__ == '__main__':
    app.run(debug=True)
