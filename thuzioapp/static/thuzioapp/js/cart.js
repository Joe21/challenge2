window.onload = (function() {

	storage = [];

	// Render pricing based on user level
	var level = document.getElementsByTagName("meta")[5].getAttribute('level');
	switch(level) {
		case "1":
			$('.regular').show();
			$('.regular .product-price').attr('rendered', true);
			calculateRegular();
			calculateTotal();
			break;

		case "2":
			$('.silver').show();
			$('.silver .product-price').attr('rendered', true)
			break;

		case "3":
			$('.gold').show();
			$('.gold .product-price').attr('rendered', true)
			break;

		case "4":
			$('.platinum').show();
			$('.platinum .product-price').attr('rendered', true)
			break;

		default:
			return false;
	}

	function calculateRegular() {
		var type = $('.regular');
		for (var i = 0; i < type.length; i++ ) {
			var array = [];
			var price = parseFloat(type[i].children[0].innerText);
			var shipping = parseFloat(type[i].children[1].innerText);
			var qty = parseFloat($('.product-box')[i].children[4].childNodes[1].innerText);
			var total = (price + shipping) * qty;
			var	totalText = ('Total: $' + total.toString());
			var productTotal = $('.product-box')[i].children[16].innerText = totalText;

			array.push(price,shipping,qty,total);
			storage.push(array);
		}
	}

	function calculateTotal() {
		sumTotal = 0;
		for (var i = 0; i < storage.length; i++ ) {
			sumTotal += storage[i][3]
		}
		sumTotal = parseFloat(sumTotal).toFixed(2);
		output = ("Total: " + sumTotal.toString())
		$('#current-total').text(output);
	}

	// function bla(el) = {
	// 	// el = $('.platinum .product-price')
	// 	productPrices = $('.product-price')
	// 	for (var i = 0; i < productPrices.length; i++ ) {
	// 		if(productPrices[i].getAttribute('rendered') == true) {
	// 			console.log(i);
	// 			// addme = (productPrices[i].innerText);
	// 			// productPrices[i].attr('price', addme);
	// 		}
	// 	}
	// }

			// productPrices = $('.platinum .product-price');
			// productQty = $('.platinum .product-qty');
			// priceTotal = [];
			// for (var i = 0; i < productPrices.length; i++ ) {
			// 	addme = (productPrices[i].innerText);
			// 	priceTotal.push(addme);
			// }

	// type = $('.regular');
	// for (var i = 0; i < type.length; i++ ) {

	// 	array = [];
	// 	price = parseInt(type[i].children[0].childNodes[1].innerText)
	// 	shipping = 


	// }



	// productPrices = $('.product-price')
	// for (var i = 0; i < productPrices.length; i++ ) {
	// 	if(productPrices[i].getAttribute('rendered') == true) {
	// 		console.log(i);
	// 		// addme = (productPrices[i].innerText);
	// 		// productPrices[i].attr('price', addme);
	// 	}
	// }



	// productPrices = $('.product-price')
	// for (var i = 0; i < productPrices.length; i++ ) {
	// 	if(productPrices[i].getAttribute('rendered') == 'true') {
	// 		var addme = (productPrices[i].innerText);
	// 		productTotal += addme;
	// 	}
	// }


	// // Calculate price totals
	// productTotal = 0;
	// productShipping = 0;
	// purchaseTotal = 0;
	


	// var total = $('#current-total');
	// total.text("Total = " + productTotal);

})