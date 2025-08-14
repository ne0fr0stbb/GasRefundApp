# 📱 Gas Refund App - Easy Setup Guide

## Step-by-Step Instructions to Build and Run on Your Phone

### 🔧 **STEP 1: Install Android Studio (One-time setup)**
1. **Download Android Studio**: Go to https://developer.android.com/studio
2. **Install it** with default settings (this installs everything you need)
3. **Launch Android Studio** when done

### 📱 **STEP 2: Prepare Your Android Phone**
1. **Enable Developer Options:**
   - Go to **Settings** → **About Phone**
   - Tap **"Build Number"** 7 times (you'll see "You are now a developer!")
   
2. **Enable USB Debugging:**
   - Go back to **Settings**
   - Find **"Developer Options"** (usually under System)
   - Turn ON **"Developer Options"**
   - Turn ON **"USB Debugging"**

3. **Connect Your Phone:**
   - Connect via USB cable to your computer
   - Choose **"File Transfer"** mode on your phone
   - Allow **"USB Debugging"** when prompted (check "Always allow")

### 🏗️ **STEP 3: Open and Build the App**

#### **Method A: Using Android Studio (Recommended)**
1. **Open Android Studio**
2. Click **"Open an Existing Project"**
3. Navigate to: `C:\Users\Jason\PycharmProjects\gasrefund\GasRefundApp`
4. **Wait for Gradle sync** to complete (5-10 minutes first time)
5. **Click the green "Run" button** (▶️) at the top
6. **Select your phone** from the device list
7. **Wait for build and install** (5-10 minutes first time)

#### **Method B: Using Command Line (Alternative)**
1. **Open PowerShell** in the app directory
2. **Run these commands:**
   ```powershell
   cd "C:\Users\Jason\PycharmProjects\gasrefund\GasRefundApp"
   .\gradlew.bat assembleDebug
   .\gradlew.bat installDebug
   ```

### ✅ **STEP 4: Test the App**
1. **Look for "Gas Refund App"** on your phone's home screen or app drawer
2. **Tap to open** the app
3. **Try adding a test trip:**
   - Tap the "+" button
   - Enter a date
   - Add locations (e.g., "Chickmont" to "Guinea")
   - Enter mileage (e.g., Start: 100000, End: 100014)
   - Save the trip
4. **Generate a test report:**
   - Go back to main screen
   - Tap "Generate Report"
   - The PDF should open automatically

### 🚨 **Troubleshooting**

**If your phone isn't detected:**
- Make sure USB cable supports data transfer (not just charging)
- Try a different USB port
- Restart both Android Studio and your phone
- Check that USB Debugging is enabled

**If build fails:**
- Make sure you have a stable internet connection (downloads dependencies)
- Wait for all Gradle sync operations to complete
- Try "Build" → "Clean Project" then "Build" → "Rebuild Project"

**If app crashes:**
- Make sure your phone has Android 7.0 (API 24) or newer
- Check that you granted storage permission when prompted

### 📋 **What You'll See:**
- **Main Screen**: Summary of current month's trips and refund amount
- **Add Trip**: Easy form to add new travel entries
- **Reports**: Professional PDF reports in your Excel format
- **Auto-complete**: Common locations like Chickmont, Guinea, etc.

### 🎯 **First Time Setup Tips:**
1. **Grant permissions** when the app asks (for storage access)
2. **Add a few test trips** to see how it works
3. **Generate a test report** to verify PDF creation
4. **Check the Documents/GasRefundReports/** folder for saved PDFs

### 📞 **Need Help?**
- The app is designed to work exactly like your Excel system
- All your common locations are pre-loaded
- Reports match your current format exactly
- Data is stored locally on your phone (no internet required)

---
**You're all set! The app will streamline your travel refund process with mobile convenience while maintaining your professional reporting standards.**
