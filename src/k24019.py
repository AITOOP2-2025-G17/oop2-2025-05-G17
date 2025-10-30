import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def  k24019():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    capture_img : cv2.Mat = app.get_img()  # カメラからキャプチャした画像を取得

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            b, g, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # カメラ画像を(0,0)からグリッド状に並べる
                # カメラ画像のどの位置の画素を使うかを計算
                cam_x = x % c_width
                cam_y = y % c_hight
                # google画像の白い部分をカメラ画像で置き換え
                google_img[y, x] = capture_img[cam_y, cam_x]

    # 書き込み処理
    cv2.imwrite('output_images/lecture05_01_K24019.png', google_img)
    print("画像を保存しました: output_images/lecture05_01_K24019.png")