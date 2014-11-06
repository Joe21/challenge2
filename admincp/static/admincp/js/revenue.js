$(document).ready(function() {
	var data;
	var request = $.ajax({
	  url: '/admincp/reporting_api',
	  method: 'GET',
	  dataType: 'json',
	  success: function(d) {
	  	// Mutates the global variable to equal warhead_30 (2nd element in the missile array)
	    data = d;
	    createChart();
	  }
	});

	function createChart() {
		var lineChartData = {
			labels : ["Regular", "Silver", "Gold", "Platinum"],
			datasets : [
				{
					fillColor : "rgba(11,44,60,0.5)",
					strokeColor : "rgba(11,44,60,1)",
					pointColor : "rgba(11,44,60,1)",
					pointStrokeColor : "#fff",
					data : data
				}
			],
		};

		var chartOptions = {
			scaleFontColor: '#333745',
			scaleLineColor: "rgba(51,55,69,.1)",
			scaleFontFamily : "'Cabin'",
		};
		var myLine = new Chart(document.getElementById("canvas").getContext("2d")).Line(lineChartData, chartOptions);
	}
})



