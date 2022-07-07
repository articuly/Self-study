from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file(r"C:\Users\ASL\lcqqdwjdbjyj.aac", "aac")
chunk_length_ms = 22000 * 600  # 分块的毫秒数
chunks = make_chunks(myaudio, chunk_length_ms)  # 将文件切割成1秒每块

# 保存切割的音频到文件
for i, chunk in enumerate(chunks):
    chunk_name = r".\audio\财经历史《两次全球大危机的比较研究》{0:0>2d}.aac".format(i)
    print("exporting...", chunk_name)
    chunk.export(chunk_name, format="adts")
