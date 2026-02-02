from ultralytics import YOLO
import torch
import os
from ultralytics import YOLO
import torch

# إعداد GPU
device = 0 if torch.cuda.is_available() else 'cpu'

# 1. تغيير الموديل لـ Small (أخف وأسرع)
model = YOLO('yolov8s.pt') 

print("🚀 Starting Optimized Training...")

results = model.train(
    data='formal_data_absolute.yaml',
    name='formal_wear_small_fast',
    
    # --- تعديلات السرعة ---
    epochs=50,             # 50 دورة كافية جداً للموديل الـ Small
    patience=10,           # لو مفيش تحسن في 10 دورات اقفل
    batch=16,              # الـ Small يسمح بباتش أكبر (أسرع في التدريب)
    imgsz=512,             # تصغير الصورة قليلاً لتسريع الكارت (بدل 640)
    cache=True,            # تحميل الصور في الرامات للسرعة القصوى
    workers=4,
    device=device,
    
    # --- الاحتفاظ بالتحسينات ---
    augment=True,
    hsv_v=0.4,             # تغيير الإضاءة مهم
    degrees=10.0,
    fliplr=0.5
)

print("✅ Done! Saved in runs/detect/formal_wear_small_fast/weights/best.pt")


from ultralytics import YOLO

# 1. تحميل أفضل نسخة وصل لها الموديل
# تأكدي أن المسار صحيح كما فعلنا سابقاً
model = YOLO('C:/runs/detect/formal_wear_small_fast/weights/best.pt')

# 2. تشغيل اختبار الدقة على بيانات الاختبار (Validation Set)
metrics = model.val()

# 3. طباعة النتائج بشكل مقروء
print(f"Mean Average Precision (mAP50): {metrics.box.map50:.3f}")
print(f"Precision: {metrics.box.mp:.3f}")
print(f"Recall: {metrics.box.mr:.3f}")