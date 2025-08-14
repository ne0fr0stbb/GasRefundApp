@echo off
echo ============================================
echo    EMERGENCY FIX: Rebuilding Gas Refund App
echo ============================================
echo.

echo Step 1: Cleaning old generated files...
gradlew clean

echo.
echo Step 2: Rebuilding with Room database generation...
gradlew assembleDebug --info

echo.
echo Step 3: Checking if Room implementation was generated...
if exist "app\build\generated\source\ksp\debug\kotlin\com\jasonburnham\gasrefundapp\data" (
    echo ✅ SUCCESS: Room database implementation generated with KSP!
    echo.
    echo The app should now run without crashing.
    echo You can now install it on your device.
) else (
    echo ❌ ISSUE: Room files not generated properly.
    echo Please try opening in Android Studio and:
    echo 1. Build → Clean Project  
    echo 2. Build → Rebuild Project
)

echo.
echo ============================================
echo Rebuild complete! Try running the app now.
echo ============================================
pause
