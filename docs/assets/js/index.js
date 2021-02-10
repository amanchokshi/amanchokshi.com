let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -37.814, lng: 144.96332 },
    zoom: 8,
  });
}
