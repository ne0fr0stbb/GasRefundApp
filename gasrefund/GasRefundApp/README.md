# Gas Refund Android App

A mobile application designed to replicate the functionality of your Excel-based gas refund tracking system for **Chickmont Foods Ltd**. This app allows you to track business travel, calculate refunds, and generate professional PDF reports in the same format as your current Excel sheets.

## Features

### ✅ Core Functionality
- **Trip Entry**: Add and edit travel entries with date, locations, mileage, and reasons
- **Automatic Calculations**: Auto-calculate distance and refund amounts
- **Monthly Summaries**: View current month totals and refund amounts
- **PDF Report Generation**: Generate reports matching your Excel format exactly
- **Data Persistence**: Local SQLite database storage with Room

### ✅ User Experience
- **Material Design 3**: Modern, clean interface following Android design guidelines
- **Intuitive Navigation**: Easy-to-use forms with validation and auto-completion
- **Smart Defaults**: Pre-populated locations and vehicles based on your usage patterns
- **Offline Capable**: Works completely offline with local data storage

### ✅ Report Features
- **Exact Excel Format**: Matches your current "Travel Refund" layout
- **Company Branding**: Includes "Chickmont Foods Ltd" header and formatting
- **Professional Output**: PDF reports with proper signatures lines and totals
- **Easy Sharing**: Share reports via email or other apps

## App Structure

### Database Schema
- **TravelEntry**: Stores individual trip records
- **Vehicle**: Manages company vehicles (L3274, etc.)
- **Location**: Common locations with usage tracking for auto-completion

### Key Components
- **MainActivity**: Dashboard with monthly summary and trip list
- **AddTripActivity**: Add/edit individual trips
- **ReportActivity**: Generate and share PDF reports
- **PDFReportGenerator**: Creates PDF reports matching Excel format
- **TravelEntryViewModel**: Manages data and business logic

## Pre-loaded Data

The app comes with your commonly used locations pre-populated:
- Chickmont (highest usage)
- Guinea
- Oldbury
- Brighthall
- K&E
- Ridge
- Ellesmere
- Hatchery
- ZRS
- D.E Computers
- Rainforest Swan Street

Default vehicle: **L3274**

## Report Output

Generated PDF reports include:
- **Header**: "CHICKMONT FOODS LTD" / "TRAVEL REFUND"
- **Employee Info**: "NAME: JASON BURNHAM" / "VEHICLE: L3274"
- **Trip Table**: Date, From/To Description, Mileage, Distance, Manager's Initial, Reason
- **Summary**: Total distance, rate per km (configurable, default $2.00), refund due
- **Signatures**: Employee signature, Manager's signature, and date lines

## Installation & Setup

### Prerequisites
- Android Studio Arctic Fox or later
- Android SDK API Level 24+ (Android 7.0)
- Kotlin support

### Build Instructions
1. Open Android Studio
2. Click "Open an Existing Project"
3. Navigate to the `GasRefundApp` folder and select it
4. Wait for Gradle sync to complete
5. Connect an Android device or start an emulator
6. Click "Run" to build and install the app

### Permissions Required
- **Storage**: To save PDF reports to external storage
- **Location** (optional): For potential future GPS integration

## Usage Guide

### Adding a Trip
1. Tap the "+" button or "Add Trip"
2. Select the date (defaults to today)
3. Enter from/to locations (auto-completes from frequent locations)
4. Input start and end mileage (distance calculates automatically)
5. Select vehicle (defaults to L3274)
6. Add reason (optional)
7. Tap "Save Trip"

### Generating Reports
1. From the main screen, tap "Generate Report"
2. The app will create a PDF for the current month
3. Reports are saved to Documents/GasRefundReports/
4. The PDF automatically opens for viewing
5. Share via email or other apps

### Data Management
- All data is stored locally on your device
- The app automatically tracks location usage for better auto-completion
- Edit trips by tapping on them from the main list
- Monthly totals update automatically

## Technical Details

### Architecture
- **MVVM Pattern**: Clean separation of concerns
- **Room Database**: Local SQLite database with type-safe queries  
- **LiveData**: Reactive data updates for UI
- **Coroutines**: Async operations for database and PDF generation
- **Material Design**: Modern UI components and theming

### Libraries Used
- **Android Jetpack**: Room, LiveData, ViewModel, Navigation
- **Material Components**: UI components and theming
- **iText PDF**: Professional PDF generation
- **Kotlin Coroutines**: Asynchronous programming

## Customization

### Rate Per Kilometer
- Default: $2.00 per km (matches your recent Excel sheets)
- Can be modified in the TravelEntryViewModel

### Company Information
- Company name, employee name, and default vehicle can be updated in the strings.xml file
- PDF formatting can be modified in PDFReportGenerator.kt

### Locations
- The app learns from your usage and ranks locations by frequency
- You can add new locations by typing them in the trip entry form
- Pre-loaded locations match those from your Excel analysis

## Future Enhancements

Potential features for future versions:
- **GPS Integration**: Auto-populate mileage from GPS tracking
- **Multiple Employees**: Support for different staff members
- **Cloud Backup**: Sync data across devices
- **Receipt Photos**: Attach photos to trip entries
- **Advanced Reports**: Custom date ranges and filtering
- **Export/Import**: Backup data to Excel/CSV

## Support

This app replicates your exact Excel workflow but provides the convenience of mobile entry and professional PDF generation. The database structure allows for easy data export if needed, and the PDF format matches your current reporting requirements exactly.

For customizations or issues, refer to the source code comments or Android development documentation.

---

**Built for Jason Burnham - Chickmont Foods Ltd**  
*Streamlining your travel refund process with mobile convenience*
