// Do nothing
function doNothing() {
}

function initialize() {

    // Google Maps
    var mapOptions = {
        center: new google.maps.LatLng(52.2, 20),
        zoom: 7,
        disableDefaultUI: false,
        scaleControl: false,
        zoomControl: true,
        panControl: true,
        streetViewControl: true,
        overviewMapControl: true,
        mapTypeControl: true,
        mapTypeControlOptions: {
            mapTypeIds: [
                google.maps.MapTypeId.ROADMAP,
                google.maps.MapTypeId.SATELLITE,
                google.maps.MapTypeId.HYBRID,
                google.maps.MapTypeId.TERRAIN,
                'Open Street Map'
            ],
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
            position: google.maps.ControlPosition.TOP_CENTER
        }
    };
    var map = new google.maps.Map(document.getElementById('map'),mapOptions);

    // Open Street Map
    var osm = new google.maps.ImageMapType({
        getTileUrl: function(coord, zoom) {
            return "http://tile.openstreetmap.org/" + zoom + "/" + coord.x + "/" + coord.y + ".png";
        },
        tileSize: new google.maps.Size(256, 256),
        isPng: true,
        maxZoom: 19,
        minZoom: 0,
        name: "Open Street Map"
    });
    map.mapTypes.set('Open Street Map', osm);

    // Markers
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            var markers = JSON.parse(xmlhttp.responseText);
            for (var i = 0; i < markers.length; i++) {
                var address = markers[i].fields.address
                var city = markers[i].fields.city
                var city_district = markers[i].fields.city_district
                var county = markers[i].fields.county
                var created_date = markers[i].fields.created_date
                var geometry = markers[i].fields.geometry
                var house_number = markers[i].fields.house_number
                var lattitude = markers[i].fields.lattitude
                var longtitude = markers[i].fields.longtitude
                var max_speed = markers[i].fields.max_speed
                var neighbourhood = markers[i].fields.neighbourhood
                var note = markers[i].fields.note
                var osm_url = markers[i].fields.osm_url
                var postcode = markers[i].fields.postcode
                var ref = markers[i].fields.ref
                var road = markers[i].fields.road
                var state = markers[i].fields.state
                var suburb = markers[i].fields.suburb
                var type = markers[i].fields.type

                var marker = new google.maps.Marker({
                    map: map,
                    position: new google.maps.LatLng(lattitude, longtitude)
                });

            }
        }
    }
    xmlhttp.open("GET", "/ajax", true);
    xmlhttp.send();

}

google.maps.event.addDomListener(window, 'load', initialize);





