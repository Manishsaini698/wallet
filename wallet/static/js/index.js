let foo;

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4.5,
        center: {
            lat: 20.5937,
            lng: 78.9629
        }
    });
    foo = map
    var geocoder = new google.maps.Geocoder();

    document.getElementById('submit').addEventListener('click', function() {
        geocodeAddress(geocoder, map);
    });
}

function geocodeAddress(geocoder, resultsMap) {
    var address = document.getElementById('address').value;
    geocoder.geocode({
        'address': address
    }, function(results, status) {
        if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: resultsMap,
                position: results[0].geometry.location
            });
            //console.log(results)
                //start
            let bounds = foo.getBounds();
            var southWest = bounds.getSouthWest()
            var northEast = bounds.getNorthEast();
            var lngSpan = northEast.lng() - southWest.lng();
            var latSpan = northEast.lat() - southWest.lat();

            var markers = [];
            let center = bounds.getCenter();
            var myLatlng = new google.maps.LatLng(center.lat(), center.lng());

            var map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: myLatlng,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            });

            // Create some markers
            for (var i = 1; i < 2500; i++) {
                var location = new google.maps.LatLng(southWest.lat() + latSpan * Math.random(), southWest.lng() + lngSpan * Math.random());
                var marker = new google.maps.Marker({
                    position: location,
                    map: map
                });

                markers.push(marker);
            }
            //end

          
        } else {
            alert('Search was not successful for the following reason: ' + status);
        }
    });
}