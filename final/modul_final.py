import pymysql
class Database():
    def __init__(self):
        self._db=pymysql.connect(
            user = "root", 
            passwd = "*Bethewannabe27",
            host ="localhost",
            db = "ubion"
            )
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)
        
#빈딕셔너리
    def execute(self,sql,values={}):
        self.cursor.execute(sql,values)
        #self._db.commit() 변경된 값이 없으면 커밋할 필요없음
        #왜굳이 여기에는 안 넣어놨을까
        #효율적인 것은 전부다 해주고 하는 것이 더 효율적
        #중복으로 넣는 경우가 있을 수도 있기 때문에
    def __excuteAll__(self,sql,values={}):
        self.cursor.execute(sql,values)
        
        self.result=self.cursor.fetchall()
        return self.result
    
    def commit(self):
        self._db.commit()