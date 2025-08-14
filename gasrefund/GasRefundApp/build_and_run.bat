@echo off
echo ============================================
echo    Building Gas Refund Android App
echo ============================================
echo.

echo Checking for connected devices...
adb devices

echo.
echo Building the app...
gradlew assembleDebug

echo.
echo Installing on connected device...
gradlew installDebug

echo.
echo ============================================
echo Build complete! Check your phone for the app.
echo ============================================
pause
