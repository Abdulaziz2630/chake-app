[app]
title = Verification
package.name = verify
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 1.0
requirements = python3,kivy==2.2.1,requests,urllib3,certifi,idna,chardet
android.permissions = INTERNET, CAMERA, RECORD_AUDIO
android.api = 31
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2