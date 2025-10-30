import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def k24036():
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # カメラ画像を取得
    capture_img: cv2.Mat = app.get_img()
    if capture_img is None:
        print("カメラ画像が取得できませんでした。")
        return

    # Google検索画面画像を読み込み
    google_img: cv2.Mat = cv2.imread('images/google.png')
    if google_img is None:
        print("google.png が見つかりません。")
        return

    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape

    print("google.png:", google_img.shape)
    print("capture_img:", capture_img.shape)

    # 白色部分をキャプチャ画像で置き換える（グリッド状）
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                # キャプチャ画像を繰り返し利用
                google_img[y, x] = capture_img[y % c_height, x % c_width]

    # 結果を保存
    output_filename = 'lecture05_01_K24036.png'
    cv2.imwrite(output_filename, google_img)
    print(f"{output_filename} を保存しました。")