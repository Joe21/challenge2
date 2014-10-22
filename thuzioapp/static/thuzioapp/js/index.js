$(document).ready(function() {
	var level = document.getElementsByTagName("meta")[5].getAttribute('level');
	var membership = $('#membership-price');
	
	switch(level) {
		
		case "1":
		membership.html("Price: {{ product.price_unit_normal }}")
		break

		case "2":
		membership.html("Silver Discounted Price: {{ product.price_unit_silver }}")
		break

		case "3":
		membership.html("Gold Discounted Price: {{ product.price_unit_gold }}")
		break

		case "4":
		membership.html("Premium Discounted Price: {{ product.price_unit_premium }}")
		break
	}
});