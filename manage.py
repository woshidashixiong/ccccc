from PIL import Image
import io

# 打开AI文件
with open('example.ai', 'rb') as f:
    ai_data = f.read()

# 将AI文件转换为PNG格式
with Image.open(io.BytesIO(ai_data)) as im:
    im.save('example.png', 'PNG')
