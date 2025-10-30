import os
import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import (
    MyVideoCapture,
)


def process_image(captured_frame: np.ndarray):
    """
    メモリ上のキャプチャフレームとgoogle.pngを合成し、結果をファイルに保存する処理。

    パラメータ:
        captured_frame (np.ndarray): カメラで取得したフレーム画像
    """
    # スクリプトのディレクトリを取得
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 1階層上のディレクトリ（プロジェクトルート想定）
    parent_dir = os.path.dirname(script_dir)

    # 画像ファイルへのフルパスを作成
    google_path = os.path.join(parent_dir, "images", "google.png")  # 合成元の画像
    output_dir = os.path.join(parent_dir, "images")  # 保存先ディレクトリ
    output_path = os.path.join(
        output_dir, "output_google_replace.png"
    )  # 保存ファイル名

    # google.pngを読み込む
    google_img = cv2.imread(google_path)

    if google_img is None:
        print("⚠️ Google画像が読み込めません。パスを確認してください。")
        print(f"Google画像パス: {google_path}")
        return  # 画像が読み込めなければ処理中止

    # キャプチャ画像としてメモリ上のフレームを使用
    capture_img = captured_frame

    # --- 画像加工処理 ---
    output_img = google_img.copy()  # 加工用にコピー
    g_height, g_width, _ = google_img.shape  # Google画像の高さ・幅
    c_height, c_width, _ = capture_img.shape  # キャプチャ画像の高さ・幅

    print("Google画像サイズ:", google_img.shape)
    print("キャプチャ画像サイズ:", capture_img.shape)

    # Google画像の各ピクセルを走査
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]  # BGR値取得
            # 白い部分をキャプチャ画像で置換
            if b > 250 and g > 250 and r > 250:
                # キャプチャ画像をタイリング（繰り返し）して貼り付け
                cx = x % c_width
                cy = y % c_height
                output_img[y, x] = capture_img[cy, cx]

    # 出力ディレクトリを作成（存在しない場合）
    os.makedirs(output_dir, exist_ok=True)
    # 画像を保存
    result = cv2.imwrite(output_path, output_img)

    print("--- 処理結果 ---")
    print("加工後の保存結果:", result)
    print(f"画像を保存しました → {output_path}")

    # 加工結果を画面にも表示
    cv2.imshow("Processed Image", output_img)
    cv2.waitKey(0)  # 任意のキー入力で閉じる
    cv2.destroyAllWindows()


def k24122():
    """
    カメラキャプチャを行い、取得したフレームを画像合成処理に渡すメイン関数
    """
    # 1. MyVideoCaptureを実行 (qキーでフレームが app.captured_img に保存される)
    app = MyVideoCapture()
    app.run()  # カメラウィンドウを表示してフレーム取得

    # 2. get_img() メソッドを使って、キャプチャされたフレームを取得
    captured_frame = app.get_img()

    # 3. フレームが正常に取得できた場合のみ画像加工を実行
    if captured_frame is not None:
        print("\nカメラキャプチャを終了しました。画像加工を開始します。")
        process_image(captured_frame)  # メモリ上のフレームを渡す
    else:
        # qキー以外（例: ウィンドウのXボタン）で終了した場合
        print(
            "\n⚠️ キャプチャされたフレームがありませんでした。qキーを押して終了してください。画像加工はスキップします。"
        )


if __name__ == "__main__":
    k24122()  # メイン関数実行
