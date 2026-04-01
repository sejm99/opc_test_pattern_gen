from flask import Flask, render_template ,request
from flask import send_file

## 전역변수 
GDS_NAME = None
TEXT_FILE_NAME = None

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  return render_template('index.html')
  # return ('index.html')

@app.route('/genteg1', methods=['POST','GET']) ## 데이터값 전달
def genteg1(): # 입력값이 1종류
  if request.method == "POST":
    Type = request.form.get('Type')
    LAYER_NO = int(request.form.get('LAYER_NO'))
    LINE = request.form.get('LINE').split()
  if Type != "" and LINE != "":
    ## GDS 생성위한 함수 호출
    gds_name = GEN_TEG_OPC(S1=None,GAP=None,LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)
    if gds_name != None:
      return render_template('download.html',LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)
    else:
      return ("Error : GDS 만들기 실패 하였습니다.")
  else:
    return render_template('Notindata.html',LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)

@app.route('/genteg2', methods=['POST','GET']) ## 데이터값 전달
def genteg2(): # 입력값이 2종류
  if request.method == "POST":
    print(request.form)
    Type = request.form.get('Type')
    LAYER_NO = int(request.form.get('LAYER_NO'))
    GAP = request.form.get('GAP').split()
    LINE = request.form.get('LINE').split()
    #GAP = dual_list_gen(GAP)
    #LINE = dual_list_gen(LINE)
  if Type != "" and GAP != "" and LINE != "":
    ## GDS 생성위한 함수 호출
    gds_name = GEN_TEG_OPC(S1=None,GAP=GAP,LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)
    if gds_name != None:
      return render_template('download.html',GAP=GAP,LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)
    else:
      return ("Error : GDS 만들기 실패 하였습니다.")
  else:
    return render_template('Notindata.html',GAP=GAP,LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)

@app.route('/genteg3', methods=['POST','GET']) ## 데이터값 전달
def genteg3():# 입력값이 3종류
  if request.method == "POST":
    #print(request.form)
    Type = request.form.get('Type')
    LAYER_NO = int(request.form.get('LAYER_NO'))
    S1 = request.form.get('S1').split()
    GAP = request.form.get('GAP').split()
    LINE = request.form.get('LINE').split()
    #Island(LINE)
    # if Type == 'CTDLE':
    #   S1 = dual_list_gen(S1)
    #   GAP = dual_list_gen(GAP)
    #   LINE = dual_list_gen(LINE)
  if Type != "" and S1 !="" and GAP != "" and LINE != "":
    ## GDS 생성위한 함수 호출
    gds_name = GEN_TEG_OPC(S1=S1,GAP=GAP,LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)
    if gds_name != None:
      return render_template('download.html',S1=S1,GAP=GAP,LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)
    else:
      return ("Error : GDS 만들기 실패 하였습니다.")
  else:
    return render_template('Notindata.html',S1=S1,GAP=GAP,LINE=LINE,TYPE=Type,LAYER_NO=LAYER_NO)

def dual_list_gen(xx):
    dubble_list_line = []
    for x in xx:
      tmp = []
      tmp.append(x)
      dubble_list_line.append(tmp)
    return  dubble_list_line

