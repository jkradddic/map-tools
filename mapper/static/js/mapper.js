var Mapper = new function() {

	_map = this;
	this.els= {}
	this.form_components = {
		coords: null
	}
	this.map_components = {
		map: null,
		emap: null,
		activeMarkerLayer: null,
		storageMarkerLayer: null
	}

	this.map_id;

	this.init = function() {
		if (Mapper.map_id) {
			Mapper.ui.init();
			Mapper.view.loadData();
			Mapper.ui.generateView();
		}
		else {
			Mapper.ui.init();
			Mapper.gallery.init();
		}
	}

}();

$(document).ready(function() {
	Mapper.init();
});
