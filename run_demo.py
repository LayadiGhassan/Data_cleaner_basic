import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from utils import audio_to_spectrogram

# إعداد المسارات
MODEL_PATH = 'models/final.h5'
AUDIO_INPUT = 'input_audio/test_voice.wav'
OUTPUT_PATH = 'outputs/result_face.png'

def run():
    print("--- جاري تحميل النموذج... قد يستغرق ذلك لحظات ---")
    model = load_model(MODEL_PATH, compile=False)
    
    print(f"--- جاري معالجة الملف الصوتي: {AUDIO_INPUT} ---")
    # تحويل الصوت لـ spectrogram
    spec = audio_to_spectrogram(AUDIO_INPUT)
    
    # تجهيز الأبعاد للنموذج (1, Height, Width, 1)
    input_data = np.expand_dims(spec, axis=0)
    input_data = np.expand_dims(input_data, axis=-1)
    
    print("--- جاري التنبؤ بالوجه... ---")
    prediction = model.predict(input_data)
    
    # معالجة النتيجة (بافتراض أن النموذج يخرج صورة مباشرة)
    # إذا كان يخرج Embedding، ستحتاج لخطوة إضافية للمقارنة
    face_img = prediction[0]
    
    # حفظ النتيجة
    if not os.path.exists('outputs'): os.makedirs('outputs')
    plt.imsave(OUTPUT_PATH, face_img)
    
    print(f"--- تم بنجاح! يمكنك رؤية النتيجة في: {OUTPUT_PATH} ---")
    plt.imshow(face_img)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    run()
