[app]
title = Verification App
package.name = checkapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1

# REQUIREMENTS - Faqat eng asosiylari
requirements = python3,kivy==2.2.1,requests,certifi,urllib3

orientation = portrait
fullscreen = 0

# ANDROID SOZLAMALARI
android.permissions = INTERNET, CAMERA, RECORD_AUDIO
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
