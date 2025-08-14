# Google Sign-In Setup Instructions

To enable Google Sign-In functionality in the Gas Refund App, you need to set up Firebase and Google Cloud Console:

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Create a project" or "Add project"
3. Enter project name: "Gas Refund App" (or your preferred name)
4. Enable Google Analytics if desired
5. Click "Create project"

## Step 2: Add Android App to Firebase

1. In Firebase Console, click "Add app" and select Android
2. Enter package name: `com.jasonburnham.gasrefundapp`
3. Enter app nickname: "Gas Refund App"
4. Leave SHA-1 certificate fingerprint blank for now (for development)
5. Click "Register app"

## Step 3: Download google-services.json

1. Download the `google-services.json` file
2. Place it in the `app/` directory of your Android project
3. The file should be at: `app/google-services.json`

## Step 4: Get Web Client ID

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Go to "APIs & Services" > "Credentials"
4. Find the "Web client (auto created by Google Service)" credential
5. Copy the "Client ID" value

## Step 5: Update App Configuration

1. Open `app/src/main/res/values/strings.xml`
2. Replace `YOUR_WEB_CLIENT_ID_HERE` with the actual Web Client ID from Step 4:
   ```xml
   <string name="default_web_client_id">123456789-abcdefghijklmnop.apps.googleusercontent.com</string>
   ```

## Step 6: Enable Authentication

1. In Firebase Console, go to "Authentication"
2. Click "Get started"
3. Go to "Sign-in method" tab
4. Enable "Google" provider
5. Set support email
6. Save changes

## Step 7: Generate Debug SHA-1 (Optional for Development)

To get better debugging and testing:

1. Open terminal/command prompt
2. Navigate to your Android SDK location
3. Run (on Windows):
   ```bash
   keytool -list -v -keystore "%USERPROFILE%\.android\debug.keystore" -alias androiddebugkey -storepass android -keypass android
   ```
4. Copy the SHA1 fingerprint
5. In Firebase Console, go to Project Settings > Your App
6. Add the SHA-1 fingerprint

## Step 8: Test the App

1. Build and run the app
2. You should see the login screen first
3. Click "Sign in with Google"
4. Complete the Google sign-in flow
5. You should be redirected to the main app

## Troubleshooting

- Make sure `google-services.json` is in the `app/` folder
- Verify the package name matches exactly
- Check that the Web Client ID is correct
- Ensure Firebase Authentication is enabled with Google provider
- For production, add your release SHA-1 fingerprint

## Security Notes

- The `google-services.json` file contains API keys but is safe to include in version control for mobile apps
- The Web Client ID is also safe to be public in mobile apps
- Firebase security rules will protect your backend data
