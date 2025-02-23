import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "8e5000b867msh16dc983238d6080p156581jsn93394b13c745"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  
