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

