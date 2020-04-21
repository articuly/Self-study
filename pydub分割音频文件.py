from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file(r"E:\Downloads\mm.wav", "wav")
chunk_length_ms = 1000 * 60  # 分块的毫秒数
chunks = make_chunks(myaudio, chunk_length_ms)  # 将文件切割成1秒每块

# 保存切割的音频到文件
for i, chunk in enumerate(chunks):
    chunk_name = r".\audio\chunk{0:0>3d}.wav".format(i)
    print("exporting...", chunk_name)
    chunk.export(chunk_name, format="wav")
