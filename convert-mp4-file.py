import cv2

# 入力ビデオ名
input_video_name = "input_video.mp4"
# 出力ビデオ名
output_video_name = "output_video.mp4"
# 幅の指定
new_width = 500
# フレームレートの指定
new_fps = 30

video = cv2.VideoCapture(input_video_name)

# フレームレートの確認
fps_setting = video.get(cv2.CAP_PROP_FPS)
print("FPS(Setting):", '{:11.02f}'.format(fps_setting))

# ビデオの高さと幅を取得
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# アスペクト比を保ったまま高さを計算
new_height = int(height * (new_width / width))

# リサイズ後のビデオを保存するためのオブジェクトを作成
output_video = cv2.VideoWriter(
    output_video_name,
    cv2.VideoWriter_fourcc(*'mp4v'),
    new_fps,
    (new_width, new_height)
)

# ビデオをフレームごとに読み込んでリサイズし、新しいビデオに書き込み
while True:
    ret, frame = video.read()
    if not ret:
        break
    resized_frame = cv2.resize(frame, (new_width, new_height))
    output_video.write(resized_frame)

# ビデオを閉じてリソースを解放
video.release()
output_video.release()
