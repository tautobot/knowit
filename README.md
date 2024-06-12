# knowit

# Install instruction
1. Install pyenv
```
brew install pyenv
brew update
brew upgrade pyenv
pyenv install <python version>
```
2. Install python and set global/local python version
```
pyenv install 3.9.11
pyenv global 3.9.11
pyenv local 3.9.11
pyenv virtualenv 3.9.11 .venv
```
3. Activate and deactivate .venv
```
pyenv shell 3.9.11
python -m venv .venv
```
4. Install pipenv
```
pip install pipenv
pipenv activate
pipenv deactivate
```
5. Install Appium (follow guide from this link) and Check to make sure appium is installed, run this cmd on terminal
    `appium` to check if installed version
    
    eg.
    [Appium] Welcome to Appium v1.21.0
    [Appium] Appium REST http interface listener started on 0.0.0.0:4723
    
    Sample code: https://appium.io/docs/en/latest/quickstart/test-py/
    To upgrade `npm update -g appium`
    Download Appium Server: https://github.com/appium/appium-desktop/releases
    Download Appium Inspector: https://appium.github.io/appium-inspector/latest/quickstart/installation/#macos
    Install driver: `xcodebuild -version && sw_vers && rm -rf ~/.appium && npm install -g appium@next && appium driver install xcuitest && appium --allow-cors`
    
    Install Plugins: `appium --use-plugins=<plugin-name>`    

    Real Device Config: 
        https://appium.github.io/appium-xcuitest-driver/latest/preparation/real-device-config/
        Enable Developer Mode: https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device
        `appium driver run xcuitest open-wda`
        It is possible to build WebDriverAgentRunner for a generic iOS/iPadOS/tvOS device, and install the generated .app package to a real device.
        # iOS/iPadOS
        `xcodebuild clean build-for-testing -project WebDriverAgentRunner.xcodeproj -derivedDataPath appium_wda_ios -scheme WebDriverAgentRunner -destination generic/platform=iOS CODE_SIGNING_ALLOWED=YES`

6. Install Android Studio and Emulator (for Android)
    ref. https://www.alphr.com/run-android-emulator/
    Install driver: `xcodebuild -version && sw_vers && rm -rf ~/.appium && npm install -g appium@next && appium driver install uiautomator2 && appium --allow-cors`
    start `emulator -avd <device-name>`, e.g `emulator -avd emulator-5554 --allow-cors`
    stop `adb -s emulator-5554 emu kill` or `adb devices | grep emulator | cut -f1 | while read line; do adb -s $line emu kill; done`

7. Install iOS simuator (only for MAC OS)
    ref. https://www.kindacode.com/article/how-to-install-an-ios-simulator-in-xcode/
    view devices list `xcrun simctl list` 
    Now you should be able to use simctl to install and launch commands.
        xcrun simctl install <YOUR-DEVICE-ID> <PATH-TO-APPLICATION-BUNDLE>
        xcrun simctl launch <YOUR-DEVICE-ID> <BUNDLE-ID-OF-APP-BUNDLE>
    start `open -a Simulator`, start with specific identifier `open -a Simulator --args -CurrentDeviceUDID <YOUR-DEVICE-ID>`
    stop `killall Simulator`
    
8. Install for aq with iOS reeal device
    This allows Appium to complete certain operations since the Apple apps do not easily enable programmatic use.
    `pipenv install libimobiledevice`
    This package will allow you to transfer iOS apps onto your device
    `pipenv install ios-deploy`  # pipenv uninstall ios-deploy, then brew install ios-deploy if RuntimeError: Failed to lock Pipfile.lock!
    Appium will automatically build the WDA app. Since WDA requires a dependency manager for iOS called Carthage, we will need to install this to enable the WDA bootstrap process.
    `pipenv install carthage`    # pipenv uninstall ios-deploy, then brew install carthage if RuntimeError: Failed to lock Pipfile.lock!
    ref. https://medium.com/@abhaykhs/using-appium-to-run-ios-tests-on-real-devices-fabd9850a06a
```
