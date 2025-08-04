from datetime import datetime

today = datetime.now().strftime("%m%d")

MAPS = {
"SPC_Convective_Outlook": f"https://www.spc.noaa.gov/products/outlook/day1otlk_{today}.gif",
"SPC_Fire_Weather": f"https://www.spc.noaa.gov/products/fire_wx/fwdy1otlk_{today}.gif",
"AirNow_FireSmoke": "https://fire.airnow.gov/images/fwsmoke.png" # Static fallback, may need screenshot logic
}
