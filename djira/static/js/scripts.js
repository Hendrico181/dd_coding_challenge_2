const weatherApiUrl = "https://api.openweathermap.org/data/2.5/weather";
const apiKey = "c17f80b8977a3ca05b570bd7a5b8679c";
const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0,
};

function success(pos) {
  const crd = pos.coords;
  const lat = crd.latitude;
  const long = crd.longitude;

  const url = `${weatherApiUrl}?lat=${lat}&lon=${long}&appid=${apiKey}&units=metric`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const weatherDiv = document.getElementById("weather");
      const weatherIcon = `https://openweathermap.org/img/w/${data.weather[0].icon}.png`;
      const weatherInfo = `${data.main.temp}°C <br> The weather condition is ${data.weather[0].description}.<br>If only you could take notes...`;
      weatherDiv.innerHTML = `<img src="${weatherIcon}" alt="Weather icon" style="width: 100px; height: 100px;"> ${weatherInfo}`;
    })
    .catch((error) => console.log(error));
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

navigator.geolocation.getCurrentPosition(success, error, options);

console.log(111);