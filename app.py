from flask import Flask
app = Flask(__name__)
#메인
@app.route('/')
def hello():
    return 'Hello, World!'
#야구
@app.route('/Baseball')
def baseball():
    return '야구 페이지!'
#축구
@app.route('/Soccer')
def Soccer():
    return '''
<html>
<body>

<h2>여기는 축구페이지</h2>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn0NYtbLJzv5JoCfuWcZlXxiqjj6i1u6JfQA&usqp=CAU" alt="Trulli" width="1000" height="500">

</body>
</html>

    '''
#농구
@app.route('/Basketball')
def Basketball():
    return '농구 페이지!'
#배구
@app.route('/Volleyball')
def Volleyball():
    return '배구 페이지!'

if __name__ == '__main__':
    app.run()    