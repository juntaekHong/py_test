from flask import Flask , render_template , send_file
import pandas as pd
import matplotlib.pyplot as plt 
from io import BytesIO 

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/corona/')
def corona():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns=["인덱스","등록일시","사망자","확진자","게시글번호",
                       "기준일","기준시간","수정일시","누적 의심자","누적 확진률"]
    corona_df["일일 사망자"] = ((corona_df["사망자"]) - corona_df["사망자"].shift()).fillna(0)
    corona_df["일일 확진자"] = ((corona_df["확진자"]) - corona_df["확진자"].shift()).fillna(0)
    corona_df["일일 확진자"].values.tolist() 
    corona_df["등록일시"].values.tolist()
    corona_df.sort_values("등록일시",inplace=True)
    corona_df=corona_df.drop(["인덱스","기준일","기준시간","수정일시","게시글번호"],axis=1)
                  #     "기준일","기준시간","수정일시","누적 의심자","누적확진률"],axis=1,inplace=True)
    #drop으로 해서 몇개 빠뜨리고, axis=1 넣어서 빼주기
    corona_df.reset_index(drop=True,inplace=True)
    
    corona_dict =corona_df.head(50).to_dict() #to_dict 딕셔너리형태로 바꿈
    
    cnt=len(corona_dict["등록일시"].keys()) #len 값 때문에 인덱스 계속 나옴 50넘음
 
    return render_template('corona.html', result = corona_dict,
                           cnt = cnt )
#변수['컬럼명']=(변수_2['컬럼명2']-변수['컬러명'].shift()).filla(0)
#html주석처리  <!--파이썬 코드 사용하기 위해서-->
#  <!--파이썬 코드 사용하기 위해서-->
    #<!--{% for i in result %}
#{{result["등록일시"][i]}} <!--여기서는 .values안해도됨 왜
 #   냐하면 .values는 판다스 라이브러리이기 때문-->>
  #  <!--for문 들여쓰기는 {%으로 한다.}-->
   # <!--{% endfor %}-->
@app.route("/img")
def img():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns=["인덱스","등록일시","사망자","확진자","게시글번호",
                       "기준일","기준시간","수정일시","누적 의심자","누적 확진률"]
    corona_df=corona_df.drop(["인덱스","기준일","기준시간","수정일시","게시글번호"],axis=1)
    corona_df["일일 사망자"] = (corona_df["사망자"]).diff().fillna(0)
    corona_df.sort_values("등록일시",inplace=True)
    decide_cnt = corona_df.head(10)["일일 사망자"].values.tolist()
    state_dt=corona_df.head(10)["등록일시"].values.tolist()
    
    plt.plot(state_dt,decide_cnt)
    img_1 = BytesIO() #이미지로 저장해주는 문장
    plt.savefig(img_1,format="png",dpi=200)
    img_1.seek(0)
    #send_file은 웹에 이밎 파일을 보내주는 작업
    return send_file(img_1,mimetype='image/png')

app.run()



