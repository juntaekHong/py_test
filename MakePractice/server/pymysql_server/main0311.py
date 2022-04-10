from operator import mod
from flask import Flask, render_template, request, redirect, url_for
#모듈에 넣어놨기 때문에 굳이 할 필요없음import pymysql
from modules import mod0314_sql

app = Flask(__name__) # name에는 내가 실행시키는 파일이 들어간다.
#post형식 상대적으로 느림
@app.route('/') # web: 주소->127.0.0.1:5000/ , localhost:500/

def index():
    return render_template("index.html")
#빈 url
# localhost/signup
@app.route('/signup/', methods=['GET']) # web-> 주소 127.0.0.1:5000/signup/
def signup():
    return render_template("signup.html")
# 두번째 페이지 만들기
@app.route("/signup/", methods=['POST'])
def signup_2():
    #_db = pymysql.connect(
    #user = "root", # mysql 아이디
    #passwd = "*Bethewannabe27", # mysql 비밀번호
    #host ="localhost", # 내 컴퓨터 
    #db = "ubion"
    #)
    #sql쿼리문을 실행시키기 위한 cursor
    #cursor = _db.cursor(pymysql.cursors.DictCursor)
    _id = request.form["_id"]
    _password = request.form["_password"]
    _phone = request.form["_phone"]
    _ads = request.form["_ads"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _regitdate = request.form["_regitdate"]
    _name = request.form["_name"]
    sql = """ 
         INSERT INTO user_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
          """
    _values = [_id, _password, _phone, _ads, _gender, _age, _regitdate,_name]
    #print(_values)
#    cursor.execute(sql, _values)
#   _db.commit()
#      _db.close()
    _db=mod0314_sql.Database()
    _db.execute(sql,_values)
    _db.commit()

    
    return redirect(url_for('index'))
#아무리 주소가 변경되더라도 index로 실행되는 것을 뜻함
#기존에 있는 어딘가로 돌아가는 것.
#index
    
@app.route("/login/",methods=["POST"])
def login():
    _id = request.form["_id"]
    _password = request.form["_password"]

    sql = """ 
         SELECT * from user_info WHERE ID=%s and password=%s
         """
    _values =[_id,_password]
    _db = mod0314_sql.Database()
    result=_db.__excuteAll__(sql,_values)
    
    
    print(result) #2번완료 #이름이랑 아이디 같이 보내야함. name을 적어서
    
    if result:
        return render_template("welcome.html",name =result[0]["name"],
                               id=result[0]["ID"])
    else:
        return redirect(url_for('index'))
    #존재하면 true, len 써도 되고 if len(result) 튜플이니 개수1 길이 1
    #return redirect(url_for('index'))
    
@app.route("/update/")
def update():
    id= request.args["_id"]
    sql="""
        SELECT * FROM user_info WHERE ID = %s
        """
    values=[id]
    
    _db =mod0314_sql.Database()
    result = _db.__excuteAll__(sql,values)
    return render_template("update.html",info =result[0])

@app.route("/update/", methods=["POST"])
def update_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _phone = request.form["_phone"]
    _ads = request.form["_ads"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _name = request.form["_name"]
    sql ="""
        UPDATE user_info SET 
        password=%s,
        phone =%s,
        gender=%s,
        age = %s,
        ads= %s,
        name =%s
        where ID =%s
        """
        #ID값은  프라이머리키라서 없음
    values =[_password,_phone,_gender,_age,_ads,_name,_id]
    _db=mod0314_sql.Database()
    _db.execute(sql,values)
    _db.commit()
    return redirect(url_for('index'))
    #redirect('/')도 같은기능
    #DB에 접속해서 Select 문을 가지고 인덱스 페이지에 아이디와 
    # 패스워드값을 받아와서
    #Select 문으로 조회
    #결과가 존재하면 return "login"
    #존재하지 않으면 return "fail"
    
#회원탈퇴 만들기
# welcome.html ->delete url로 접속--> 로그인한 ID값을 같이 전송
# delete -> password를 확인! -> id password가 db에 존재하면 delete 
#존재하지 않으면 패스워드가 맞지 않습니다라는 메세지를 페이지에 띄워주는 형식으로 만들기
#delete.html페이지생성

@app.route("/delete/",methods=["GET"]) #맨처음에 get의 형태로 만들어준다.
def delete():
    _id = request.args["_id"]
    return render_template("delete.html",id=_id)
#렌더 템플레이트는 html을 불러오고, redirect는 url을 다른 url로 바꿔놓는 작업
#updaate에서와 같이 id값을 보내준 것은 똑같음.
#delete에서는 아이디값을 받아온 다음 아이디값을 보내줌.

@app.route("/delete", methods=["POST"])
def delete_2():
    _id = request.form["_id"]
    #앞에 값이 키값, 뒤에값이 벨류값
    _password=request.form["_password"]
    _db = mod0314_sql.Database()
    s_sql = """ 
                select * from user_info WHERE ID=%s and password=%s
            """
    d_sql = """ 
                delete from user_info WHERE ID=%s and password=%s
            """
         
    _values =[_id,_password]
    
    result=_db.__excuteAll__(s_sql,_values)
    if not result:
        return "패스워드가 일치하지 않습니다."
    else:
        _db.execute(d_sql,_values)
        _db.commit()
        return redirect(url_for('index'))
    

@app.route("/view", methods=["GET"])
def _view():
    _db = mod0314_sql.Database()
    
    sql="""
        select user_info.name, 
        user_info.ads, 
        user_info.age,
        ads_info.register_count
        from user_info 
        left join 
        ads_info 
        on user_info.ads =  ads_info.ads
        """
    result=_db.__excuteAll__(sql)
    key=list(result[0].keys())
    
    return render_template("view.html",result=result,keys=key)


    # -> sql문을 사용할 건데 ->user_info left join ads_info 
    #columns-> user_info : name,ads,age / ads_info :register_count user_info ,ads_info ads쿼리문작성해서
    #view.html을 render 쿼리문의 결과 값을 데이터로 같이 보내주는 코드를 작성
    
    
    #존재하면 true, len 써도 되고 if len(result) 튜플이니 개수1 길이 1
    #return redirect(url_for('index'))
    
app.run(port=8080 )
#debug 저장할때마다 저절로 실행시켜줌