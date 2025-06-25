from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''\
    <html>
    <head>
        <title>kflask Deployment Pipeline</title>
        <style>
            body {
                background-color: #ffefdd; /* light cream */
                font-family: Arial, sans-serif;
                color: #222;
                padding: 2em;
            }
            .step {
                margin-bottom: 1.5em;
                font-size: 1.2em;
            }
            .emoji {
                font-size: 1.3em;
                vertical-align: middle;
            }
        </style>
    </head>
    <body>
        <h1>kflask Deployment Pipeline</h1>
        <div class="step">GitHub stores the code <span class="emoji">✅</span></div>
        <div class="step">Quay builds the container <span class="emoji">✅</span></div>
        <div class="step">Flux Deploying to local k8 cluster <span class="emoji">❌</span></div>
        <div class="step">Successful service rollout and access via localhost:30666 <span class="emoji">✅👹</span></div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)