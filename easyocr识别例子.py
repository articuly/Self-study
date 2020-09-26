import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])
# 路经不能有中文
result = reader.readtext("picture/20200325234858.png", detail=0)
print(result)
