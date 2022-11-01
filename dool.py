from flask import Flask , request, render_template
import os 

UPLOAD_FOLDER = '/home/d/Documents/code/python/poostvip'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#         background-image: url("{{ url_for('static', filename='montara-beach-california-wallpaper.jpg') }}");
#     <header class="intro-header" style="background-image: url('static/montara-beach-california-wallpaper.jpg')">

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return '''
        
        '''
    return '''
    <html>
    <head>
    <link rel="apple-touch-icon" sizes="180x180" href="static/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="static/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="static/favicon-16x16.png">
    <link rel="manifest" href="static/site.webmanifest">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style> 

    body{
        background-image: url('/static/stem.jpg');
        height:auto;
        text-align: center;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    @media screen and (max-width: 500px) {
    body {
        flex-wrap: nowrap;
        justify-content: normal;
        }      
    }     
    h1 {
        color: maroon;
        text-align: center;
    }
    .form-section{
        background-color: #f1f1f1;
        padding: 20px 10px;
        opacity: 0.8;

    }
    .form-section-right{
        float:right;
    }
    @media screen and (max-width: 500px){
        .form-section {width: 100%; 
            max-width: calc(100% - 20px);
            margin: 0 auto;
            }
    }


    </style>
    </head>
    <body >
    <h1>Upload new File</h1>
    <form class="form-section" method="post" enctype="multipart/form-data">

        <input class="upload-button" type="file" name="file1">
        <input class="submit-button" type="submit">
    
    </form>
    </body>
    </html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0')


"-------------------------------------------"
# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/', methods=['POST'])
# def upload_file():
#     uploaded_file = request.files['file']
#     if uploaded_file.filename != '':
#         uploaded_file.save(uploaded_file.filename)
#     return redirect(url_for('index'))


# if __name__ == '__main__':
#     app.run()