def GEN_TEG_OPC(S1,GAP,LINE,TYPE,LAYER_NO):
  global GDS_NAME
  global TEXT_FILE_NAME
  if TYPE == "CTDLE":
    from OPC_TEG.CTDLE.CTDLE import main as Ctdle 
    GDS_NAME,TEXT_FILE_NAME = Ctdle(LAYER_NO,S1,GAP,LINE)
  elif TYPE == "CL1B":
    from OPC_TEG.Centerline_1Bar.Centerline_1Bar import main as cl1b
    GDS_NAME,TEXT_FILE_NAME = cl1b(LAYER_NO,S1,GAP,LINE)
  elif TYPE == "CL3B":
    from OPC_TEG.Centerline_3Bar.Centerline_3Bar import main as cl3b
    GDS_NAME,TEXT_FILE_NAME = cl3b(LAYER_NO,S1,GAP,LINE)
  elif TYPE == "ISLAND":
    from OPC_TEG.ISLAND.Island import main as Island
    GDS_NAME,TEXT_FILE_NAME = Island(LAYER_NO,GAP,LINE)
  elif TYPE == "INV_ISLAND":
    from OPC_TEG.INV_ISLAND.INV_Island import main as INV_Island
    GDS_NAME,TEXT_FILE_NAME = INV_Island(LAYER_NO,GAP,LINE)
  elif TYPE == "PITCH":
    from OPC_TEG.PitchLineLinearity.pitch import main as PITCH
    GDS_NAME,TEXT_FILE_NAME = PITCH(LAYER_NO,GAP,LINE)
  elif TYPE == "PitchSpaceLinerity":    
    from OPC_TEG.PitchSpaceLinerity.PitchSpaceLineriry import main as pitch_space_linerity
    GDS_NAME,TEXT_FILE_NAME = pitch_space_linerity(LAYER_NO,GAP,LINE)
  elif TYPE == "ISOLine":
    from OPC_TEG.ISOLineLinearity.ISOLineLinearity import main as ISOLineLinearity
    GDS_NAME,TEXT_FILE_NAME = ISOLineLinearity(LAYER_NO,LINE)
  elif TYPE == "ISOSpace":
    from OPC_TEG.ISOSpaceLinerrity.ISOSpaceLinearity import main as ISOSpaceLinearity
    GDS_NAME,TEXT_FILE_NAME = ISOSpaceLinearity(LAYER_NO,LINE)
  elif TYPE == "BIG":
    from OPC_TEG.BIG.BIG import main as BIG
    GDS_NAME,TEXT_FILE_NAME = BIG(LAYER_NO,LINE,GAP)
  elif TYPE == "2BAR":
    from OPC_TEG.BAR2.BAR2 import main as BAR2
    GDS_NAME,TEXT_FILE_NAME = BAR2(LAYER_NO,LINE,GAP)  
  elif TYPE == "3BAR":
    from OPC_TEG.BAR3.BAR3 import main as BAR3
    GDS_NAME,TEXT_FILE_NAME = BAR3(LAYER_NO,LINE,GAP)  
  elif TYPE == "ISOLineEnd":
    from OPC_TEG.ISOLineEnd.ISOLineEnd import main as ISOLineEnd
    GDS_NAME,TEXT_FILE_NAME = ISOLineEnd(LAYER_NO,LINE,GAP)  
  elif TYPE == "DLE":
    from OPC_TEG.DLE.DLE import main as DLE
    GDS_NAME,TEXT_FILE_NAME = DLE(LAYER_NO,S1,GAP,LINE) 
  elif TYPE == "INVISOLineEnd":
    from OPC_TEG.INV_ISOLineEnd.INV_ISOLineEnd import main as INVISOLineEnd
    GDS_NAME,TEXT_FILE_NAME = INVISOLineEnd(LAYER_NO,LINE,GAP) 
  elif TYPE == "INV_DenseLineEnd":
    from OPC_TEG.INV_DenseLineEnd.INV_DenseLineEnd import main as INV_DenseLineEnd
    GDS_NAME,TEXT_FILE_NAME = INV_DenseLineEnd(LAYER_NO,S1,GAP,LINE) 
  elif TYPE == "CenterLineISOLineEnd":
    from OPC_TEG.CenterLineISOLineEnd.CenterLineISOLineEnd import main as CenterLineISOLineEnd
    GDS_NAME,TEXT_FILE_NAME = CenterLineISOLineEnd(LAYER_NO,GAP,LINE) 
  else:
    GDS_NAME = None
  return GDS_NAME

@app.route('/CenterLineISOLineEnd')
def CenterLineISOLineEnd():
  return render_template('CenterLineISOLineEnd.html')

@app.route('/INV_DenseLineEnd')
def INV_DenseLineEnd():
  return render_template('INV_DenseLineEnd.html')

@app.route('/INV_ISOLineEnd')
def INV_ISOLineEnd():
  return render_template('INV_ISOLineEnd.html')

@app.route('/DenseLineEnd')
def DenseLineEnd():
  return render_template('DenseLineEnd.html')

@app.route('/ISO_LINE_END')
def ISO_LINE_END():
  return render_template('ISO_LINE_END.html')

@app.route('/3BAR')
def BAR3():
  return render_template('3BAR.html')

@app.route('/2BAR')
def BAR2():
  return render_template('2BAR.html')

@app.route('/BIG')
def BIG():
  return render_template('BIG.html')

@app.route('/ISO_Space')
def ISO_Space():
  return render_template('ISOSpace.html')

@app.route('/ISO_line')
def ISO_line():
  return render_template('ISOline.html')

@app.route('/PitchSpaceLinerity')
def PitchSpaceLinerity():
  return render_template('PitchSpaceLinerity.html')

@app.route('/PITCH')
def PITCH():
  return render_template('PITCH.html')

@app.route('/CTDLE')
def CTDLE():
  return render_template('CTDLE.html')

@app.route('/CL1B')
def CL1B():
  return render_template('CL1B.html')

@app.route('/CL3B')
def CL3B():
  return render_template('CL3B.html')

@app.route('/ISLAND')
def ISLAND():
  return render_template('ISLAND.html')

@app.route('/INVISLAND')
def INV_ISLAND():
  return render_template('INVISLAND.html')

@app.route('/download_gds')
def download_gds():
    global GDS_NAME
    path = GDS_NAME
    return send_file(path, as_attachment=True)

@app.route('/download_text')
def download_text():
    global TEXT_FILE_NAME
    path = TEXT_FILE_NAME
    return send_file(path, as_attachment=True)

if __name__=="__main__":
  #app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  app.run(host="0.0.0.0", port="5000", debug=True)