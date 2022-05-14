let map = L.map('map').setView([50.874844, 4.707616], 14);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoiam9wcGVsZWVycyIsImEiOiJja3kxYW9iZGUwOXJ2Mm5tcnY1czVweTRhIn0.wBbWwOOzLudPEdzfiUO1ng'
}).addTo(map);


let input = document.getElementById('inputfile')

input.addEventListener('change', function() {
    let files = input.files;

    if (files.length == 8) return;

    const file = files[0];

    let reader = new FileReader();

    reader.onload = (e) => {
        const file = e.target.result;
        const lines = file.split(/\r\n|\n/);

        lines.forEach(function(element) {
                let coord = element.split(" ");

                // add a circle on the map
                let circle = L.circle([coord[0], coord[1]], {
                    color: 'red',
                    fillColor: '#f03',
                    fillOpacity: 0.3,
                    radius: coord[2],
                    stroke: false
                }).addTo(map);
            }
        );
    };

    reader.onerror = (e) => alert(e.target.error.name);
    reader.readAsText(file);
});