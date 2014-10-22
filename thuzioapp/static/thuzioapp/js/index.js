$(document).ready(function() {
	var level = document.getElementsByTagName("meta")[5].getAttribute('level');
	
	switch(level) {
		case "1":
			$('.regular').show();
			break;

		case "2":
			$('.silver').show();
			break;

		case "3":
			$('.gold').show();
			break;

		case "4":
			$('.premium').show();
			break;
		default:
			return;
	}
});