var Mapper = new function() {

	_map = this;
	this.els= {}
	this.form_components = {
		coords: null
	}
	this.map_components = {
		map: null,
		activeMarkerLayer: null,
		storageMarkerLayer: null
	}

	this.init = function() {
		Mapper.ui.init();
	}


}();

$(document).ready(function() {
	Mapper.init();
});
