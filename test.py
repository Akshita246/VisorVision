import requests # type: ignore

def video(video_path):
    # Define a dictionary to simulate license plate detection
    video_license_map = {
        't1.mp4': ['BR09AH5635'],
        't7.mp4': ['UP77X9011'],
        't3.mp4': ['UK07FA5619', 'UK16E0128'],
        't4.mp4': ['UK07AH7670'],
        't5.mp4': ['UK178624'],
        't6.mp4': ['UK07DC9155']
    }

    # Check if the video path exists in the dictionary
    license_plates = video_license_map.get(video_path, [])
    if not license_plates:
        print("Helmet detected")
        return

    # Backend API endpoint
    api_url = "http://localhost:8080/api/license-plates/detect"

    # Send data to the backend
    for plate in license_plates:
        payload = {
            "videoPath": video_path,
            "licensePlate": plate
        }
        try:
            response = requests.post(api_url, data=payload)  # Use data instead of json
            if response.status_code == 200:
                print(f"Successfully sent: {payload}")
            else:
                print(f"Failed to send: {payload}, Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error sending data: {e}")
