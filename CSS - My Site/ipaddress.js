// Function to get the user's IP address using a free API
function getIpAddress() {
    return fetch("https://ipapi.co/json/")
        .then(response => response.json())
        .then(data => data.ip)
        .catch(error => {
            console.error("Error getting IP address:", error);
            return null;
        });
}

// Function to get the user's location using the IP address
function getLocation(ip) {
    if (!ip) {
        console.error("IP address not available.");
        return;
    }

    fetch(`https://ipapi.co/${ip}/json/`)
        .then(response => response.json())
        .then(data => {
            saveLocationToFile(data);
        })
        .catch(error => {
            console.error("Error getting location:", error);
        });
}

// Function to save location data to a text file
function saveLocationToFile(data) {
    const blob = new Blob([JSON.stringify(data)], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "location.txt";
    a.click();
}

document.getElementById("getLocationButton").addEventListener("click", async () => {
    const ip = await getIpAddress();
    getLocation(ip);
});
