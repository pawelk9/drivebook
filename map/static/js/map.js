$(document).ready(function () {
    initMap();
});

// Global variables
var map;

function initMap() {

    var map = L.map('map').setView([52.2, 19], 7);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: 'pawelk9.cifcs0oy500bxt0lx37ssd3m5',
        accessToken: 'pk.eyJ1IjoicGF3ZWxrOSIsImEiOiJjaWZjczBwNTUwMGExdWVseXBmdHVnaDE5In0.BS4MuI49zQxh8feq64a2bQ'
    }).addTo(map);

    // Geolocation
    map.locate({setView: true, maxZoom: 16});

    // Custom icons
    var speedDevice = L.icon({
        iconUrl: '/static/img/speed_camera_stationary.png',
        iconSize: [32, 26]
    });

    // Add markers
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        var marker = [];
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            var markers = JSON.parse(xmlhttp.responseText);
            for (var i = 0; i < markers.length; i++) {
                marker[i] = new L.marker([markers[i].fields.lattitude, markers[i].fields.longtitude], {
                name: '<img src="/static/img/speed_camera_header.png" class="img-responsive" alt="Fotoradar">',
                icon: speedDevice,
                postcode: markers[i].fields.postcode,
                type: markers[i].fields.type
                });
                marker[i].addTo(map);
                marker[i].on('click', onClick);
            }
        }
    }
    xmlhttp.open("GET", "/ajax", true);
    xmlhttp.send();
}

// Click event
function onClick(e) {
    $(".marker-name").html(this.options.name);
}