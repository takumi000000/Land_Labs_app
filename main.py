import bpy
from path import model_path, output_image

# --- 設定 ---
MODEL_PATH = model_path()
OUTPUT_IMAGE = output_image()
ORTHO_SCALE = 20.0
RESOLUTION = 1024

# シーンの初期化
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# モデルインポート
bpy.ops.import_scene.fbx(filepath=MODEL_PATH)

# カメラ作成
camera_data = bpy.data.cameras.new("OrthoCamera")
camera_data.type = 'ORTHO'
camera_data.ortho_scale = ORTHO_SCALE
camera_obj = bpy.data.objects.new("OrthoCamera", camera_data)
bpy.context.scene.collection.objects.link(camera_obj)
# カメラ位置を真上から見下ろす (Z 軸方向)
camera_obj.location = (0.0, 0.0, 10.0)
camera_obj.rotation_euler = (3.14159/2.0, 0, 0)

# シーンにカメラ設定
bpy.context.scene.camera = camera_obj
bpy.context.scene.render.resolution_x = RESOLUTION
bpy.context.scene.render.resolution_y = RESOLUTION
bpy.context.scene.render.filepath = OUTPUT_IMAGE

# レンダリング
bpy.ops.render.render(write_still=True)
print("オルソ画像の作成が完了しました", OUTPUT_IMAGE)
