import librosa
import numpy as np

def audio_to_spectrogram(audio_path, n_mels=64, duration=3, sr=16000):
    """
    تحويل ملف WAV إلى مصفوفة نيمباي (Spectrogram) قابلة للإدخال في النموذج.
    """
    # 1. تحميل الصوت بمعدل عينة موحد
    y, sr = librosa.load(audio_path, sr=sr, duration=duration)
    
    # 2. التأكد من طول الملف (Padding)
    target_length = sr * duration
    if len(y) < target_length:
        y = np.pad(y, (0, target_length - len(y)))
    
    # 3. استخراج الـ Mel-spectrogram
    # ملاحظة: قيم hop_length و n_fft يجب أن تطابق ما تم استخدامه في التدريب
    spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, 
                                          n_fft=1024, hop_length=512)
    
    # 4. التحويل لمقياس الديسيبل اللوغاريتمي
    spec_db = librosa.power_to_db(spec, ref=np.max)
    
    # 5. التقييس (Normalization) ليكون بين 0 و 1
    spec_norm = (spec_db - spec_db.min()) / (spec_db.max() - spec_db.min())
    
    return spec_norm
