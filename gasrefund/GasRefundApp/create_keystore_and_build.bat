@echo off
echo ============================================
echo    Gas Refund App - Release Build Setup
echo ============================================
echo.

echo This script will help you create a signed APK for distribution
echo.

echo Step 1: We need to create a keystore (certificate) for signing
echo This is required for distributing Android apps
echo.

set /p STORE_PASSWORD=Enter a password for your keystore (remember this!): 
set /p KEY_ALIAS=Enter key alias (or press Enter for 'chickmont'): 
if "%KEY_ALIAS%"=="" set KEY_ALIAS=chickmont

echo.
echo Creating keystore...
keytool -genkeypair -v -keystore chickmont-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias %KEY_ALIAS%

echo.
echo Creating gradle.properties file for signing...
echo MYAPP_RELEASE_STORE_FILE=../chickmont-keystore.jks > app\gradle.properties
echo MYAPP_RELEASE_KEY_ALIAS=%KEY_ALIAS% >> app\gradle.properties
echo MYAPP_RELEASE_STORE_PASSWORD=%STORE_PASSWORD% >> app\gradle.properties
echo MYAPP_RELEASE_KEY_PASSWORD=%STORE_PASSWORD% >> app\gradle.properties

echo.
echo Now building signed release APK...
gradlew assembleRelease

echo.
echo ============================================
echo SUCCESS! Your signed APK is ready at:
echo app\build\outputs\apk\release\app-release.apk
echo.
echo You can now share this APK file with your colleagues!
echo File size should be around 10-15MB
echo ============================================
echo.
echo IMPORTANT: Keep the file 'chickmont-keystore.jks' safe!
echo You need it for any future updates to the app.
echo ============================================
pause
