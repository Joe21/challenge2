window.onload = (function() {

	var storage = [];

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
			calculateSilver();
			calculateTotal();
			break;

		case "3":
			$('.gold').show();
			$('.gold .product-price').attr('rendered', true)
			calculateGold();
			calculateTotal();
			break;

		case "4":
			$('.platinum').show();
			$('.platinum .product-price').attr('rendered', true)
			calculatePlatinum();
			calculateTotal();
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
			var total = parseFloat((price + shipping) * qty).toFixed(2);
			var	totalText = ('Total: $' + total.toString());
			var productTotal = $('.product-box')[i].children[16].innerText = totalText;

			array.push(price,shipping,qty,total);
			storage.push(array);
		}
	}

	function calculateSilver() {
		var type = $('.silver');
		for (var i = 0; i < type.length; i++ ) {
			var array = [];
			var price = parseFloat(type[i].children[0].innerText);
			var shipping = parseFloat(type[i].children[1].innerText);
			var qty = parseFloat($('.product-box')[i].children[4].childNodes[1].innerText);
			var total = parseFloat((price + shipping) * qty).toFixed(2);
			var	totalText = ('Total: $' + total.toString());
			var productTotal = $('.product-box')[i].children[16].innerText = totalText;

			array.push(price,shipping,qty,total);
			storage.push(array);
		}
	}

	function calculateGold() {
		var type = $('.gold');
		for (var i = 0; i < type.length; i++ ) {
			var array = [];
			var price = parseFloat(type[i].children[0].innerText);
			var shipping = parseFloat(type[i].children[1].innerText);
			var qty = parseFloat($('.product-box')[i].children[4].childNodes[1].innerText);
			var total = parseFloat((price + shipping) * qty).toFixed(2);
			var	totalText = ('Total: $' + total.toString());
			var productTotal = $('.product-box')[i].children[16].innerText = totalText;

			array.push(price,shipping,qty,total);
			storage.push(array);
		}	
	}

	function calculatePlatinum() {
		var type = $('.gold');
		for (var i = 0; i < type.length; i++ ) {
			var array = [];
			var price = parseFloat(type[i].children[0].innerText);
			var shipping = 0;
			var qty = parseFloat($('.product-box')[i].children[4].childNodes[1].innerText);
			var total = parseFloat(price * qty).toFixed(2);
			var	totalText = ('Total: $' + total.toString());
			var productTotal = $('.product-box')[i].children[16].innerText = totalText;

			array.push(price,shipping,qty,total);
			storage.push(array);

		}
	}

	function calculateTotal() {
		var sumTotal = 0;
		for (var i = 0; i < storage.length; i++ ) {
			sumTotal += parseFloat(storage[i][3])
		}
		total = parseFloat(sumTotal).toFixed(2);
		output = ("Order Total: $" + total.toString())
		$('#current-total').text(output);

	}
})