from git import *

audio= "hardware/qcom/audio"
display= "hardware/qcom/display"
media= "hardware/qcom/media"
camera= "hardware/qcom/camera"
fm= "hardware/qcom/fm"
gps= "hardware/qcom/gps" 
power= "hardware/qcom/power"
keymaster= "hardware/qcom/keymaster"
display_caf= "hardware/qcom/display-caf/msm8996" 
media_caf= "hardware/qcom/media-caf/msm8996"
audio_caf= "hardware/qcom/audio-caf/msm8996"
mm_core= "hardware/qcom/mm-core"
msm8960= "hardware/qcom/msm8690"
display_mdss= "hardware/qcom/display-mdss"
mm_video= "hardware/qcom/mm-video"
media_v4l2= "hardware/qcom/media-v4l2"

c_audio= "https://github.com/LineageOS/android_hardware_qcom_audio.git"
c_display= "https://github.com/LineageOS/android_hardware_qcom_display.git"
c_media= "https://github.com/LineageOS/android_hardware_qcom_media.git"
c_camera= "https://github.com/LineageOS/android_hardware_qcom_camera.git"
c_fm= "https://github.com/LineageOS/android_hardware_qcom_fm.git"
c_gps= "https://github.com/LineageOS/android_hardware_qcom_gps.git"
c_power= "https://github.com/LineageOS/android_hardware_qcom_power.git"
c_keymaster= "https://github.com/LineageOS/android_hardware_qcom_keymaster.git"
c_sensors= "https://github.com/LineageOS/android_hardware_qcom_sensors.git"
c_mm_core= "https://github.com/LineageOS/android_hardware_qcom_mm-core.git"
c_msm8960= "https://github.com/LineageOS/android_hardware_qcom_msm8960.git"
c_display_mdss= "https://github.com/LineageOS/android_hardware_qcom_display-mdss.git"
c_mm_video= "https://github.com/LineageOS/android_hardware_qcom_mm-video.git"
c_media_v4l2= "https://github.com/LineageOS/android_hardware_qcom_media-v4l2.git"

b= "lineage-15.1"
bc= "lineage-15.1-caf-8996" 

ask= raw_input("clone HALs? y/n ")

if ask == "y":
   
   repo = Repo.clone_from(
    c_audio, audio,
    branch=b
   ),
   repo = Repo.clone_from(
    c_display, display,
    branch=b
   ),
   repo = Repo.clone_from(
    c_media, media,
    branch=b
   ),   
   repo = Repo.clone_from(
    c_camera, camera,
    branch=b
   ),
   repo = Repo.clone_from(
    c_fm, fm,
    branch=b
   ),
   repo = Repo.clone_from(
    c_gps, gps,
    branch=b
   ),
   repo = Repo.clone_from(
    c_power, power,
    branch=b
   ),
   repo = Repo.clone_from(
    c_keymaster, keymaster,
    branch=b
   ),
   repo = Repo.clone_from(
    c_media, media_caf,
    branch=bc
   ),
   repo = Repo.clone_from(
    c_display, display_caf,
    branch=bc
   ),
   repo = Repo.clone_from(
    c_audio, audio_caf,
    branch=bc
   )
   
   print("Cloned boi")
 
elif ask == "n":
     print("k bye")
	 
else:
   print("wrong input bhsdk")
 
print("BYE BISH")
  
