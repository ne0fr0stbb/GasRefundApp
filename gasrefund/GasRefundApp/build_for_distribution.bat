@echo off
echo ============================================
echo    Building Gas Refund App for Distribution
echo ============================================
echo.

echo Building release APK...
gradlew assembleRelease

echo.
echo APK built! Location:
echo app\build\outputs\apk\release\app-release.apk
echo.

echo You can now share this APK file with your colleagues!
echo They need to:
echo 1. Enable "Install from Unknown Sources" in their phone settings
echo 2. Download and install the APK file
echo.

echo ============================================
echo Distribution APK ready!
echo ============================================
pause
