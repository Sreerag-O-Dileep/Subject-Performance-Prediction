from flask import Flask, request, render_template
from GNB import gnb
from RF import rf
from SVM import svm

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/x')
def my_form():
    return render_template('input.html')


@app.route('/getfile', methods=['POST'])
def my_form_post():
    text1 = int(request.form['user_school'])
    text2 = int(request.form['user_sex'])
    text3 = int(request.form['user_age'])
    text4 = int(request.form['user_addresstype'])
    text5 = int(request.form['user_familysize'])
    text6 = int(request.form['user_cohabitation'])
    text7 = int(request.form['user_mothereducation'])
    text8 = int(request.form['user_fathereducation'])
    text9 = int(request.form['user_motherjob'])
    text10 = int(request.form['user_fatherjob'])
    text11 = int(request.form['user_schoolchoose'])
    text12 = int(request.form['user_guardian'])
    text13 = int(request.form['user_traveltime'])
    text14 = int(request.form['user_studytime'])
    text15 = int(request.form['user_failures'])
    text16 = int(request.form['user_schoolsupport'])
    text17 = int(request.form['user_familysupport'])
    text18 = int(request.form['user_paidclasses'])
    text19 = int(request.form['user_extraactivities'])
    text20 = int(request.form['user_attendednursery'])
    text21 = int(request.form['user_highereducation'])
    text22 = int(request.form['user_internetaccess'])
    text23 = int(request.form['user_romantic'])
    text24 = int(request.form['user_familyrelation'])
    text25 = int(request.form['user_freetime'])
    text26 = int(request.form['user_goingout'])
    text27 = int(request.form['user_workalcohol'])
    text28 = int(request.form['user_weekalcohol'])
    text29 = int(request.form['user_health'])
    text30 = int(request.form['user_attendence'])
    text31 = int(request.form['user_s1'])
    text32 = int(request.form['user_s2'])

    if text31 >= 10:
        g1 = 1
    else:
        g1 = 0

    if text32 >= 10:
        g2 = 1
    else:
        g2 = 0

    x = [[text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16,
          text17, text18, text19, text20, text21, text22, text23, text24, text25, text26, text27, text28, text29, text30, g1, g2]]
    a = rf(x)
    b = gnb(x)
    c = svm(x)
    if a == b:
        output = a
    elif a == c:
        output = a
    elif b == c:
        output = b
    
    if output=='bad':
        info="This is just an assessment based on the data you have given. This prediction shows that there is higher probabilty for you to fail in this subject. You should work hard for getting better results"
    else:
        info="This is just an assessment based on the data you have given. This prediction shows that there is higher probabilty for you getting good result in this subject. You should work hard like this, else this prediction can be wrong"

    return render_template('results.html',output=output,info=info)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8080)
