Mapper.annotate = new function() {

	this.init = function() {

	}

	this.addMarker = function(e) {

    	var newMarker = new L.marker(e.latlng, {
    		draggable: true })
    		.addTo(Mapper.map_components.map);

    	alert(e.latlng);
		}

}();