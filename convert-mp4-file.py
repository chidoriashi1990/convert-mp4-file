import cv2

basefilename = "sample.mp4"

# 入力動画ファイル名
input_file = basefilename

# 出力動画ファイル名
output_file = "output-" + basefilename

# 入力動画ファイルを開く
cap = cv2.VideoCapture(input_file)

# 動画のFPSを取得
fps = cap.get(cv2.CAP_PROP_FPS)

# 出力動画のFPSを設定
output_fps = 5

# 出力動画のフレームサイズを設定
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 出力動画のコーデックを設定
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# 出力動画ファイルを作成
out = cv2.VideoWriter(output_file, fourcc, output_fps, (frame_width, frame_height))

# フレームカウンターの初期化
frame_count = 0

# フレームが読み込める限りループ
while cap.isOpened():
    # フレームを読み込む
    ret, frame = cap.read()

    if not ret:
        break

    # 30fpsから5fpsに間引く
    if frame_count % int(fps / output_fps) == 0:
        # フレームを出力動画に書き込む
        out.write(frame)

    # フレームカウンターを増やす
    frame_count += 1

    # キーボード入力を待機し、'q'が押されたらループを終了する
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# メモリを解放する
cap.release()
out.release()

# ウィンドウを全て閉じる
cv2.destroyAllWindows()
